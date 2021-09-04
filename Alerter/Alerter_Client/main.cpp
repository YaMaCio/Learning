#include "Sockets.h" // port: 7777
#define MSG_SIZE 1 << 8
#define BUF_SIZE 1 << 9
#define IP_STR_SIZE 16

#pragma warning(disable : 4996)

int wmain()
{
	WSADATA wsaData;
	SOCKET sock;
	SOCKADDR_IN sa;

	SockInit(wsaData, sock, sa);

	HANDLE hInput = GetStdHandle(STD_INPUT_HANDLE);
	DWORD iCount = 0;
	LPWSTR msg = (LPWSTR)calloc(MSG_SIZE, sizeof(WCHAR));
	LPSTR buf = (LPSTR)calloc(BUF_SIZE, sizeof(CHAR));
	LPSTR ip_str = (LPSTR)calloc(IP_STR_SIZE, sizeof(CHAR));
	wprintf(L"Enter IP adress: ");
	scanf("%15[0-9.]", ip_str);
	if ((sa.sin_addr.S_un.S_addr = inet_addr(ip_str)) == INADDR_NONE)
	{
		wprintf(L"Incorrect adress!");
		Sleep(500);
		exit(2);
	}
	connect(sock, (LPSOCKADDR)&sa, sizeof(sa));
	wprintf(L"Message: ");
	ReadConsoleW(hInput, msg, (MSG_SIZE)-1, &iCount, NULL);
	DWORD writtenBytes = WideCharToMultiByte(CP_UTF8, NULL, msg, iCount, buf, 0, NULL, NULL);
	WideCharToMultiByte(CP_UTF8, NULL, msg, iCount, buf, writtenBytes, NULL, NULL);
	if ((send(sock, buf, BUF_SIZE, 0)) == SOCKET_ERROR)
	{
		wprintf(L"Can't send message!");
		Sleep(500);
		exit(3);
	}

	free(msg);
	free(buf);
	CloseHandle(hInput);

	SockFree(sock);

	return 0;
}