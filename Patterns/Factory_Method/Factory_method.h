#ifndef __FACTORY_METHOD_H__
#define __FACTORY_METHOD_H__
#define UNICODE
#define _UNICODE
#include <iostream>
#include <string>
#include <Windows.h>

using namespace std;

class Logistics;
class Transport;
class CarLogistics;
class SeaLogistics;
class Car;
class Ship;

class Logistics
{
public:
	Logistics(){}
	virtual ~Logistics(){}
	virtual void planDelivery()const;
	virtual Transport* CreateTransport() = 0;
};

class CarLogistics : public Logistics
{
public:
	CarLogistics() {}
	virtual ~CarLogistics() {}
	void planDelivery()const override;
	Transport* CreateTransport() override;
};

class SeaLogistics : public Logistics
{
public:
	SeaLogistics() {}
	virtual ~SeaLogistics() {}
	void planDelivery()const override;
	Transport* CreateTransport() override;
};

class Transport
{
public:
	Transport(){}
	virtual ~Transport(){}
	virtual void deliver() = 0;
};

class Car : public Transport
{
public:
	Car() {}
	~Car() {}
	void deliver() override;
};

class Ship : public Transport
{
public:
	Ship() {}
	~Ship() {}
	void deliver() override;
};
#endif 