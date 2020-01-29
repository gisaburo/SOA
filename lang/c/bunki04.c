#include <stdio.h>
int bunki04()
{
    int day;
    int zone;
    int f_open = 1;
    printf( "Please select the day of the week\n0=Sun,1=Mon,2=Tes,3=Wed,4=Thu,5=Fri,6=Sat\n");
    scanf( "%d", &day );
    printf( "Please specify a time zone\n0=AM,1=PM,2=MD\n");
    scanf( "%d", &zone );
    if( day == 0 )
        f_open = 0;
    if( zone == 0 && ( day == 2 || day == 5 ) )
        f_open = 0;
    else if( zone == 1 && day == 6 )
        f_open = 0;
    else if( zone == 2 && ( day == 3 || day == 6 ) )
        f_open = 0;
    if( f_open == 1 )
        printf( "open\n" );
    else
        printf( "close\n" );
}
int main()
{
    bunki04();
    return 0;
}