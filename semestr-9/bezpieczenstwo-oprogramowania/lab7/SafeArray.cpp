#include "SafeArray.h"

class SafeArray
{
private:
    int* array;
    int size;
public:
    SafeArray(int size);
    ~SafeArray();
    void set(int index, int element);
    int get(int index);
};

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
