#ifndef __LOG_H__
#define __LOG_H__
#define UNICODE
#define _UNICODE
#define MASK L"*"
#define SIZE_BUF 300
#include "Windows.h"
#include "string.h"
#include "malloc.h"
#include "shellapi.h"
#include "stdio.h"

void WriteInLog(HANDLE hFile, LPWSTR path);

#endif