import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from sklearn.decomposition import PCA
import pandas as pd

def create_elipsoid(a,b,c,theta,phi):
    x=a*np.sin(theta)*np.cos(phi)
    y=b*np.sin(theta)*np.sin(phi)
    z=c*np.cos(theta)
    return x,y,z
def kernel_gause(x_i,x_j):
    x_norm=np.linalg.norm(x_j-x_i)
    return np.exp(x_norm)

a=1
b=2
c=1

circle_x=[]
circle_y=[]
hight=[]
data=[]
RONDAM_NUM=1500

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

out_csv=pd.DataFrame(data)
out_csv.to_csv("example_elipsoid_data.csv")

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(circle_x,circle_y,hight)
plt.show()

#PCAの場合
data=np.array(data)
pca=PCA()
pca.fit(data)
pca_data=pca.fit_transform(data)
plt.scatter(pca_data[:,0],pca_data[:,1])
plt.show()


#カ-ネル行列の生成
kernel_matrix=[]
ones_matrix=[]
data=np.array(data)
for i in range(data.shape[0]):
    a=[]
    ones_row=[]
    for j in range(data.shape[0]):
        result_gause=kernel_gause(data[i,:],data[j,:])
        a.append(result_gause)
        ones_row.append(1)
    kernel_matrix.append(a)
    ones_matrix.append(ones_row)

kernel_matrix=np.array(kernel_matrix)
ones_matrix=np.array(ones_matrix)
n_reverse=1/kernel_matrix.shape[0]
ones_matrix=n_reverse*ones_matrix
print(kernel_matrix.shape)
print(ones_matrix[0,0])

i_n=np.identity(kernel_matrix.shape[0])
j_n=i_n - ones_matrix

#KCAにおける固有値計算
value_solve=np.dot(j_n,kernel_matrix)
lamda,v=np.linalg.eig(value_solve)
#固有値をソート
ind=np.argsort(lamda)
x1=ind[-1]
x2=ind[-2]
#print(x1,x2)
#print(lamda)
#print(ind)
plt.scatter(v[:,x1],v[:,x2])
plt.show()
