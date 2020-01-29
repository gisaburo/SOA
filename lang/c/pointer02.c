#include <stdio.h>
int pointer02()
{
    char str[] = "hello world";
    *str -= ( 'a' - 'A' );
    *( str + 6 ) -= ('a' - 'A' );
    printf( "%s\n", str );
}
int main()
{
    pointer02();
    return 0;
}