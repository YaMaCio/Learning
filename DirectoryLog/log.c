#include "log.h"

DWORD iteration = 0;

void WriteInLog(HANDLE hFile, LPWSTR path)
{
	WIN32_FIND_DATA wfd = { 0 };
	SetCurrentDirectory(path);
	HANDLE search = FindFirstFile(MASK, &wfd);

	if (search == INVALID_HANDLE_VALUE) return;
	do
	{
		LPWSTR strTmp = (LPWSTR)calloc(SIZE_BUF + 1, sizeof(WCHAR));
		LPWSTR curDir = (LPWSTR)calloc(SIZE_BUF + 1, sizeof(WCHAR));
		for(int i = 0;i!=iteration;i++) wcscat_s(curDir, SIZE_BUF, L"\t");
		GetCurrentDirectory(SIZE_BUF, strTmp);

		wcscat_s(strTmp, SIZE_BUF, L"\\");
		wcscat_s(strTmp, SIZE_BUF, wfd.cFileName);

		LPWSTR strTmp_ = (LPWSTR)calloc(wcslen(strTmp) + 1, sizeof(WCHAR));
		wcscpy_s(strTmp_, wcslen(strTmp) + 1, strTmp);
		wcscat_s(curDir, SIZE_BUF, strTmp);

		if (wcscmp(wfd.cFileName, L".") && wcscmp(wfd.cFileName, L".."))
		{
			wcscat_s(curDir, SIZE_BUF, L"\t\t\t");
			if ((wfd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
				&& !(wfd.dwFileAttributes & FILE_ATTRIBUTE_REPARSE_POINT))
			{
				wcscat_s(curDir, SIZE_BUF, L"DIR");
				wcscat_s(curDir, SIZE_BUF, L"\r\n");
				DWORD intCount = 0;
				WriteFile(hFile, curDir, wcslen(curDir) * sizeof(WCHAR), &intCount, NULL);
				++iteration;
				WriteInLog(hFile, strTmp_);
				SetCurrentDirectory(path);
			}
			else
			{
				wcscat_s(curDir, SIZE_BUF, L"FILE");
				wcscat_s(curDir, SIZE_BUF, L"\r\n");
				DWORD intCount = 0;
				WriteFile(hFile, curDir, wcslen(curDir) * sizeof(WCHAR), &intCount, NULL);
			}
		}
	} while (FindNextFile(search, &wfd));
	FindClose(search);
	--iteration;
}
