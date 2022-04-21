#!/usr/bin/python3
"""Find a peak in array."""


def findPeakUtil(arr, low, high, n):
    """Find peak using divide and conquer."""
    # Find index of middle element
    mid = low + (high - low)//2

    # Compare middle element with its
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid

    # If middle element is not peak and
    # its left neighbour is greater
    # than it, then left half must
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)

# If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must
    # have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)


# A wrapper over recursive
# function findPeakUtil()
def find_peak(list_of_integers):
    """Wrap the recursive function."""
    n = len(list_of_integers)
    if n == 0:
        return None
    return list_of_integers[findPeakUtil(list_of_integers, 0, n - 1, n)]
