#pragma once
#include <stdio.h>
#include <io.h>
#include "string.h"
#include "WinSock2.h"
#include "Windows.h"
#define UNICODE
#define _UNICODE
#define PORT 7777

#pragma comment(lib, "Ws2_32.lib")

void SockInit(WSADATA& wsaData, SOCKET& sock, SOCKADDR_IN& sa);
void SockFree(SOCKET& sock);