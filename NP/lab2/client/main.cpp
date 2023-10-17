#include <iostream>
#include <string>
#include <stdio.h>
#include <winsock2.h>
#include <vector>
#include "commonutils.h"

DWORD countThreads;
DWORD repeats;
DWORD WINAPI workThread(LPVOID lpParam);

#pragma comment(lib,"ws2_32.lib")

using namespace std;

DWORD WINAPI workThread(LPVOID lpParam)
{
	SOCKET sock = (SOCKET)lpParam;
	const char* message = "Test message";
	for (int i = 0; i < repeats; i++)
	{
		if (send(sock, message, strlen(message), 0) < 0)
		{
			cout << "Send failed" << endl;
			closeSocket(sock);
			ExitThread(1);
		}
		cout << "Data send" << endl;
	}
	closeSocket(sock);
	ExitThread(0);
}

int main(int argc, char* argv[])
{
	WSADATA wsa;
	SOCKET s;
	struct sockaddr_in server;
	char* message, server_reply[2000];
	int recv_size;
	string ipAddress;
	vector < HANDLE > hThreads;
	vector < SOCKET > sockets;
	int nPort = 5150;
	HANDLE hThread;
	DWORD dwThreadId;

	if (initSocketAPI()) {
		socketError(TRUE, "init socket API");
		return -1;
	}

	cout << "Initialised" << endl;

	cout << "Enter IP: ";
	cin >> ipAddress;
	cout << "Enter number of threads: ";
	cin >> countThreads;
	cout << "Enter number of repeats: ";
	cin >> repeats;

	for (int i = 0; i < countThreads; i++)
	{
		Sleep(100);
		if ((s = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET)
		{
			printf("Could not create socket : %d", WSAGetLastError());
		}

		cout << "Socket created" << endl;

		server.sin_addr.s_addr = inet_addr(ipAddress.c_str());
		server.sin_family = AF_INET;
		server.sin_port = htons(nPort);

		if (connect(s, (struct sockaddr*)&server, sizeof(server)) < 0)
		{
			cout << "Connect error" << endl;
			return 1;
		}
		cout << "Client [";
		cout << inet_ntoa(server.sin_addr) << ":";
		cout << ntohs(server.sin_port) << "] connected\n";
		hThread = CreateThread(NULL, CREATE_SUSPENDED,
			workThread, (LPVOID)s,
			0, &dwThreadId);
		if (hThread == NULL) {
			cout << "Error creating thread: ";
			cout << GetLastError() << endl;
			continue;
		}
		else {
			sockets.push_back(s);
			hThreads.push_back(hThread);
			SetThreadPriority(hThread, THREAD_PRIORITY_BELOW_NORMAL);
			ResumeThread(hThread);
		}
	}

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

	deinitSocketAPI();
	return 0;
}