#include <stdio.h>
int main(int argc, char *argv[]) {
    int i;
    printf("引数の総数=%d\n", argc);
    for (i=0; i<argc; i++) {
        printf("%d番目の引数=%s\n", i, argv[i]);
    }
    return 0;
}