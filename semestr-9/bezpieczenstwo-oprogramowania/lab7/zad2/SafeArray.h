#include <stdexcept>

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