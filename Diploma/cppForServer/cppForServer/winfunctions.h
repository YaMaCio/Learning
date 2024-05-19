//#ifndef _WINFUNCTIONS
//#define _WINFUNCTIONS
#pragma once
#ifdef CPPFORSERVER_EXPORTS
#define CPPFORSERVER_API __declspec(dllexport)
#else
#define CPPFORSERVER_API __declspec(dllimport)
#endif
#include "FirstMessage.h"
#include "SecondMessage.h"
#include "memory.h"
#include <string>
#include "nlohmann\json.hpp"

extern "C" CPPFORSERVER_API int FirstMessageToByteArray(FirstMessage* fm, unsigned char* byteArray);
extern "C" CPPFORSERVER_API FirstMessage ByteArrayToFirstMessage(unsigned char* byteArray);
extern "C" CPPFORSERVER_API const char* FirstMessageCString(FirstMessage* fm);
extern "C" CPPFORSERVER_API int SecondMessageToByteArray(SecondMessage* sm, unsigned char* byteArray);
extern "C" CPPFORSERVER_API SecondMessage ByteArrayToSecondMessage(unsigned char* byteArray);
extern "C" CPPFORSERVER_API const char* SecondMessageCString(SecondMessage* sm);
extern "C" CPPFORSERVER_API void ExtractAudioFromSecondMessage(SecondMessage* sm, unsigned char* byteArray);
extern "C" CPPFORSERVER_API FirstMessage getFirstMessageInstance();
extern "C" CPPFORSERVER_API SecondMessage getSecondMessageInstance();

//#endif