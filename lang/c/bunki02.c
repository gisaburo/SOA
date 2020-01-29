#include <stdio.h>
int bunki02()
{
    int x;
    scanf( "%d", &x);
    if( x > 0 )
    {
        if( ( x % 2 ) == 0)
            printf( "Positive even\n");
        else
            printf( "Positive odd\n");
    }
    else
    {
        if( ( x % 2 ) == 0)
            printf( "Negative even\n");
        else
            printf( "Negative odd\n");
    }
}
int main()
{
    bunki02();
}