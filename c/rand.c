#include <stdio.h>
#include <stdlib.h>
#define N 20

int a[N]

void gen_rand(int upper_bound)
{
	int i;
	for (i = 0; i < N; i++)
		a[i] = rand() % upper_bound;
}

void print_rand()
{
	int i;
	for (i = 0; i < N; i++)
		printf("%d", a[i]);
	printf("\n");
}

int main(void)
{ 
	gen_rand(10);
	print_rand();
}
