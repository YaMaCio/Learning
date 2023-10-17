#include "commonutils.h"

#include <vector>

CRITICAL_SECTION syncObj;
//Функція потоку
DWORD WINAPI clientThread(LPVOID lpParam);
using namespace std;
int main(int argc, char * argv[]) {
    SOCKET listenSocket, newClient;
    struct sockaddr_in serverAddr, clientAddr;
    int clientAddrLen;
    //Ініціюємо критичну секцію для синхронізації
    InitializeCriticalSection( & syncObj);
    int nPort = 5150;
    HANDLE hThread;
    DWORD dwThreadId;
    char strPort[6];
    //З командного рядка визначаємо заданий порт серверу
    if (getParameter(argv, argc, "-port", strPort, ’: ’)) {
      int tempPort = atoi(strPort);
      if (tempPort > 0)
        nPort = tempPort;
      else {
        cout << "\nError command argument ";
        cout << argv[0] << " -port:<integer value>\n";
        cout << "\nUsage " << argv[0] << " -port:<integer value>\n";
      }
    }
    //Ініціюємо бібліотеку сокетів
    if (initSocketAPI()) {
      socketError(TRUE, "init socket API");
      return -1;
    }
    listenSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(nPort);
    serverAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    //Зв’язуємо сокет з адресою машини
    if (bind(listenSocket, (struct sockaddr * ) & serverAddr,
        sizeof(serverAddr))) {
      socketError(TRUE, "bind socket");
      return -2;
    }
    //Переводимо сокет у пасивний режим
    listen(listenSocket, 5);
    printInfo(argv[0]);
    cout << "Waiting incoming connections in port:" << nPort << endl;
    //Масив ідентифікаторів потоків
    vector < HANDLE > hThreads;
    vector < SOCKET > sockets;
    //Нескінченний цикл очікування
    while (1) {
      Sleep(100);
      clientAddrLen = sizeof(clientAddr);
      newClient = accept(listenSocket,
        (struct sockaddr * ) & clientAddr, &
        clientAddrLen);
      if (newClient <= 0) {
        cout << "Connections error\n";
        break;
      }
      cout << "Client [";
      cout << inet_ntoa(clientAddr.sin_addr) << ":";
      cout << ntohs(clientAddr.sin_port) << "] connected\n";
      //Створюємо потік, якому передаємо клієнтський сокет
      hThread = CreateThread(NULL, CREATE_SUSPENDED,
        clientThread, (LPVOID) newClient,
        0, & dwThreadId);
      if (hThread == NULL) {
          cout << "Error creating thread: ";
          cout << GetLastError() << endl;
          continue;
        } else { //Додаємо сокет у масив
          sockets.push_back(newClient);
          hThreads.push_back(hThread);
          SetThreadPriority(hThread, THREAD_PRIORITY_BELOW_NORMAL);
          ResumeThread(hThread);
        }
      }
      //Надсилаємо клієнтам повідомлення про завершення
      //роботи серверу.
      for (int i = 0; i < sockets.size(); ++i) {
        send(sockets[i], shutdownServerCmd,
          strlen(shutdownServerCmd), 0);
      }
      //Якщо є активні потоки, то чекаємо їх завершення
      // і вивільняємо ресурси
      if (!hThreads.empty())
      switch (WaitForMultipleObjects(hThreads.size(), &
          hThreads[0], TRUE, INFINITE)) {
      case WAIT_OBJECT_0:
        for (int i = 0; i < hThreads.size(); ++i) {
          CloseHandle(hThreads[i]);
        }
        break;
      case WAIT_TIMEOUT:
        cout << "Error finished child threads\n";
        break;
      }
      //Видаляємо критичну секцію
      DeleteCriticalSection( & syncObj);
      //Закриваємо слухаючий сокет
      closeSocket(listenSocket);
      //Звільняємо ресурси системи
      deinitSocketAPI();
      return 0;
    }
}

DWORD WINAPI clientThread(LPVOID lpParam) {
    //Перетворимо параметр до типу SOCKET
    SOCKET sock = (SOCKET) lpParam;
    struct sockaddr_in clientAddr;
    int ret;
    int caSize = sizeof(clientAddr);
    //Отримуємо дані про сокет клієнта
    getpeername(sock, (struct sockaddr * ) & clientAddr, & caSize);
    char dataBuffer[BUFFER_SIZE];
    memset(dataBuffer, 0, BUFFER_SIZE);
    while (1) {
        //Отримуємо дані від клієнта
        ret = recv(sock, dataBuffer, BUFFER_SIZE, 0);
        if (ret == 0) continue;
        else
        if (ret < 0) break;
        dataBuffer[ret] = ‘\0’;
        char response[BUFFER_SIZE];
        snprintf(response, BUFFER_SIZE,
            SUCCESS_RESPONSE_SERVER_CMD, ret);
        if (send(sock, response, strlen(response), 0) < 0) {
            break;
        }
        //Синхронно виводимо ці дані на консоль
        if (TryEnterCriticalSection( & syncObj)) {
            cout << "[" << inet_ntoa(clientAddr.sin_addr);
            cout << ":" << ntohs(clientAddr.sin_port);
            cout << "]: " << dataBuffer << endl;
            LeaveCriticalSection( & syncObj);
        }
    } //while
    if (TryEnterCriticalSection( & syncObj)) {
        cout << "[" << inet_ntoa(clientAddr.sin_addr);
        cout << ":" << ntohs(clientAddr.sin_port);
        cout << "] disconnected" << endl;
        LeaveCriticalSection( & syncObj);
    }
    return 0;
}