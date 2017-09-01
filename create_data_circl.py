import numpy as np
import matplotlib.pyplot as plt

def circle_create(a,b):
    x=a*np.cos(2*np.pi*b)
    y=a*np.sin(2*np.pi*b)
    return x,y

setup=[0.01*i for i in range(0,100,1)]
out_put=[]
for i in setup:
    x,y=circle_create(1.0,i)
    box=[x,y]
    out_put.append(box)
for i in setup:
    x,y=circle_create(3.0,i)
    box=[x,y]
    out_put.append(box)

out_put=np.array(out_put)
plt.scatter(out_put[:,0],out_put[:,1])
plt.show()
np.savetxt("example_2circles.csv",out_put,delimiter=",")
