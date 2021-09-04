#include "Sockets.h" // port: 7777
#define MSG_SIZE 1 << 8
#define BUF_SIZE 1 << 9

#pragma warning(disable : 4996)

int wmain()
{
	WSADATA wsaData;
	SOCKET sock;
	SOCKADDR_IN sa;

	SockInit(wsaData, sock, sa);

	HANDLE hOutput = GetStdHandle(STD_OUTPUT_HANDLE);
	DWORD oCount = 0;
	LPWSTR recvmsg = (LPWSTR)calloc(MSG_SIZE, sizeof(WCHAR));
	LPSTR recvbuf = (LPSTR)calloc(BUF_SIZE, sizeof(CHAR));
	bind(sock, (LPSOCKADDR)&sa, sizeof(sa));
	listen(sock, 1);

	SOCKET cs;
	SOCKADDR_IN csa;
	int csa_size = sizeof(csa);

	while (cs = accept(sock, (LPSOCKADDR)&csa, &csa_size))
	{
		wprintf(L"Client Connected!\n");

		while (recv(cs, recvbuf, BUF_SIZE, MSG_WAITALL) > 0)
		{
			DWORD receivedBytes = MultiByteToWideChar(CP_UTF8, NULL, recvbuf, BUF_SIZE, recvmsg, 0);
			MultiByteToWideChar(CP_UTF8, NULL, recvbuf, BUF_SIZE, recvmsg, receivedBytes);
			WriteConsoleW(hOutput, recvmsg, wcslen(recvmsg), &oCount, NULL);
			//wprintf(L"Debug: %s\n", recvmsg);
			MessageBoxW(NULL, recvmsg, L"Received message", MB_OK | MB_TOPMOST | MB_SETFOREGROUND);
		}
		if (shutdown(cs, SD_BOTH) == SOCKET_ERROR)
		{
			wprintf(L"Shutdown failed with error: %d\n", WSAGetLastError());
			closesocket(cs);
			SockFree(sock);
			exit(2);
		}
		else
		{
			wprintf(L"Client disconnected!\n");
		}
	}

	free(recvmsg);
	free(recvbuf);
	CloseHandle(hOutput);
	closesocket(cs);

	SockFree(sock);

	return 0;
}