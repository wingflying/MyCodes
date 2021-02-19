#include <stdio.h>

int main(void)
{
	int i;
	for (i = 0; i <= 1024; i++)
	{
		if ((i & 0xff) == 0)
		{
			printf("%d\n",i);
		}
	}
}

