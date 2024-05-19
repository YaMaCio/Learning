//#ifndef _FIRST_MESSAGE
//#define _FIRST_MESSAGE
#pragma once
#ifdef CPPFORSERVER_EXPORTS
#define CPPFORSERVER_API __declspec(dllexport)
#else
#define CPPFORSERVER_API __declspec(dllimport)
#endif
#include "CoordsAndDb.h"

struct CPPFORSERVER_API FirstMessage
{
	int esp32ID;
	int mp1ID;
	CAD mp1CAndDb;
	int mp2ID;
	CAD mp2CAndDb;
	int mp3ID;
	CAD mp3CAndDb;
};

//#endif