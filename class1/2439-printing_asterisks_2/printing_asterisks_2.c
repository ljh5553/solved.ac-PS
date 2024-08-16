#include <stdio.h>

int main()
{
	int i, j, counter;

	scanf("%d", &counter);

	for (i = 0; i < counter; i++)
	{
		for (j = 1; j < counter-i; j++)
			printf(" ");
		for (j = 0; j <= i; j++)
			printf("*");
		printf("\n");
	}

	return 0;
}