#include "Sockets.h"

void SockInit(WSADATA& wsaData, SOCKET& sock, SOCKADDR_IN& sa)
{
	if (WSAStartup(WINSOCK_VERSION, &wsaData))
	{
		wprintf(L"Winsock wasn't initialized!\n");
		WSACleanup();
	}
	else wprintf(L"Winsock initial OK!\n");

	sock = socket(AF_INET, SOCK_STREAM, 0);
	if (sock == INVALID_SOCKET)
	{
		wprintf(L"Error create socket!\n");
		exit(1);
	}

	ZeroMemory(&sa, sizeof(sa));
	sa.sin_family = AF_INET;
	sa.sin_port = htons(PORT);
}

void SockFree(SOCKET& sock)
{
	closesocket(sock);
	if (WSACleanup())
		wprintf(L"Error Cleanup!\n");
	else
		wprintf(L"Cleanup Good!\n");
}
