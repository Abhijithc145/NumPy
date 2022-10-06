import numpy as np

# arr = np.array([1,2,3,4])
# print(arr)
# print(np.__version__)
# print(type(arr))

# arr = np.array((1,3,4,5))
# print(arr)

                   # Dimentions in Array

                # 0-D Array   
# arr = np.array(35)
# print(arr)
              
            #   1-D Array

# arr=np.array([1,2,3,4,5])
# print(arr)

            #    2-D Array
# arr = np.array([[1,2,3],[4,5,6],[7,8,0]])
# print(arr)
                # 3-D Array
# arr= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[7,3,1]]])
# print(arr)

                    #  Check dirction
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

               # Dimention array change to other dimention
# arr = np.array([1,2,3,4,5], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

                # Access 1 Array

# arr=np.array([1,2,3,4])
# print(arr[2])
# print(arr[2]+arr[3])
# print(arr[2]+arr[2])

                # Access 2 Array

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print(arr[1, 1])
# print(arr[0,2])

                #Numpy Array Slicing

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[4:])
# print(arr[1:5])
# print(arr[:4])
# print(arr[-3:-1])

# print(arr[0:6:2])
# print(arr[::2])

#2-D
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1:5, 1:4])
# print(arr[1, 1:4])

# NumPy data type

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr.dtype)
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)
# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)
# arr = np.array([1, 2, 3, 4, 5, 6, 7],dtype='u4')
# print(arr)



# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# newarr = arr.astype('i')
# print(newarr)
# print(newarr.dtype)

# x = arr.copy()
# print(arr)
# print(x)


# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base)
# print(y.base)
# print(x)
# print(y)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)








                   #Shape

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape)

                  #ReShape


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arr.reshape(2, 4).base)


# l =[]
# for i in range(0,5):
#     int_1 = input("Enter the number :")
#     l.append(int_1)
# print(l)
# print(type(np.array(l)))



# arr = np.twos((4,4))
# print(arr)

# arr = np.arange(3)
# print(arr)

# arr = np.eye(3,7)
# print(arr)





                          #Random function


# var = np.random.rand(4,2)    ##Only positive value is allowed
# var = np.random.randn(4,2)   ##Positive and negative value is allowed
# var2 = np.random.ranf(3)
# va1= np.random.randint(1,89,5)
# print(va1)



                             #Data Type
# var = np.array([1.4,2,3,"d",4,5])    
# var= np.array(["A","B","C",7.4])
# print(var.dtype)
# var1 = np.array([5,5,6,7,8,2],dtype='f')  #np.int8 , "f" or np.float
# print(var1)                         

# x2 = np.array([1,2,3,4,5])
# new = np.float32(x2)
# print(x2.dtype)
# print(x2)
# print(new)
# print(new.dtype)


                             #Shape
# var = np.array([[1,2,3,4],[6,7,8,9],[4,9,5,4]])
# print(var.shape)

# var2 = np.array([1,2,3,4,5,6,7,8,9],ndmin=10)
# print(var2)
# print(var2.shape)

# x=var2.reshape(3,3)
# print(x)
# print(x.ndim)


                            #Arithamatic Operations

var = np.array([1,2,3,4])
values = var / 3
values1 = var + 3
values2= var - 3
values3 = var * 3
values4 = var ** 3
print(values)
print(values1)
print(values2)
print(values3)
print(values4)

print("-------------------------------")
data1=np.array([[1,2,3],[7,8,9]])
data2 = np.array([[9,8,7],[3,2,1]])

sum = data1+data2
print(sum)
print("-------------------------------")

value = np.array([4,5,6,7])
print(np.max(value))         #min,max,argmin,sqrt,sin,cos,cumsum