#include <stdio.h>
int pointer03()
{
    int values[10];
    int i;
    for( i = 0 ; i < 10 ; i++ )
      scanf( "%d", values + i );
    for( i = 9 ; i >= 0 ; i-- )
      printf( "\n%d", *( values + i ) );
}
int main()
{
    pointer03();
    return 0;
}