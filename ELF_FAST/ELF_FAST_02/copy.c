#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char *pcVar4;
    long lVar3;
    char cVar1;
    char *pcVar5;
    char firstLetterOfPassword = 'k';

    if (argc == 2) {
        pcVar4 = argv[1];
        lVar3 = strlen(pcVar4);
        if (lVar3 == 20) { // 0x16 est 22 en décimal
            if (*pcVar4 != '\0') {
                if (*pcVar4 != firstLetterOfPassword) {
LAB_001011ed:
                    printf("No, %s is not correct.\n", pcVar4);
                    return 1;
                }
                pcVar5 = "8gZprxXQDzuNizYiek";
                cVar1 = 'h';
                do {
                    pcVar4++;
                    if (*pcVar4 == '\0') break;
                    printf("pcVar4 = pass = %c\n", *pcVar4);
                    if (cVar1 - 1 != *pcVar4) {
                        printf("Error on cVar1 - 1 != *pcVar4 / %c - 1 != %c\n", cVar1, *pcVar4);
                        goto LAB_001011ed;
                    }
                    cVar1 = *pcVar5;
                    pcVar5++;
                } while (cVar1 != '\0');
            }
            printf("Yes, %s is correct!\n", pcVar4);
            return 0;
        }
        else {
            printf("No, %s is not correct.\n", pcVar4);
            return 0;
        }
    }
    else {
        puts("You should give one argument.");
        return -1; // 0xffffffff est -1 en int
    }
}
