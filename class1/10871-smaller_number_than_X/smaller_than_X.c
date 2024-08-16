#include <stdio.h>

int main()
{
	int counter, n, x;
	int a[10000];

	scanf("%d %d", &n, &x);

	for (counter = 0; counter < n; counter++)
	{
		scanf("%d", &a[counter]);
	}

	for (counter = 0; counter < n; counter++)
	{
		if (a[counter] < x)
			printf("%d ", a[counter]);
	}

	return 0;
}