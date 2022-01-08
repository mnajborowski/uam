#include<stdio.h>
#include<string.h>

int main(int argc, char **argv) {
    FILE *fp;
    char buff[255];

    fp = fopen("file.txt", "r");
    do {
        fgets(buff, 255, (FILE *) fp);
        if (strstr(buff, argv[1]) != NULL) {
            printf("%s", buff);
        }
    } while (strstr(buff, argv[1]) == NULL);
    fclose(fp);
}