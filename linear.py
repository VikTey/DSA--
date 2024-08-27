# Linear Search Algorihtm
# This is used to search the index of the particuallar value in an array

array1 = [4, 5, 2, 8, 6, 9, 0, 3]
value = 10

def linear(array,target):
    for i in range(len(array1)):
        if array1[i] == value:
            return i

index = linear(array1, value)
print(f"The number {value} is at the index {index}")

