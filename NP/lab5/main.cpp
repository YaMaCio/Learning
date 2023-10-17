#include "commonutils.h"

#include <vector>

#include <fstream>

#include <sstream>

#define WM_SOCKET (WM_USER + 1)
//Визначаємо коди помилок при відправці відповідей та файлів
//Код помилки при відправці НТТР-відповіді
#define ERR_SEND_HTTP_HEADER - 1
//Код помилки при відкритті запрошуваного файлу
#define ERR_OPEN_FILE - 2
//Код помилки при відправці запрошуваного файлу
#define ERR_SEND_FILE - 3
using namespace std;
//Для Win32 використовуємо критичні секції
CRITICAL_SECTION syncObj;
//Функція потоку
DWORD WINAPI clientThread(LPVOID);
//Шаблони запитів та відповіді серверу
#define DESCRIPTION "Simple web server demonstrates \
work with simple HTTP-requests"
#define HTTP_HEADER "HTTP/1.1 200 OK\r\n"\
"Content-Length: %d\r\n"\
"Content-Type: text/html\r\n\r\n"
#define ERROR_FILE_FOUND_RESPONSE\
  "<html><body><H1>Error</H1><p>\
File %s not found.</body></html>"
//Шлях до виконуваної програми
char appPath[BUFFER_SIZE];
//Масив ідентифікаторів потоків
int nPort;
vector < HANDLE > hThreads;
vector < SOCKET > sockets;
int argc;
char** argv;

//Функція для переведення 16-вих символів у 10-ві цифри
    int HexCharToDecDig(char hexChar) {
      if (hexChar >= ‘0’ && hexChar <= ‘9’)
        return hexChar - ’0’;
      else
        switch (hexChar) {
        case‘ A’:
          return 10;
        case‘ B’:
          return 11;
        case‘ C’:
          return 12;
        case‘ D’:
          return 13;
        case‘ E’:
          return 14;
        case‘ F’:
          return 15;
        default:
          return -1;
        }
    }
	
    int getFilenameFromHTTPrequest(char * request,
        char * fileName) {
        int i = 5, j = 0;
        //Згідно із стандартом URL ряд символів пробіл, #, кирилиця і
        //ін. замінюється на послідовність %код_символу (у 16-річній
        //системі). Наприклад, пробіл замінюється на %20.
        while (request[i] != ‘‘) {
          if (request[i] != ‘ % ’)
            fileName[j++] = request[i++];
          else {
            fileName[j++] = HexCharToDecDig(request[++i]) * 16 +
              HexCharToDecDig(request[++i]);
            ++i;
          }
        }
        fileName[j] = ‘\0’;
        while (char * ch = strchr(fileName, ’/’)) *ch = PATH_DELIM; #endif // OS_WINDOWS
            return 1;
          }
          //Функція для синхронізованого виведення повідомлень 
          //з потоку на консоль
          void syncOutPutStr(stringstream & buffer) {
            if (TryEnterCriticalSection( & syncObj)) {
              cout << buffer.str() << endl;
              LeaveCriticalSection( & syncObj);
            }
            buffer.str(string());
          }
          //Функція для синхронізованої передачі файлу клієнту
          int syncSendFile(SOCKET sock, char * sendFileName,
            int & nTotalSend) {
            int result = 0;
            if (TryEnterCriticalSection( & syncObj)) {
              //Відкриваємо файл
              ifstream iFile(sendFileName);
              if (iFile.good()) {
                char dataBuffer[MAX_BUFFER_SIZE];
                char HTTPResponse[MAX_BUFFER_SIZE];
                //Кількість зчитаних і переданих байт даних
                int nSend = 0;
                nTotalSend = 0;
                while (!iFile.eof()) {
                  memset(dataBuffer, 0, MAX_BUFFER_SIZE);
                  memset(HTTPResponse, 0, MAX_BUFFER_SIZE);
                  iFile.read(dataBuffer, MAX_BUFFER_SIZE);
                  nSend = iFile.gcount();
                  if (nSend <= 0)
                    break;
                  sprintf(HTTPResponse, HTTP_HEADER, nSend);
                  if (send(sock, HTTPResponse, strlen(HTTPResponse), 0) < 0) {
                    result = ERR_SEND_HTTP_HEADER;
                    break;
                  }
                  nSend = send(sock, dataBuffer, nSend, 0);
                  if (nSend < 0) {
                    result = ERR_SEND_FILE;
                    break;
                  }
                  nTotalSend += nSend;
                }
              } else result = ERR_OPEN_FILE;
              iFile.close();
              LeaveCriticalSection( & syncObj);
            }
            return result;
          }
		  
          DWORD WINAPI clientThread(LPVOID lpParam) {
              //Перетворимо параметр до типу SOCKET
              SOCKET sock = (SOCKET) lpParam;
              struct sockaddr_in clientAddr;
              int ret;
              int caSize = sizeof(clientAddr);
              //Отримаємо дані про сокет клієнту
              getpeername(sock, (struct sockaddr * ) & clientAddr, & caSize);
              char dataBuffer[MAX_BUFFER_SIZE];
              char HTTPResponse[BUFFER_SIZE];
              char fileName[MAX_BUFFER_SIZE];
              char filePath[MAX_BUFFER_SIZE];
              stringstream ss;
              int totalsize = 0;
              do {
                memset(fileName, 0, MAX_BUFFER_SIZE);
                memset(filePath, 0, MAX_BUFFER_SIZE);
                strcpy(filePath, appPath);
                ret = recv(sock, dataBuffer, MAX_BUFFER_SIZE, 0);
                if (ret < 0)
                  continue;
                //Отримуємо ім’я файлу з НТТР-запиту
                getFilenameFromHTTPrequest(dataBuffer, fileName);
                strcat(filePath, fileName);
                //Якщо файл не вказано, шукаємо файл index.html
                if (filePath[strlen(filePath) - 1] == PATH_DELIM)
                  strcat(filePath, "index.html");
                //Якщо розширення не вказано, шукаємо файли.html
                if (!strchr(filePath, ’.’))
                  strcat(filePath, ".html");
                ss << "Requested file: " << filePath << endl;
                syncOutPutStr(ss);
                switch (syncSendFile(sock, filePath, totalsize)) {
                case ERR_SEND_HTTP_HEADER:
                  ss << "Error send header" << endl;
                  ss << "Successfully sent " << totalsize << " bytes\n";
                  break;
                case ERR_SEND_FILE:
                  ss << "Error send file: " << filePath << endl;
                  ss << "Successfully sent " << totalsize << " bytes\n";
                  break;
                case ERR_OPEN_FILE:
                  sprintf(HTTPResponse, ERROR_FILE_FOUND_RESPONSE, fileName);
                  sprintf(dataBuffer, HTTP_HEADER, strlen(HTTPResponse));
                  send(sock, dataBuffer, strlen(dataBuffer), 0);
                  send(sock, HTTPResponse, strlen(HTTPResponse), 0);
                  ss << "Error send request file: " << filePath << endl;
                  break;
                default:
                  ss << "Successfully sent " << totalsize << " bytes";
                  ss << " from requested file: " << filePath << endl;
                }
                syncOutPutStr(ss);
              } while (ret > 0);
              ss << "Client [" << inet_ntoa(clientAddr.sin_addr);
              ss << ":" << ntohs(clientAddr.sin_port);
              ss << "] disconnected" << endl;
              syncOutPutStr(ss);
              closeSocket(sock);
              sock = 0;
              return 0;
            }

