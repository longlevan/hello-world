
"Creating arrays in pyhton"
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack([a,b]))
# this means stack the arrays vertically, e.g. on top of each other
#print(np.vstack([a,b]).T)
print(np.row_stack([a,b]))
print(np.vstack([a,b]))
"the opposite operation is to extract the rows or columns of a 2D array into smaller arrays"
A = np.array([[1,2,3,5],
              [6,7,8,9]])
# split into two parts
p1, p2 = np.hsplit(A, 2)

p1,p2,p3,p4 = np.hsplit(A,4)
print(p1)
print(p2)
print(p3)
print(p4)