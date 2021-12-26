#include <iostream>
#include "SafeArray.h"

int main() {
    auto* array = new SafeArray(10);
    array->set(5, 5);
    std::cout << "array->get(5): " << array->get(5) << std::endl;
    std::cout << "array->get(4): " << array->get(4) << std::endl;
    std::cout << "array->get(10): " << array->get(10) << std::endl;
    return 0;
}
