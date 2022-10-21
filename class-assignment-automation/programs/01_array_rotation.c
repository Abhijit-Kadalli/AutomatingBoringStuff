#include <stdio.h>
#include <stdlib.h>

void rotate(int *arr, int n, int d);
void printArray(int *arr, int size);

int main(int argc, char const *argv[])
{
    int n = 0;
    int shift = 0;
    int *arr;
    scanf("%d %d", &n, &shift);
    arr = (int *)malloc(n * sizeof(int));

    if (arr == NULL)
    {
        printf("ERROR: MEMORY ALLOCATION FAIL\n");
        return 1; // memory allocation fails - return from here
    }

    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &arr[i]);
    }

    rotate(arr, n, shift);
    printArray(arr, n);

    free(arr);
    return 0;
}

void rotate(int *arr, int n, int d)
{
    int p = 1;
    while (p <= d)
    {
        int last = arr[0];
        for (int i = 0; i < n - 1; i++)
        {
            arr[i] = arr[i + 1];
        }
        arr[n - 1] = last;
        p++;
    }
}

void printArray(int *arr, int size)
{
    int i;
    printf("[");
    for (i = 0; i < size - 1; i++)
    {
        printf(" %d,", arr[i]);
    }
    printf(" %d]\n", arr[i]);
}
