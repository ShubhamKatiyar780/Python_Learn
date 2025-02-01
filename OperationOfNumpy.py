import numpy as np

# Create a arrey by using array() function
a = np.array([10, 20, 30])
print(type(a))
print(a[2])
print(a.shape)
print(f"Total no. of elements: {a.size}")
print(f"Dimension :{a.ndim}D")
print(a)

# Create a new arrey by using asrray() function
b = np.asarray(a)  # replace the value at index
a[1] = 15
print(b) # b = a both are equal

# Create a new arrey by using arange() function
c = np.arange(1,10,2)
print(c)

# d = np.array([1, 2, 3])
# print(d)

e = np.array([[1,2], [3, 4], [5, 6]])
f = np.array([10, 20])
# print(e+f)
# print(f+e)

e = np.array([[1,2], [3, 4], [5, 6]])
f = np.array([10, 20, 30])
# print(e+f)
# print(f+e)

g = np.ones((3, 3), dtype=int)
print(g)