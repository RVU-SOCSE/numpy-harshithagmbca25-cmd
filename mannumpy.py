Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> a=np.array([1,2,3,4,5])
>>> print(a)
[1 2 3 4 5]
>>> print(a.shape)
(5,)
>>> print(a.ndim)
1
>>> print(a.size)
5
>>> print(a.dtype)
int64
>>> b=([[1,2,3,4],[5,6,7,8]])
>>> b=np.array([[1,2,3,4],[5,6,7,8]])
>>> print(b)
[[1 2 3 4]
 [5 6 7 8]]
>>> b.shape
(2, 4)
>>> b.ndim
2
>>> b.size
8
>>> b.dtype
dtype('int64')
>>> ####Indexing of 1D Array
>>> a[2]
np.int64(3)
>>> a[-1]
np.int64(5)
>>> ####Indexing of 2D Array
>>> b[2,2]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b[2,2]
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> b[1,2]
np.int64(7)
>>> b[-1,-1]
np.int64(8)
>>> #####Slicing 1D Array
... a[1:4]
array([2, 3, 4])
>>> a[:3]
array([1, 2, 3])
a[2:-1]
array([3, 4])
array([3, 4])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    array([3, 4])
NameError: name 'array' is not defined. Did you forget to import 'array'?
####Slicing of 2D Array
b[1,:]
array([5, 6, 7, 8])
b[0:2,0:1]
array([[1],
       [5]])
####Reshaping an Array
KeyboardInterrupt
import numpy as np
x=np.array([1,2,3,4,5,6])
x.reshape(2,3)
array([[1, 2, 3],
       [4, 5, 6]])
x.reshape(2,1,3)
array([[[1, 2, 3]],

       [[4, 5, 6]]])
####Element Wise operations
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
x+y
array([ 6,  8, 10, 12])
x-y
array([-4, -4, -4, -4])
x*u
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x*u
NameError: name 'u' is not defined
x*y
array([ 5, 12, 21, 32])
x/y
array([0.2       , 0.33333333, 0.42857143, 0.5       ])
x//y
array([0, 0, 0, 0])
x**2
array([ 1,  4,  9, 16])
y**2
array([25, 36, 49, 64])
np.sqrt(x)
array([1.        , 1.41421356, 1.73205081, 2.        ])
x+10
array([11, 12, 13, 14])
x-2
array([-1,  0,  1,  2])
x*2
array([2, 4, 6, 8])
 ### Transpose
x.T
array([1, 2, 3, 4])
 b==np.array([[1,2,3,4],[5,6,7,8]])
 
SyntaxError: unexpected indent
    b==np.array([[1,2,3,4],[5,6,7,8]])
    
SyntaxError: unexpected indent
 b==np.array([[1,2,3,4],[5,6,7,8]])
 
SyntaxError: unexpected indent
      b==np.array([[1,2,3,4],[5,6,7,8]])
      
SyntaxError: unexpected indent
SyntaxError: unexpected indent
SyntaxError: invalid syntax
 ### Transpose
x.T
array([1, 2, 3, 4])
    b==np.array([[1,2,3,4],[5,6,7,8]])
    
SyntaxError: unexpected indent
b=np.array([[1,2,3,4],[5,6,7,8]])
x.T
array([1, 2, 3, 4])
b==np.array([[1,2,3,4],[5,6,7,8]])
array([[ True,  True,  True,  True],
       [ True,  True,  True,  True]])
b=np.array([[1,2,3,4],[5,6,7,8]])
b.T
array([[1, 5],
       [2, 6],
       [3, 7],
       [4, 8]])
