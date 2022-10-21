#include <stdio.h>
#include <stdlib.h>

int binary_search(int *arr, int l, int r, int target);

int main(int argc, char const *argv[])
{
    int n = 0;
    int target = 0;
    int *arr;
    int result;
    scanf("%d %d", &n, &target);
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

    result = binary_search(arr, 0, n - 1, target);
    printf("%d", result);

    free(arr);
    return 0;
}

int binary_search(int *arr, int l, int r, int target)
{
    if (r >= l)
    {
        int mid = l + (r - l) / 2;
        if (arr[mid] == target)
            return mid;

        if (arr[mid] > target)
            return binary_search(arr, l, mid - 1, target);
        return binary_search(arr, mid + 1, r, target);
    }
    return -1;
}
