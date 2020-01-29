#include <stdio.h>
int bunki03()
{
    int x;
    int y;
    printf( "Please enter data in integer type: x,y\n");
    scanf( "%d", &x );
    scanf( "%d", &y );
    if( x >= 60 && y >= 60 )
        printf( "ok\n" );
    else if( ( x + y) >= 130 )
        printf( "ok\n" );
    else if( ( x + y ) >=100 && x >= 90 || y >= 90 )
        printf( "ok\n" );
    else
        printf( "ng\n" );
}
int main()
{
    bunki03();
    return 0;
}