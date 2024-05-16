#ifndef _FUNCTIONS
#define _FUNCTIONS
#include "FirstMessage.h"
#include "SecondMessage.h"
#include "memory.h"
#include <string>
#include "nlohmann\json.hpp"

int __cdecl FirstMessageToByteArray(FirstMessage* fm, unsigned char* byteArray);
FirstMessage __cdecl ByteArrayToFirstMessage(unsigned char* byteArray);
const char* __cdecl FirstMessageCString(FirstMessage* fm);
int __cdecl SecondMessageToByteArray(SecondMessage* sm, unsigned char* byteArray);
SecondMessage __cdecl ByteArrayToSecondMessage(unsigned char* byteArray);
const char* __cdecl SecondMessageCString(SecondMessage* sm);
void __cdecl ExtractAudioFromSecondMessage(SecondMessage* sm, unsigned char* byteArray);
FirstMessage __cdecl getFirstMessageInstance();
SecondMessage __cdecl getSecondMessageInstance();

#endif