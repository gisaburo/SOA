#include <stdio.h>
int enzan06()
{
    int x;
    printf( "Please enter data in integer type: x\n");
    scanf( "%d", &x );
    printf( "x=%d\nx*x=%d\nx*x*x=%d\n", x, x*x, x*x*x );
}
int main()
{
    enzan06();
}