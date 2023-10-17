#include "stdio.h"
#include "windows.h"
#include "winsock2.h"

#pragma comment(lib,”ws2_32.lib”)

#define PORT 7777
#define BUF_SIZE 1 << 8

bool TCPPort_isOpen(DWORD port, LPSTR ipAdress)
{
	sockaddr_in client;
	SOCKET sock;
	WSADATA wsdata;
	bool result;

	if (WSAStartup(WINSOCK_VERSION, &wsData))
	{
		WSACleanup();
	}

	ZeroMemory(&client, sizeof(client));
	client.sin_family = AF_INET;
	client.sin_port = htons(port);
	client.sin_addr.s_addr = inet_addr(ipAdress);
	sock = socket(AF_INET, SOCK_STREAM, 0);
	result = (connect(sock, client, sizeof(client)) == 0);

	closesocket(sock);
	WSACleanup();
	return result;
}

void startScanning(WORD startPort, DWORD finishPort, LPSTR ipAdress)
{
	WORD port = startPort;
	while (port <= finishPort)
	{
		if (TCPPort_isOpen(port, ipAdress))
		{
			printf("The port %d is open", port);
		}
		else
		{
			printf("The port %d is closed", port);
		}
	}
}

int main()
{
	HANDLE hInput = GetStdHandle(STD_INPUT_HANDLE);
	HANDLE hOutput = GetStdHandle(STD_OUTPUT_HANDLE);
	DWORD chCount = 0;
	LPSTR ipStr = (LPSTR)calloc(21, sizeof(CHAR));

	memset(ipStr, 0, BUF_SIZE);

	WriteConsoleA(hOutput, "Enter IP adress: ", 17, &chCount, NULL);
	ReadConsoleA(hInput, ipStr, 21, &chCount, NULL);
	startScanning(1, 65536, ipStr);

	free(ipStr);
	CloseHandle(hInput);
	CloseHandle(hOutput);

	return 0;
}