#include <iostream>
#include <fstream>


int main(int argc, char **argv) {
    std::string line;
    std::ifstream file("file.txt");
    while (std::getline(file, line)) {
        if (line.find(argv[1]) != std::string::npos) {
            std::cout << line << std::endl;
        }
    }
    return 0;
}