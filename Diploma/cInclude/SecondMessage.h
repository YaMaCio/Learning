#ifndef _SECOND_MESSAGE
#define _SECOND_MESSAGE
#include "CoordsAndDb.h"

struct SecondMessage
{
	int esp32ID;
	int mp4ID;
	CAD mp4CAndDb;
	unsigned char audio[8192];
};

#endif