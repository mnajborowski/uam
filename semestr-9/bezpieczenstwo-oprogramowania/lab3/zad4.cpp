#include <sys/mman.h>
#include <iostream>
#include <cstdlib>

int main() {
    int* preKey = new int[16];
    for (int i = 0; i < 16; i++) {
        preKey[i] = rand() % 2;
    }
    mlockall(MCL_CURRENT);
    munlockall();
    delete[] preKey;
    return 0;
}