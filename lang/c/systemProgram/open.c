////////////////////////////////////////////////////////
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
// int open (const char *name, int flags);
// int open (const char *name, int flags, mode_t mode);
////////////////////////////////////////////////////////
#include <stdlib.h>

int main( void ) {
    int fd;

    /* open a file for output              */
    /* replace existing file if it exists  */
    /* with read/write perms for owner     */

    fd = open( "myfile.dat",
        O_WRONLY | O_CREAT | O_TRUNC,
        S_IRUSR | S_IWUSR );

    /* read a file that is assumed to exit  */    

    fd = open( "myfile.dat", O_RDONLY );

    /* append to the end of an existing file  */
    /* write a new file if file doesn't exist */
    /* with full read/write permissions       */

    fd = open( "myfile.dat",
        O_WRONLY | O_CREAT | O_APPEND,
        S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP
        | S_IROTH | S_IWOTH );
    return EXIT_SUCCESS;
}
