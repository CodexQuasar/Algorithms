import random
import time
import matplotlib.pyplot as plt


def BinarySearch(A, start,  end, val) : 
    if val < A[start] : return -1
    while start <= end :
        mid = (start+end) // 2
        if A[mid] > val : end = mid - 1
        elif A[mid] < val : start = mid + 1
        else : return mid
    return end

def swap(A, i, j) :
    A[i], A[j] = A[j], A[i]

def insertionSort(A) :
    length = len(A)
    i=0
    for i in range(1, length-1, 2) :
        if i<length-1 and A[i] < A[i+1] : swap(A, i, i+1)

        pos = BinarySearch(A, 0, i-1, A[i])
        if pos == -1 :
            for j in range(i, 0, -1) :
                swap(A, j, j-1)
                swap(A, j+1, j)
            swap(A, 0, 1)   

        else :
            for j in range(i, pos+1, -1) :
                if pos + 1 >= i : break
                swap(A, j, j-1)
                swap(A, j+1, j)
            pos2 = BinarySearch(A, 0, pos, A[pos+2]) 
            if pos2 == -1 :
              for j in range(pos+2, 0, -1) :
                 swap(A, j, j-1)  
            else:
                for j in range(pos+2, pos2+1, -1) :
                 swap(A, j, j-1)
                  
    i+=2
    if i == length-1 and i%2 == 1:
        pos = BinarySearch(A, 0, i-1, A[i])
        if pos == -1 :
            for j in range(i, 0, -1) :
                  swap(A, j, j-1)
        else:          
         for j in range(i, pos+1, -1) :
              swap(A, j, j-1)

input_size = []            
time_taken = []

for m in range(1, 18) : # Set range for test cases here
    A = [random.randint(0,10**m) for _ in range(2**m)]
    input_size.append(m)
    print(A)
    print()
    start_time = time.time()
    insertionSort(A)
    end_time = time.time()
    print(A)
    print()
    print("The time required for execution is: ", end_time-start_time)
    print()
    time_taken.append(end_time-start_time)

plt.plot(input_size, time_taken, marker='o')
plt.title("Binary Insertion Sort - Execution Time vs Input Size")
plt.xlabel("Input Size (2^m)")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.show()