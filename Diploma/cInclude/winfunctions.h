#ifndef _WINFUNCTIONS
#define _WINFUNCTIONS
#include "FirstMessage.h"
#include "SecondMessage.h"
#include "memory.h"
#include <string>
#include "nlohmann\json.hpp"

int __stdcall FirstMessageToByteArray(FirstMessage* fm, unsigned char* byteArray);
FirstMessage __stdcall ByteArrayToFirstMessage(unsigned char* byteArray);
const char* __stdcall FirstMessageCString(FirstMessage* fm);
int __stdcall SecondMessageToByteArray(SecondMessage* sm, unsigned char* byteArray);
SecondMessage __stdcall ByteArrayToSecondMessage(unsigned char* byteArray);
const char* __stdcall SecondMessageCString(SecondMessage* sm);
void __stdcall ExtractAudioFromSecondMessage(SecondMessage* sm, unsigned char* byteArray);
FirstMessage __stdcall getFirstMessageInstance();
SecondMessage __stdcall getSecondMessageInstance();

#endif