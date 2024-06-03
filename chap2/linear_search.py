import numpy as np

def linear_search(A, x):
    """
    Linear search for x in array A from beginning to end
    Arguments:
        A: array
        x: the object to be found
    """
    n = len(A)
    for i in range(n):
        key = A[i]
        if A[i] == x:
            return i
        else:
            pass
    return "NIL"

def main():
    A = [1, 2, 5, 6, 8]
    x = 7
    y = 5

    print (linear_search(A, x))
    print (linear_search(A, y))
    return

if __name__ == "__main__":
    main()