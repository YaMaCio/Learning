//#ifndef _SECOND_MESSAGE
//#define _SECOND_MESSAGE
#pragma once
#ifdef CPPFORSERVER_EXPORTS
#define CPPFORSERVER_API __declspec(dllexport)
#else
#define CPPFORSERVER_API __declspec(dllimport)
#endif
#include "CoordsAndDb.h"

struct CPPFORSERVER_API SecondMessage
{
	int esp32ID;
	int mp4ID;
	CAD mp4CAndDb;
	unsigned char audio[8192];
};

//#endif