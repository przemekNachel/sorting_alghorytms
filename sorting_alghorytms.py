import random

numbers = []
for i in range(100):
    numbers.append(random.randint(0, 100))


def bubble_sort(numbers):
    for j in range(len(numbers)):
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i+1], numbers[i] = numbers[i], numbers[i+1]
    return numbers


def insert_sort(A):
    for i in range(1, len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    return A


def qsort(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    i, j = l, r
    pivot = arr[int((l + r) / 2)]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if l < j:
        qsort(arr, l, j)
    if r > i:
        qsort(arr, i, r)
    return arr


print(qsort(numbers))
