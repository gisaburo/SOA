#include <stdio.h>
int hensu5()
{
    int x;
    int y;
    int t;
    x = 3;
    y = 7;
    t = x;
    x = y;
    y = t;
    printf( "x=%d, y=%d", x, y );
}
int main()
{
    hensu5();
}