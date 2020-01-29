/////////////////////////////////////////////
#include <string.h>
// char * strerror (int errnum);
/////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int i;

    for ( i = 0; i < 44; i++ ) {
        fprintf(stderr, "%s\n", strerror(i));
    }

    return EXIT_SUCCESS;
}