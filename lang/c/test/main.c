/* main,c */
#include <stdio.h>
#include "sum.h"

int main(void) {
    int value;
    value = sum(50, 100);
    printf("%d\n", value);
    return 0;
}
