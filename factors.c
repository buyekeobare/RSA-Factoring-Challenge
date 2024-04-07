#include <stdio.h>

int main()
{
    long long int value = 239809320265259;
    long int num1 = 2;
    long int num2;

    while (value % num1)
    {
        if (num1 <= value)
        {
            num1++;
        }
        else {
            return (-1);
        }
    }

    num2 = value / num1;
    printf("%lld = %ld * %ld\n", value, num2, num1);
    return (0);
}
