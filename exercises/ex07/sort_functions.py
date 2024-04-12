"""Functions that implement sorting algorithms."""

__author__ = "730431261"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    idx: int = 1
    ## tracks indices in list
    while idx < len(x): 
        ## outer loop
        idx1: int = x[idx]
        ## tracks unsorted indices
        loc = idx
        while loc > 0 and x[loc - 1] > idx1: 
            ## inner loop
            x[loc] = x[loc -1]
            loc -= 1 
            ## idx1 now is (idx1 - 1)
            x[loc] = idx1
        idx += 1 
        ## iterate back through list
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx: int = 0 
    ## track sorted indicies
    while idx < len(x) - 1: 
        ## outer loop
        min_idx: int = idx 
        ## idx can't be lower than number of indices
        idx1: int = idx + 1 
        ## track unsorted indices in list
        while idx1 < len(x): 
            ## inner loop
            if x[idx1] < x[min_idx]: 
                ## if x at idx1 is less than x at min_idx
                min_idx = idx1 
                ## now idx1 becomes the lowest index (min_idx)
            idx1 += 1 
            ## itierate through list
        x[idx], x[min_idx] = x[min_idx], x[idx]
        idx += 1
    return None
    