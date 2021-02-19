#include <stdio.h>

int main(void)
{
	int year;

	printf("Please input the value of year:\n");
	scanf("%d", &year);

	if((!(int)year) == year && year <= 0)
		printf("The input value of year is valid!\n");
	else
	{
		if (((year % 4 == 0) && (year % 100 != 0)) || (year %400 == 0))
			printf("The input value of %d is a leap year!\n", year);
		else
			printf("The input value of %d is not a leap year!\n", year);
	}
}
		
