# First we import numpy
import numpy as np 

# Create an numpy array using np.array()
# Values can be accessed like this a[1], a[2]
numbers = np.array([ 100, 1, 2, 3, 4 ])

# Accessing all the value stored
for number in numbers:
    print(number)

# Type of numbers: numpy.ndarray
print(type(numbers))

# data type of np array case of int: int64
print(numbers.dtype)

# Prints size of numbers
print(numbers.size)

# Prints dimention of numbers
print(numbers.ndim)

# shape is a turple integers indicating the number of elements in each dimention
print(numbers.shape)

# Slice takes two value, from which index to start, which index to end. In this case,
# It will copy values from index 1 to index 3. 
d = numbers[1:4]

#This changed the value of those entity.
numbers[3:5] = 300, 400

# Basic Operations

# Vector Addition In case we don't use numpy
u = [1, 0]
v = [0, 1]
z = []

for n,m in zip(u,v):
    z.append(u+v)
print(z)
# output : [[1, 0, 0, 1], [1, 0, 0, 1]]

#Np
p = np.array([1, 1])
q = np.array([2, 1])

z = p-q
print(z)
# Output [ 1 -1], Can do addition

# Cross Multiplication
z = 2* p
print(z)
z = p * q 
print (z)

# Dot Multiplication
d = np.dot(u,v)
print("dp")
print(d)

# Broadcasting: If you add 1 with a vector, like z, it will add 1 in every value of z
z = p+1
print(z)

# Universal Functions

# Calculating mean(avgerage)
ar = np.array([2, 2, 2, 2])
mean = ar.mean()
print(mean)
# Maximum Value
max = ar.max()

# np.pi access the value of pi
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print(y)

# Creating an interval
np.linespace(-2, 2, num=5)
# Output [-2, -1, 0, 1, 2]