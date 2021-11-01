#include <stdio.h>
#include <signal.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define NORMAL 0
#define ADMIN 1

typedef struct user {
    char name[0x20];
    int type;
} user;

// not relevant to challenge
void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

user me = { .type = NORMAL };

void whoami() {
    puts(me.name);
}

void echo(char* arg) {
    puts(arg);
}

// not for u peasants, only for me, the ADMIN
void execute(char* arg) {
    system(arg);
}

int main() {
    int opt;
    char arg[0x20];

    setup();

    puts("---- User Checker System v0.05-alpha-001 ----");
    puts("|   feeling cute, might have vulns inside   |");
    puts("---------------------------------------------");

    puts("Enter your name:");
    gets(me.name);

    while (1) {
        puts("1. echo");
        puts("2. whoami");
        puts("3. execute");
        printf("> ");
        scanf("%d", &opt);
        getc(stdin); // to eat the newline character
        switch (opt) {
            case 1:
                printf("arg > ");
                gets(arg);
                echo(arg);
                break;
            case 2:
                whoami();
                break;
            case 3:
                if (me.type != ADMIN) {
                    printf("%s is not in the sudoers file. This incident will be reported\n", me.name);
                    continue;
                }
                printf("arg > ");
                gets(arg);
                execute(arg);
                break;
        }
    }
}