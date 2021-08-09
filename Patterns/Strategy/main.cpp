#include "Strategy.h"

int main()
{
	Context* context = new Context(new Add);
	cout << context->DoStrategy(10, 5) << endl;
	context->setStrategy(new Substract);
	cout << context->DoStrategy(10, 5) << endl;
	context->setStrategy(new Multiply);
	cout << context->DoStrategy(10, 5) << endl;
	context->setStrategy(new Divide);
	cout << context->DoStrategy(10, 5) << endl;

	delete context;

	return 0;
}