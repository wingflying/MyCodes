#include <stdio.h>

int main(void)
{
	int i, a, b, num = 0;

	for(i = 1; i <100; i++)
	{
	a = i % 10;
	b = i % 100 /10;

	if (a == 9)
		num = num + 1;
	if (b == 9)
		num = num + 1;
	}

	printf("There are %d number of 9 from 1 to 100\n", num);
}
