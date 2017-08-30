import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from sklearn.decomposition import PCA
import pandas as pd

def create_elipsoid(a,b,c,theta,phi):
    x=random.uniform(0,a)*np.sin(theta)*np.cos(phi)
    y=random.uniform(0,b)*np.sin(theta)*np.sin(phi)
    z=random.uniform(0,c)*np.cos(theta)
    return x,y,z

a=1
b=2
c=1

circle_x=[]
circle_y=[]
hight=[]
data=[]
RONDAM_NUM=100

#楕円型のデータを作成
for theta in [0.01*i for i in range(314)]:
    for phi in [0.01*k for k in range(314*2)]:
        if random.randint(0,RONDAM_NUM)==1:
            x,y,z=create_elipsoid(a,b,c,theta,phi)
            box=[x,y,z]
            circle_x.append(x)
            circle_y.append(y)
            hight.append(z)
            data.append(box)

        #print(x,y,z)
print(len(hight))
data=np.array(data)

out_csv=pd.DataFrame(data)
#out_csv.to_csv("example_elipsoid_data.csv")
np.savetxt("example_elipsoid_data.csv",data,delimiter=",")
