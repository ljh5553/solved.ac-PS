#include <stdio.h>

int main()
{
	int a = 1, b = 1, counter1 = 0, counter2 = 0;
	int x[1000] = { 0 }, y[1000] = { 0 };
	
	while (a != 0 && b != 0)
	{
		scanf("%d %d", &a, &b);
		x[counter1] = a;
		y[counter1] = b;
		counter1++;
	}

	while (counter2 < counter1 - 1)
	{
		printf("%d\n", x[counter2] + y[counter2]);
		counter2++;
	}

	return 0;
}