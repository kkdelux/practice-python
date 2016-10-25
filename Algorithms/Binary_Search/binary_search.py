# Simple implementation of binary search which takes a sorted array and a key
# as its input and returns the element's index if found and None if not
def binary_search(key, arr, min_idx, max_idx):
    if min_idx == max_idx and arr[min_idx] != key:
        return None
    else:
        mid_idx = (min_idx + max_idx) / 2
        
        if arr[mid_idx] > key:
            return binary_search(key, arr, min_idx, mid_idx-1)
        elif arr[mid_idx] < key:
            return binary_search(key, arr, mid_idx + 1, max_idx)
        else:
            return mid_idx
    
l = [1,2,3,4,5,6,7,8,9,10]
print binary_search(6, l, 0, len(l)-1)
a = ['a','b','c','d','e','f','g','h','i','j']
print binary_search('e', a, 0, len(a)-1)