#include <thread>
#include <chrono>
#include <iostream>
#include <time.h>

long count = 0;

void func1()
{
    for (int i = 0; i < 10000000; i++)
        count++;
}

void func2()
{
    for (int i = 0; i < 10000000; i++)
        count++;
}

void func3()
{
    for (int i = 0; i < 10000000; i++)
        count++;
}

int main()
{
    std::thread(func1).join();
    std::thread(func2).join();
    std::thread(func3).join();

    std::this_thread::sleep_for(std::chrono::milliseconds(2000));

    std::cout << count << std::endl;

    return 0;
}
