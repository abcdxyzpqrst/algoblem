import random
import numpy as np

def insertion_sort(A, option="increasing"):
    """
    At the current position i, the subarray A[1:i-1] are already sorted
    Hence, we just put the current key A[i] into the right position in A[1:i-1]

    Arguments:
        A: list to be sorted
        option: increasing/decreasing
    """
    n = len(A)
    if option == "increasing":
        for i in range(1, n):
            key = A[i]
            j = i-1
            while j >= 0 and A[j] > key:
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
    elif option == "decreasing":
        for i in range(1, n):
            key = A[i]
            j = i-1
            while j >= 0 and A[j] < key:
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
    else:
        raise ValueError("Not possible")
    return A

def main():
    """
    test scripts
    """
    n = 500
    A = np.arange(n)
    perm = np.random.permutation(n)
    A = A[perm]
    print (A)
    print (insertion_sort(A))
    print (insertion_sort(A, "decreasing"))
    return

if __name__ == "__main__":
    main()