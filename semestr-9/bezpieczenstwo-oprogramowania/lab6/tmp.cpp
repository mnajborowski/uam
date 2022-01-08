#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <filesystem>
namespace fs = std::filesystem;

int main()
{
    std::cout << "TMP_MAX = " << TMP_MAX << '\n'
              << "FOPEN_MAX = " << FOPEN_MAX << '\n';
    std::FILE *tmpf = std::tmpfile();
    std::fputs("Hello, world", tmpf);
    std::rewind(tmpf);
    char buf[6];
    std::fgets(buf, sizeof buf, tmpf);
    std::cout << buf << '\n';
    std::fclose(tmpf);
}