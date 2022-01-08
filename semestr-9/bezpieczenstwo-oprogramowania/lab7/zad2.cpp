#include <iostream>
#include "SafeArray.h"

int main()
{

    SafeArray* array = new SafeArray(10);
    array->set(5, 5);
    array->get(5);
    array->get(4);g
    array->get(10);
    return 0;
}