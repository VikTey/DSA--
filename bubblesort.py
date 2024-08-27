# BUbble sort algorithm
# This algorithm is used to sort the araay from the lowest value to the highest value

array1 = [3, 5, 2, 4, 7, 1]

for i in range(len(array1)-1):
    for k in range((len(array1)-1-i)):
        if array1[k] > array1[k+1] :
            array1[k], array1[k+1] = array1[k+1], array1[k]

print(f"The sorted array is: {array1}")