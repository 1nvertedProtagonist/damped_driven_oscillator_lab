'''

a1=(1,2)

print(type(a1))




b = np.asarray(a1)

print(b)

print(type(b))

c = np.asarray(a1[:]) 

print(c)
print(type(c))


d = np.asarray([1,2,3,4,5])

print(d)'''

import numpy as np 
from scipy.signal import find_peaks


#x = np.asarray([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
#y = np.asarray([3,5,3,6,7,8,9,5,4,7,6,8,10,1])
#xandy  =np.asarray([x,y])
#xandyt = np.transpose(xandy)
#print(xandyt.shape)
#print(xandy.shape)

#print(np.diff(x))

#a=find_peaks(y,height=5)
#print(type(a))
#print((len(a)))
#print(type(a[:]))
#print(type(a[0]))
#print(type(a[1]))
#print(a[0][0]) 

## this shit literally returns an array of indexes corresponding to the 
## positions

#print(a[1]["peak_heights"])
#print(type(a[1]["peak_heights"]))
#print()


x = [1,2,3,4,5]
#x = np.asarray(x)
#print(x[1:])
#print(type(x))

print(type(find_peaks(x)[0]))