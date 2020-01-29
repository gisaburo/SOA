#include <stdio.h>
int enzan08()
{
    int x;
    printf( "Please enter data in integer type: x\n");
    scanf( "%d", &x );
    x++;
    printf( "x+1=%d\n", x );
    x--;
    x--;
    printf( "x-2=%d\n", x );
}
int main()
{
    enzan08();
}