#include <iostream>

int main() {
    int *array = (int*) malloc(10 * sizeof(int));
    array = (int*) malloc(20 * sizeof(int));
    
    return 0;
}