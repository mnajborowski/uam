#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    int wynik_porownania = 1;
    char podane_haslo[12];
    char* wlasciwe_haslo = "password1";

    strcpy(podane_haslo, argv[1]);
    wynik_porownania = strcmp(podane_haslo, wlasciwe_haslo);

    char wiadomosc[32];
    gets(wiadomosc);

    if (0 == wynik_porownania) {
        printf("Haslo okej");
        printf("Wiadomosc: %s\n", wiadomosc);
    } else {
        printf("Zle haslo");
    }
    return 0;
}