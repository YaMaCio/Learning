#include <Arduino.h>
#include <WiFi.h>

WiFiClient localClient;

const char* ssid = "...";
const char* password = "...";

const uint port = 9876;
const char* ip = "45.79.112.203"; // tcpbin.com's ip

struct CAD
{
	float x;
	float y;
	float db;
};

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

struct SecondMessage
{
	int esp32ID;
	int mp4ID;
	CAD mp4CAndDb;
	unsigned char audio[8192];
};

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

SecondMessage sm;
sm.esp32ID = 1;
sm.mp4ID = 4;
sm.mp4CAndDb.x = 5;
sm.mp4CAndDb.y = 5;
sm.mp4CAndDb.db = 90;

unsigned char fmBA[sizeof(FirstMessage)+8];
unsigned char smBA[sizeof(SecondMessage)+8];
FirstMessage* fmP = &fm;
SecondMessage* smP = &sm;

void setup() {
  Serial.begin(115200);
  Serial.println("Connect Wlan");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(WiFi.localIP());
}

void loop() {
  sendRequestOne();
  delay(5000);
  sendRequestTwo();
}

void readSoundSensors(FirstMessage* fmP)
{
	
}

void readMicrophone(SecondMessage* smP, unsigned char* audio)
{
	
}

int FirstMessageToByteArray(FirstMessage* fm, unsigned char* byteArray)
{
	memcpy(byteArray, reinterpret_cast<unsigned char*>(fm), sizeof(FirstMessage));
	return sizeof(FirstMessage);
}

int SecondMessageToByteArray(SecondMessage* sm, unsigned char* byteArray)
{
	memcpy(byteArray, reinterpret_cast<unsigned char*>(sm), sizeof(SecondMessage));
	return sizeof(SecondMessage);
}

void sendRequestOne() {
	readSoundSensors(fmP);
	FirstMessageToByteArray(fmP, fmBA);

	if (localClient.connect(ip, port)) {                 // Establish a connection

      if (localClient.connected()) {
        localClient.println('A');                      // send data
        Serial.println("[Tx] A");
      }
	}
}

void sendRequestTwo() {
	SecondMessageToByteArray(smP, smBA);
	readMicrophone(smP, audioArray);

	if (localClient.connect(ip, port)) {                 // Establish a connection

      if (localClient.connected()) {
        localClient.println('A');                      // send data
        Serial.println("[Tx] A");
      }
	}
}