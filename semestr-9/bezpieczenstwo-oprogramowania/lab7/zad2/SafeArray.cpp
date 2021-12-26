#include "SafeArray.h"

SafeArray::SafeArray(int size)
{
    SafeArray::size = size;
    array = new int[size];
}

SafeArray::~SafeArray()
{
    delete[] array;
}

void SafeArray::set(int index, int element)
{
    if (index < 0 || index >= size)
    {
        throw std::invalid_argument("Index out of range.");
    }
    array[index] = element;
}

int SafeArray::get(int index)
{
    if (index < 0 || index >= size)
    {
        throw std::invalid_argument("Index out of range.");
    }
    return array[index];
}
