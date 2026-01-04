from array import *

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
val = array('i', [])
n = int(input("Enter number of elements: "))
for i in range(0, n):
    val.append(int(input("Enter values: ")))

for i in val:
    print(i, end=" ")