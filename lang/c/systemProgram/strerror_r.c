///////////////////////////////////////////////////////
#include <string.h>
// int strerror_r (int errnum, char *buf, size_t len);
///////////////////////////////////////////////////////
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

#define MSG_LEN 100

int main(void) {
    FILE *fp;
    char msg_buff[MSG_LEN];
    int error_num;

    fp = fopen( "file.name", "r" );
    if( fp == NULL) {
        error_num = strerror_r (errno, msg_buff, MSG_LEN);

        switch (error_num) {
            case 0:
                printf( "Unable to open file: %s\n", msg_buff);
                break;

            case EINVAL:
                printf ( "strerror_r() failed: invalid error code, %d\n", 
                error_num);
                break;

            case ERANGE:
                printf ( "strerror_r() failed: buffer too small: %d\n",
                MSG_LEN);
                break;

        } 
    }
    return EXIT_SUCCESS;
}