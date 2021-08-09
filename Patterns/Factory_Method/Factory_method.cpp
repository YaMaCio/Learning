#include "Factory_method.h"

void Logistics::planDelivery()const 

{ wcout << __TEXT("Настройка плана доставки") << endl; }

void CarLogistics::planDelivery()const
{
		Logistics::planDelivery();
		wcout << __TEXT("Загрузка машин") << endl;
}

void SeaLogistics::planDelivery()const
{
	Logistics::planDelivery();
	wcout << __TEXT("Загрузка корабля") << endl;
}

Transport* CarLogistics::CreateTransport()
{
	wcout << __TEXT("Создан грузовик") << endl;
	return new Car();
}

Transport* SeaLogistics::CreateTransport()
{
	wcout << __TEXT("Создан корабль") << endl;
	return new Ship();
}

void Car::deliver() { wcout << __TEXT("Грузовик отправлен") << endl; }

void Ship::deliver() { wcout << __TEXT("Корабль отправлен") << endl; }