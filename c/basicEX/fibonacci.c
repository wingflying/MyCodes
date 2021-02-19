#include <stdio.h>

int fib(int i)
{
	int Fib;

	if (i == 0 || i == 1)
		Fib = 1;
	else
		Fib = fib(i-1) +fib(i-2);
	return Fib;
}

int main(void)
{
	int n;

	printf("Please input the number of series:\n");
	scanf("%d", &n);

	printf("The value of Fibonacci series is  %d\n", fib(n));
}
