#ifndef _FUNCTIONS
#define _FUNCTIONS
#include "FirstMessage.h"
#include "SecondMessage.h"
#include "memory.h"
#include <string>
#include <nlohmann/json.hpp>
using json = nlohmann::json;

int FirstMessageToByteArray(FirstMessage* fm, unsigned char* byteArray)
{
	memcpy(byteArray, static_cast<unsigned char*>(fm), sizeof(FirstMessage));
	return sizeof(FirstMessage);
}

FirstMessage ByteArrayToFirstMessage(unsigned char* byteArray)
{
	FirstMessage firstMessage = *(reinterpret_cast<FirstMessage*>(byteArray));
	return firstMessage;
}

char* FirstMessageCString(FirstMessage* fm)
{
	json tmp = {
	  {"esp32ID", fm->esp32ID},
	  {"mp1ID", fm->mp1ID},
	  {"mp1CAndDb", {
		{"x", fm->mp1CAndDb.x}
		{"y", fm->mp1CAndDb.y}
		{"db", fm->mp1CAndDb.db}
	  }},
	  {"mp2ID", fm->mp2ID},
	  {"mp2CAndDb", {
		{"x", fm->mp2CAndDb.x}
		{"y", fm->mp2CAndDb.y}
		{"db", fm->mp2CAndDb.db}
	  }},
	  {"mp3ID", fm->mp3ID},
	  {"mp3CAndDb", {
		{"x", fm->mp3CAndDb.x}
		{"y", fm->mp3CAndDb.y}
		{"db", fm->mp3CAndDb.db}
	  }}
	}
	return tmp.dump().c_str();
}

int SecondMessageToByteArray(SecondMessage* sm, unsigned char* byteArray)
{
	memcpy(byteArray, static_cast<unsigned char*>(sm), sizeof(SecondMessage));
	return sizeof(SecondMessage);
}

SecondMessage ByteArrayToSecondMessage(unsigned char* byteArray)
{
	SecondMessage secondMessage = *(reinterpret_cast<SecondMessage*>(byteArray));
	return secondMessage;
}

char* SecondMessageCString(SecondMessage* sm)
{
	json tmp = {
	  {"esp32ID", fm->esp32ID},
	  {"mp4ID", fm->mp1ID},
	  {"mp4CAndDb", {
		{"x", fm->mp1CAndDb.x}
		{"y", fm->mp1CAndDb.y}
		{"db", fm->mp1CAndDb.db}
	  }}
	}
	return tmp.dump().c_str();
}

void ExtractAudioFromSecondMessage(SecondMessage* sm, unsigned char* byteArray)
{
	memcpy(byteArray, sm->audio, 8192);
}

#endif