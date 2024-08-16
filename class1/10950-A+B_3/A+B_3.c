#include <stdio.h>

int main()
{
	int i, t;
	int a[100], b[100];

	scanf("%d", &t);

	for (i = 0; i < t; i++)
		scanf("%d %d", &a[i], &b[i]);

	for (i = 0; i < t; i++)
		printf("%d\n", a[i] + b[i]);

	return 0;
}