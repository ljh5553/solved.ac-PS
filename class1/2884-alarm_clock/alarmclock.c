#include <stdio.h>

int main()
{
	int h, m;

	scanf("%d%d", &h, &m);

	if (m >= 45)
		m -= 45;
	else
	{
		if (h < 1)
		{
			h = 23;
		}

		else
		{
			h -= 1;
		}
		m = (m + 60) - 45;
	}

	printf("%d %d", h, m);

	return 0;
}