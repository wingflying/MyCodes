#include <stdio.h>

void print_time(int hour, int minute)
{
	printf("It is %d:%d now\n", hour, minute);
}

int main(void)
{
	int h = 23, m = 59;
	print_time(h, m);
	return 0;
}

