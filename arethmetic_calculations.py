import numpy as np
from numpy.random import randn

#limit number of decimal

np.set_printoptions(precision=2)

a = np.array([1,2,3,4,5,6])
b = np.array([[10,20,30],[40,50,60]])

#creating arrays via assignment
np.random.seed(25)
c= 36*np.random.randn(6)
d = np.arange(1, 35)

#perfrom arthimetic on arrays

print(a*10)
print(a+c)