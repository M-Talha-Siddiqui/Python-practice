import numpy as np
a = np.array([[1,2,3], [4,5,6]])
print(a)
print(a.ndim) # show the dimension of array
print("shape: " ,a.shape)
print("size: " ,a.size)
print("itemsize " ,a.itemsize)

b = a.reshape(3,2)
print(b)
print(b.shape)

# slicing print the item you want 
print("slicing")
print(a[0,2]) # printing (index 2) 1st row and 3rs column
print(a[0:,2]) # printing all the row but only 3rd column
print(a.min())
print(a.max())
print(a.sum())

c = np.linspace(1,3,5) # 5value btw 1 and 3 
print(c)
print("sum of row or column")

#sum of all the row or column
print(a.sum(axis = 0)) #for columns since axis =0 is for column
print(a.sum(axis = 1)) # for row since axis =0 is for row
print("sqr root of each elemnet : " ,np.sqrt(a))
print("std deviation",a.std())

# algebric manupulatiin
print()
print("Algebra")
d = np.array([[5,3,6],[9,7,1]])

print("array addition :", a+d)
print("array scalar multiplication :", a*d)
print("array division :", a/d)
print("vertical and horizontal stacking")
print(np.vstack((a,d)))
print("horizontal stacking")
print(np.hstack((a,d)))
print()
# Exponetial and log values
print("exponential and log values ")
print("exponential: \n", np.exp(a))
print("log", np.log(a))
print(" log10", np.log10(a))
