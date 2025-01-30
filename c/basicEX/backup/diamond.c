#include <stdio.h>

int main(void)
{
	int num, i, j;

	printf("Please input the number of diamond:\n");
	scanf("%d", &num);

	if (num <= 0 || !(num % 2))
		printf("The number is not valid!\n");

	for (i = 1; i <= num/2 + 1; i++)
	{
		for (j = 1; j <= num/2 - i +1; j++)
			printf("\t");
		for (j = 1; j <= 2 * i -1; j++)
			printf("*\t");
		printf("\n");
	}
	
	for(i = 1; i <= num/2; i++)
	{
		for (j = 1; j <= i; j++)
			printf("\t");
		for (j =1; j <= num - 2 * i; j++)
			printf("*\t");
	}
}
	
