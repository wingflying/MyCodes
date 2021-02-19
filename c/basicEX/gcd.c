#include <stdio.h>

int Gcd(int M, int N)
{
	int Rem;
	while (N > 0)
	{
		Rem = M % N;
		M = N;
		N = Rem;
	}
	return M;
}

int main(void)
{
	int a, b;
	
	printf("Please input the value of two numbers:\n");
	scanf("%d:%d", &a, &b);

	printf("The greatest common factor of %d and %d is %d\n", a,b, Gcd(a,b));
}

