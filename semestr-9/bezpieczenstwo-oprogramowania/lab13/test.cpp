#include <mutex>
#include <thread>
#include <atomic>
#include <chrono>
#include <iostream>
#include <random>

bool canDine = false;

struct Fork
{
    std::mutex mutex;
};

struct Philosopher
{
private: 
    int index;
    Fork& leftFork;
    Fork& rightFork;
    std::thread thread;
public:
    Philosopher(int& index, Fork& leftFork, Fork& rightFork, std::thread(&Philosopher::dine, this));
    ~Philosopher()
    {
        thread.join();
    }

    void eat()
    {
        std::lock(leftFork.mutex, rightFork.mutex);

        std::lock_guard<std::mutex> left_lock(leftFork.mutex,   std::adopt_lock);
        std::lock_guard<std::mutex> right_lock(rightFork.mutex, std::adopt_lock);

        std::cout << index << " started eating." << std::endl;

        std::chrono::milliseconds timeout(1500);
        std::this_thread::sleep_for(timeout);

        std::cout << index << " finished eating." << std::endl;
    }

    void think()
    {
        static thread_local std::uniform_int_distribution<> wait(1, 6);
        std::this_thread::sleep_for(std::chrono::milliseconds(wait(rng) * 150));

        std::cout << " is thinking." << std::endl;
    }

    void dine()
    {
        while (!canDine);

        do
        {
            think();
            eat();
        } while(canDine);
    }
};

int main()
{
    Fork forks[numberOfPhilosophers];
    Philosopher philosophers[numberOfPhilosophers];
    for (i = 0; i < numberOfPhilosophers; i++)
    {
        philosophers[i] = Philosopher(i, forks[i % numberOfPhilisophers], forks[(i + 1) % numberOfPhilosophers])
    }

    canDine = true;
    std::this_thread::sleep_for(std::chrono::seconds(5));
    canDine = false;
    
    return 0;
}