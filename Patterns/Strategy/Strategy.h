#ifndef __STRATEGY_H__
#define __STRATEGY_H__
#include <iostream>
#include <string>

using namespace std;

class Context;
class Strategy;
class Add;
class Substract;
class Multiply;
class Divide;

class Context
{
private:
	Strategy* strategy;
public:
	Context(Strategy* strat = nullptr) : strategy(strat) {if(strat!=nullptr) cout << ("Strategy was set") << endl;}
	void setStrategy(Strategy* strat)
	{
		if (strategy == nullptr)
		{
			this->strategy = strat;
			cout << ("Strategy was set") << endl;
		}
		else
		{
			delete this->strategy;
			this->strategy = strat;
			cout << ("Strategy was set") << endl;
		}
	}
	~Context()
	{
		delete strategy;
		cout << ("Strategy was removed") << endl;
	}
	double DoStrategy(double a, double b);
};

class Strategy
{
public:
	virtual ~Strategy() {}
	virtual double execute(double a, double b) = 0;
};

class Add : public Strategy
{
public:
	double execute(double a, double b)override;
};

class Substract : public Strategy
{
public:
	double execute(double a, double b)override;
};

class Multiply : public Strategy
{
public:
	double execute(double a, double b)override;
};

class Divide : public Strategy
{
public:
	double execute(double a, double b)override;
};
