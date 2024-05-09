#ifndef _FIRST_MESSAGE
#define _FIRST_MESSAGE
#include "CoordsAndDb.h"

struct FirstMessage
{
	int esp32ID;
	int mp1ID;
	CAD mp1CAndDb;
	int mp2ID;
	CAD mp2CAndDb;
	int mp3ID;
	CAD mp3CAndDb;
};

#endif