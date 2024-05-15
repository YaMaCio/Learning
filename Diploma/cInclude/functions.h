#ifndef _FUNCTIONS
#define _FUNCTIONS
#include "FirstMessage.h"
#include "SecondMessage.h"
#include "memory.h"
#include <string>
#include <nlohmann/json.hpp>

int FirstMessageToByteArray(FirstMessage* fm, unsigned char* byteArray);
FirstMessage ByteArrayToFirstMessage(unsigned char* byteArray);
char* FirstMessageCString(FirstMessage* fm);
int SecondMessageToByteArray(SecondMessage* sm, unsigned char* byteArray);
SecondMessage ByteArrayToSecondMessage(unsigned char* byteArray);
char* SecondMessageCString(SecondMessage* sm);
void ExtractAudioFromSecondMessage(SecondMessage* sm, unsigned char* byteArray);

#endif