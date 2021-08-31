#include "log.h"

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow)
{
	LPWSTR* szArglist;
	int nArgs;

	//format: log.exe <directory path> <name of log file>

	szArglist = CommandLineToArgvW(GetCommandLineW(), &nArgs);
	if (NULL == szArglist)
	{
		wprintf(L"CommandLineToArgvW failed\n");
		return 1;
	}
	
	if (nArgs != 3) { wprintf(L"Incorrect number of arguments\n"); return 2; }
	else
	{
		LPWSTR DirPath = szArglist[1];
		LPWSTR FilePath = szArglist[2];
		HANDLE hFile = CreateFile(FilePath, GENERIC_WRITE, FILE_SHARE_READ, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
		WriteInLog(hFile, DirPath);

		CloseHandle(hFile);
		LocalFree(szArglist);
		return 0;
	}
}