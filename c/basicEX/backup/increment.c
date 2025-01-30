#include <stdio.h>

int increment(int x)
{
	x = x + 1;
	printf("This time the number is %d\n", x);

}

int main(void)
{
	int i = 1, j =2;
	increment(i);
	increment(j);
	printf("i = %d\nj = %d\n", i, j);
}
