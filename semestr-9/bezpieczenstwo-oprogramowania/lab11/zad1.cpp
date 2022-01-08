#include <iostream>

int main() {
    int *mallocArray = (int*) malloc(10 * sizeof(int));
    mallocArray = (int*) realloc(mallocArray, 20 * sizeof(int));
    int *newArray = new int[20];
    int *newOperatorArray = (int*) ::operator new (sizeof(int) * 20);

    free(mallocArray);
    delete[] newArray;
    delete newOperatorArray;
    
    return 0;
}