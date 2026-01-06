from numpy import *

"""
from array import *

# This code demonstrates the usage of Python's array module to create and manipulate arrays of integers.
# Create an array of integers
arr = array('i', [10, 20, 30, 40, 50])

# Print the original array
print("Original array:", arr)

for i in range(0, 5):
    print(arr[i],  end=" ")
print('\n')

for i in arr:
    print(i, end=" ")

print('\n')
print(f"typecode: {arr.typecode}")  # Output: 'i' (typecode for signed integer)

arr.insert(1, 15)  # Insert 15 at index 1
arr.append(60)    # Append 60 at the end
arr[5] = 25      # Update/replace index 2 to 25 
arr.pop(3)        # Remove element at index 3
arr.pop()         # Remove last element
arr.remove(40)   # Remove the value 40

for i in arr:
    print(i, end=" ")
print('\n')

copyarr = array(arr.typecode, (x for x in arr))  # Copying array
print("Copied array:")
for i in copyarr:
    print(i, end=" ",)

#slicing
newarray = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

sliced_array1 = newarray[2:7]  # Slicing from index 2 to 6
sliced_array2 = newarray[3:-3] # from index 3 to third last element. -3 mane last er 3 ta bad diye
sliced_array3 = newarray[::-1]   # array reverse kore dey 

print('\n')
empt = array('i', [])
n = int(input("Enter number of elements: "))
for i in range(0, n):
    empt.append(int(input("Enter values: ")))

for i in empt:
    print(i, end=" ")"""

# val = array([1, 2, 3, 4.7, 'a'])

# for i in val:
#     print(i, end=" ")

# val = arange(1, 10, 2)  # 1 theke 10 er moddhe 2 step size e print kore
# val = zeros(5)  # 5 ta zero print kore
# val = ones(5)   # 5 ta one print kore
# val = linspace(10, 20, 5)  # 10 theke 20 er moddhe 5 ta equally spaced number print kore
# for i in val:
#     print(i, end=" ")

zero = array(10)  # zero dimensional array
print(zero)

one = array([1, 2, 3, 4, 5])  # one dimensional array
print(one)

two = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # two dimensional array
print(two)

three = array([ [ [1,2], [3,4] ], [ [5,6], [7,8] ] ]) # three dimensional array
print(three)