HWND MakeWorkerWindow(void)
{
   WNDCLASS wndclass;
   CHAR *ProviderClass = "AsyncSelect";
   HWND Window;

   wndclass.style = CS_HREDRAW | CS_VREDRAW;
   wndclass.lpfnWndProc = (WNDPROC)WindowProc;
   wndclass.cbClsExtra = 0;
   wndclass.cbWndExtra = 0;
   wndclass.hInstance = NULL;
   wndclass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
   wndclass.hCursor = LoadCursor(NULL, IDC_ARROW);
   wndclass.hbrBackground = (HBRUSH) GetStockObject(WHITE_BRUSH);
   wndclass.lpszMenuName = NULL;
   wndclass.lpszClassName = (LPCWSTR)ProviderClass;

   if (RegisterClass(&wndclass) == 0)
   {
      printf("RegisterClass() failed with error %d\n", GetLastError());
      return NULL;
   }
   else printf("RegisterClass() is OK!\n");

   // Create a window
   if ((Window = CreateWindow(
      (LPCWSTR)ProviderClass,
      L"",
      WS_OVERLAPPEDWINDOW,
      CW_USEDEFAULT,
      CW_USEDEFAULT,
      CW_USEDEFAULT,
      CW_USEDEFAULT,
      NULL,
      NULL,
      NULL,
      NULL)) == NULL)
   {
      printf("CreateWindow() failed with error %d\n", GetLastError());
      return NULL;
   }
   else printf("CreateWindow() is OK!\n")
   return Window;
}

