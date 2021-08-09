#include "Strategy.h"

double Context::DoStrategy(double a, double b)
{
	return this->strategy->execute(a, b);
}

double Add::execute(double a, double b)
{
	return a + b;
}

double Substract::execute(double a, double b)
{
	return a - b;
}

double Multiply::execute(double a, double b)
{
	return a * b;
}

double Divide::execute(double a, double b)
{
	return a / b;
}
