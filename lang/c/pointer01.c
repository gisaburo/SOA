#include <stdio.h>
int pointer01()
{
    int x;
    int* p;
    p = &x;
    *p = 12;
    printf( "%d\n", x );
}
int main()
{
    pointer01();
    return 0;
}