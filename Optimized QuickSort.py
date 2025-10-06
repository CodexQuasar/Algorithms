import random
import numpy as np
import math
import time

def quickSort(arr, start, end) :
    while start < end :
        if end - start > 1 :
            pivot_array = random.sample(arr[start:end+1], 3)
            pivot_value = np.median(pivot_array)
            pivot = arr.index(pivot_value, start, end + 1)
        else : 
            pivot = end
        pivot = partition(arr, start, end, pivot) 
        if pivot - start < end- pivot :
            quickSort(arr, start, pivot-1)
            start = pivot + 1
        else :
            quickSort(arr, pivot+1, end)
            end = pivot - 1

def partition(arr, start, end, pivot) :
    pivot = int(pivot)
    pivot_value = arr[pivot]
    swap(arr, pivot, end)
    i = start-1
    for j in range(start, end) :
        if arr[j] < pivot_value :
            i += 1
            swap(arr, i, j)      
    swap(arr, i+1, end)          
    return i+1

def swap(arr, i, j) :
    arr[i], arr[j] = arr[j], arr[i]


def insertionSort(A) :
    N = len(A)
    for i in range(1,N):
     j = i
     while (j > 0 and A[j] < A[j - 1]) :
        swap(A, j, j-1)
        j -= 1

   


print("The time complexity of quickSort is 63nlog(n), while that insertion sort is n*(n-1)/2")
time_diff = 1
i = 2
while True :
    time_diff = 63*i*(math.log(i,2)) - (i*(i-1) / 2)
    if time_diff < 0 :
        break
    i += 1
print(f"The set size for which insertion sort is faster than the quicksort: {i-1}")    
    

Array = [random.randint(0,10000) for _ in range(1000)]
print(f"Original array : {Array}")
start = time.time()
quickSort(Array, 0, len(Array) - 1)
end = time.time()
print(f"Sorted array : {Array}")
print(f"Time taken for quickSort: {end-start}")

