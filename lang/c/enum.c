#include <stdio.h>
enum week{
    mon,
    tue,
    wed,
    thu,
    fri,
    sat,
    sun
};
int main(int argc, char **argv) {
    enum week wk0, wk1, wk2, wk3, wk4, wk5, wk6;
    wk0=mon;
    wk1=tue;
    wk2=wed;
    wk3=thu;
    wk4=fri;
    wk5=sat;
    wk6=sun;
    printf("mon: %d\n", wk0);
    printf("tre: %d\n", wk1);
    printf("wed: %d\n", wk2);
    printf("thu: %d\n", wk3);
    printf("fri: %d\n", wk4);
    printf("sat: %d\n", wk5);
    printf("sun: %d\n", wk6);
    return 0;
}