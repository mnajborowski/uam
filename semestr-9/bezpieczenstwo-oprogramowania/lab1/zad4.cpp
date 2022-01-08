#include <iostream>

int main() {
    std::cout << "Size of char: " << sizeof(char) << std::endl;
    std::cout << "Size of short: " << sizeof(short) << std::endl;
    std::cout << "Size of int: " << sizeof(int) << std::endl;
    std::cout << "Size of long: " << sizeof(long) << std::endl;
    std::cout << "Size of long long: " << sizeof(long long) << std::endl;
    std::cout << "Size of float: " << sizeof(float) << std::endl;
    std::cout << "Size of double: " << sizeof(double) << std::endl;

    long abc[5];
    short def[10];

    for (int i = 0; i < 30; i++) abc[i] = i;
    abc[0]++;
    for (int i = 0; i < 10; i++) {
        std::cout << def[i] << std::endl;
    }
    std::cout << sizeof(long) << sizeof(int) << sizeof(long long) << std::endl;
}