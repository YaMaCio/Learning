#include "cInclude\winfunctions.h"
using json = nlohmann::json;

int __stdcall FirstMessageToByteArray(FirstMessage* fm, unsigned char* byteArray)
{
	memcpy(byteArray, reinterpret_cast<unsigned char*>(fm), sizeof(FirstMessage));
	return sizeof(FirstMessage);
}

FirstMessage __stdcall ByteArrayToFirstMessage(unsigned char* byteArray)
{
	FirstMessage firstMessage = *(reinterpret_cast<FirstMessage*>(byteArray));
	return firstMessage;
}

const char* __stdcall FirstMessageCString(FirstMessage* fm)
{
	json tmp = {
	  {"esp32ID", fm->esp32ID},
	  {"mp1ID", fm->mp1ID},
	  {"mp1CAndDb", {
		{"x", fm->mp1CAndDb.x},
		{"y", fm->mp1CAndDb.y},
		{"db", fm->mp1CAndDb.db}
	  }},
	  {"mp2ID", fm->mp2ID},
	  {"mp2CAndDb", {
		{"x", fm->mp2CAndDb.x},
		{"y", fm->mp2CAndDb.y},
		{"db", fm->mp2CAndDb.db}
	  }},
	  {"mp3ID", fm->mp3ID},
	  {"mp3CAndDb", {
		{"x", fm->mp3CAndDb.x},
		{"y", fm->mp3CAndDb.y},
		{"db", fm->mp3CAndDb.db}
	  }}
	};
	return tmp.dump().c_str();
}

int __stdcall SecondMessageToByteArray(SecondMessage* sm, unsigned char* byteArray)
{
	memcpy(byteArray, reinterpret_cast<unsigned char*>(sm), sizeof(SecondMessage));
	return sizeof(SecondMessage);
}

SecondMessage __stdcall ByteArrayToSecondMessage(unsigned char* byteArray)
{
	SecondMessage secondMessage = *(reinterpret_cast<SecondMessage*>(byteArray));
	return secondMessage;
}

const char* __stdcall SecondMessageCString(SecondMessage* sm)
{
	json tmp = {
	  {"esp32ID", sm->esp32ID},
	  {"mp4ID", sm->mp4ID},
	  {"mp4CAndDb", {
		{"x", sm->mp4CAndDb.x},
		{"y", sm->mp4CAndDb.y},
		{"db", sm->mp4CAndDb.db}
	  }}
	};
	return tmp.dump().c_str();
}

void __stdcall ExtractAudioFromSecondMessage(SecondMessage* sm, unsigned char* byteArray)
{
	memcpy(byteArray, sm->audio, 8192);
}

FirstMessage __stdcall getFirstMessageInstance()
{
	FirstMessage fm;
	fm.esp32ID = 1;
	fm.mp1ID = 1;
	fm.mp1CAndDb.x = 1;
	fm.mp1CAndDb.y = 5;
	fm.mp1CAndDb.db = 90;
	fm.mp2ID = 2;
	fm.mp2CAndDb.x = 5;
	fm.mp2CAndDb.y = 10;
	fm.mp2CAndDb.db = 90;
	fm.mp3ID = 3;
	fm.mp3CAndDb.x = 10;
	fm.mp3CAndDb.y = 5;
	fm.mp3CAndDb.db = 90;
	return fm;
}

SecondMessage __stdcall getSecondMessageInstance()
{
	SecondMessage sm;
	sm.esp32ID = 1;
	sm.mp4ID = 4;
	sm.mp4CAndDb.x = 5;
	sm.mp4CAndDb.y = 5;
	sm.mp4CAndDb.db = 90;
	for(int i = 0; i < 8192; i++)
	{
		sm.audio[i] = 1;
	}
	return sm;
}