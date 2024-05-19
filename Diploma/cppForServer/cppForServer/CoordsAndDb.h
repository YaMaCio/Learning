//#ifndef _COORDS_AND_DB
//#define _COORDS_AND_DB
#pragma once
#ifdef CPPFORSERVER_EXPORTS
#define CPPFORSERVER_API __declspec(dllexport)
#else
#define CPPFORSERVER_API __declspec(dllimport)
#endif

struct CPPFORSERVER_API CAD
{
	float x;
	float y;
	float db;
};

//#endif