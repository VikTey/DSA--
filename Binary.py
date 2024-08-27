# Binary Search Algorithm
# This is also used to search the index of a particular value in an array
# But this reuires a sorted array and works faster

array = [0, 1, 2, 4, 6, 7, 8, 9, 10, 11]
value = 10
def binary(array, value):
    l = 0
    r = len(array)-1
    while l <=r:
        center = (l+r)//2
        if array[center] == value:
            return center
        elif array[center] > value:
            r = center - 1
        else:
            l = center + 1
    return 0
ind = binary(array, value)

print(f"The value {value} is at the index {ind}")