import pytest


def reverseArray(arr, d):
    c =(arr[d:]) + (arr[:d])
    #c =(arr[d:])
    #print(c)
    return c


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    print(reverseArray(arr,d))
