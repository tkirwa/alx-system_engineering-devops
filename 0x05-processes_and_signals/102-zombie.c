#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop
 * Return: 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Entry point
 * Return: Always 0 (Success)
 */
int main(void)
{
    int i;
    pid_t child_pid;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();
        if (child_pid == 0)
            exit(0);
        else if (child_pid > 0)
            printf("Zombie process created, PID: %d\n", child_pid);
        else
            perror("fork");
    }

    infinite_while();

    return (0);
}
