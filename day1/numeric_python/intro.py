import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[2] + arr[3])
#print(arr)
#print(type(arr))

# Use <tuple to create a NumPy array
arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#print(arr1)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr2[0:2, 1:4])
#print(arr)
#print('number of dimensions :', arr2.ndim)