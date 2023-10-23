#include <stdio.h>
#include <string.h>

int check_pw(char *input_pw, char *reference_pw, char *offsets) {
    int i;
    for (i = 0; i < strlen(reference_pw); i++) {
        if (input_pw[i] != reference_pw[i] + offsets[i]) {
            return 0; // False
        }
    }
    return 1; // True
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        puts("You should give one argument.");
        return -1;
    }

    char reference_pw[] = "WoRSNFwnBhtUJ3rB";
    char offsets[] = {2, 3, 2, 3, 5, 0}; // Note: This is just an example of possible offsets

    if (strlen(argv[1]) == 18 && check_pw(argv[1], reference_pw, offsets)) {
        printf("Yes, %s is correct!\n", argv[1]);
        return 0;
    }

    printf("No, %s is not correct.\n", argv[1]);
    return 1;
}
