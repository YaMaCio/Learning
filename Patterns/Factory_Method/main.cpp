#include <io.h>
#include <fcntl.h>
#include "Factory_method.h"

int main()
{
	_setmode(_fileno(stdout), _O_U16TEXT);
	_setmode(_fileno(stdin), _O_U16TEXT);

	Logistics* ls1 = new CarLogistics();
	Logistics* ls2 = new SeaLogistics();

	Transport* t1 = ls1->CreateTransport();
	t1->deliver();
	Transport* t2 = ls2->CreateTransport();
	t2->deliver();

	return 0;
}