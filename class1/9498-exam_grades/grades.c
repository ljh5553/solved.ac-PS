#include <stdio.h>

int main()
{
    int grade;
    
    scanf("%d", &grade);
    
    if(grade >= 90) printf("A\n");
    else if(grade <= 89 && grade >= 80) printf("B\n");
    else if(grade <= 79 && grade >= 70) printf("C\n");
    else if(grade <= 69 && grade >= 60) printf("D\n");
    else printf("F\n");
    
    return 0;
}