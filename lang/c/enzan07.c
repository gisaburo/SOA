#include <stdio.h>
int enzan07()
{
    int x,y;
    printf( "Please enter data in integer type: x\n");
    scanf( "%d", &x );
    y = x / 2;
    printf( "quotient=%d\nremainder=%d\n", x/y, x%y );
}
int main(){
    enzan07();
}