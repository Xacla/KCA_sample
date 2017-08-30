import matplotlib.pyplot as plt
import numpy as np
import random as rdn
from mpl_toolkits.mplot3d import Axes3D

p=[i/100 for i in range (-300,0,1)]
#print(p)

depth=5
d_box=[i for i in range(-3,4,1)]

x_set=[]
y_set=[]
depth_set=[]
out_csv=[]

for i in range(len(p)):
    now_x=p[i]*np.sin(2*np.pi*p[i])
    now_y=p[i]*np.cos(2*np.pi*p[i])
    x_set.append(now_x)
    y_set.append(now_y)
    moi=rdn.uniform(-3,3)
    a=[now_x,moi,now_y]
    depth_set.append(moi)
    out_csv.append(a)

data=np.array(out_csv)
print(data)
plt.scatter(x_set,y_set)
plt.show()
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x_set,depth_set,y_set,c='g')
plt.show()

np.savetxt("example_swithroll_data.csv",data,delimiter=",")
