#include <stdio.h>
int bunki01()
{
    int x;
    int y;
    printf( "Please enter data in integer type: x,y\n");
    scanf( "%d", &x );
    scanf( "%d", &y );
    if( x > y )
        printf( "x is greater than y\n");
    else if( x < y )
        printf( "y is greater than x\n");
    else
        printf( "x equal y\n");
}
int main()
{
    bunki01();
}