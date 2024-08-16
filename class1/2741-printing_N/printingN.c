#include <stdio.h>

int main()
{
    int input, i=1;
    
    scanf("%d", &input);
    
    while(input > 0)
    {
        printf("%d\n", i);
        i++;
        input--;
    }
    
    return 0;
}