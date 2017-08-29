import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from sklearn.decomposition import PCA

def create_elipsoid(a,b,c,theta,phi):
    x=a*np.sin(theta)*np.cos(phi)
    y=b*np.sin(theta)*np.sin(phi)
    z=c*np.cos(theta)
    return x,y,z

def create_swisroll():
    for i in  [0.01*i for in range(200)]:
        if

a=1
b=1
c=1.5

circle_x=[]
circle_y=[]
hight=[]
data=[]

for theta in [0.01*i for i in range(314)]:
    for phi in [0.01*k for k in range(314*2)]:
        if random.randint(0,314)==1:
            x,y,z=create_elipsoid(a,b,c,theta,phi)
            box=[x,y,z]
            circle_x.append(x)
            circle_y.append(y)
            hight.append(z)
            data.append(box)

        #print(x,y,z)
print(len(hight))

'''
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(circle_x,circle_y,hight)
plt.show()
'''

data=np.array(data)
pca=PCA()
pca.fit(data)
pca_data=pca.fit_transform(data)

plt.scatter(pca_data[:,0],pca_data[:,1])
plt.show()
