#include <stdio.h>

int main()
{
	double val1, val2;
	double rst;

	scanf("%lf%lf", &val1, &val2);

	rst = val1 / val2;

	printf("%.9lf", rst);

	return 0;
}