int WINAPI WinMain(HINSTANCE hInstance,
					HINSTANCE hPrevInstance,
					LPSTR lpCmdLine,
					int nCmdShow) {
	MSG msg;
	HWND Window;
    SOCKET listenSocket, newClient;
    struct sockaddr_in serverAddr, clientAddr;
	
	if ((Window = MakeWorkerWindow()) == NULL)
	{
      printf("MakeWorkerWindow() failed!\n");
      return 1;
	}
	else printf("MakeWorkerWindow() is OK!\n");
	
	LPSTR* lpArgv = CommandLineToArgvA(
					GetCommandLineA(),
					&argc);
	argv = (char**)malloc(argc*sizeof(char*));
	int size, i = 0;
	for(;i<argc;++i)
	{
		size = wcslen(lpArgv[i]) + 1;
		argv[i] = malloc(size);
		wcstombs(argv[i], lpArgv[i], size);
	}
	
    int clientAddrLen;
    //Ініціюємо критичну секцію для синхронізації
    InitializeCriticalSection( & syncObj);
    nPort = 5150, ret;
    HANDLE hThread;
    DWORD dwThreadId;
    char strPort[6];
    //З командного рядка визначаємо заданий порт серверу
    if (getParameter(argv, argc, "-port", strPort, ’: ’)) {
      int tempPort = atoi(strPort);
      if (tempPort > 0)
        nPort = tempPort;
      else {
        cout << "\nError command argument " << argv[0];
        cout << " -port:<integer value>\n";
        cout << "\nUsage " << argv[0] << " -port:<integer value>\n";
      }
    }
    memset(appPath, 0, BUFFER_SIZE);
    if (!extractFilePath(appPath, argv[0]))
      strcpy(appPath, ".\\");
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
    listen(listenSocket, LINEQ);
    printInfo(argv[0], DESCRIPTION);
    cout << "Waiting incoming connections in port:" << nPort << endl;
    //Нескінченний цикл очікування запитів на підключення
    while (GetMessage(&msg, NULL, 0, 0)) {
      //Призупиняємо виконання циклу на 100 мс
      Sleep(100);
	  WSAAsyncSelect(Accept, hWnd, WM_SOCKET, FD_ACCEPT|FD_CLOSE);
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
    TranslateMessage(&msg);
    DispatchMessage(&msg);
    }
}
	
LRESULT WindowProc(HWND hWindow, UINT uMessage, WPARAM wParam, LPARAM lParam){
    SOCKET Accept;
	switch (uMessage)
    {
	case WM_PAINT:
	break;
    case WM_CLOSE:
		//Надсилаємо клієнтам повідомлення про завершення 
		//роботи серверу.
		for (int i = 0; i < sockets.size(); ++i) {
			if (sockets[i] > 0)
			  send(sockets[i], shutdownServerCmd,
			strlen(shutdownServerCmd) + 1, 0);
		}
		//Якщо є активні потоки, то чекаємо їх завершення
		//і вивільняємо ресурси
		switch (WaitForMultipleObjects(hThreads.size(), & hThreads[0],
			  TRUE, INFINITE)) {
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
		int i = 0;
		for(;i<argc;++i)
			free(argv[i]);
		free(argv);
		LocalFree(lpArgv);
		DestroyWindow(hWindow);
        PostQuitMessage(0);
        return 0;
	break;
	case WM_SOCKET:
	if(WSAGETSELECTEVENT(lParam))
	{
		closeSocket(wParam); break;
	}
	switch(WSAGETSELECTEVENT(lParam))
	{
		case FD_ACCEPT:
		struct sockaddr_in clientAddr;
		DWORD clientAddrLen = sizeof(clientAddr);
		Accept = accept(wParam,
        (struct sockaddr * ) & clientAddr, &
        clientAddrLen);
		if (newClient <= 0) {
        cout << "Connections error\n";
        break;
      }
		cout << "Client [";
		cout << inet_ntoa(clientAddr.sin_addr) << ":";
		cout << ntohs(clientAddr.sin_port) << "] connected\n";
		WSAAsyncSelect(Accept, hWnd, WM_SOCKET, FD_READ|FD_WRITE|FD_CLOSE);
		break;
		case FD_READ:
		HANDLE hThread;
		DWORD dwThreadId;
		//Створюємо потік, якому передаємо клієнтський сокет
		hThread = CreateThread(NULL, CREATE_SUSPENDED,
        clientThread, (LPVOID) wParam,
        0, & dwThreadId);
		if (hThread == NULL) {
          cout << "Error creating thread: ";
          cout << GetLastError() << endl;
          continue;
        } else { //Додаємо сокет у масив
          sockets.push_back(wParam);
          hThreads.push_back(hThread);
          SetThreadPriority(hThread, THREAD_PRIORITY_BELOW_NORMAL);
          ResumeThread(hThread);
        }
		break;
		case FD_WRITE:
		
		break;
		case FD_CLOSE:
		
		break;
	}
	}
	return DefWindowProc(hWindow, uMessage, wParam, lParam);
}