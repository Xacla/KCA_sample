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
'''
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
'''
data=np.loadtxt("example_elipsoid_data.csv",delimiter=",")

split_n=[i*0.1 for i in range(1,10,2)]
indices=[int(data.shape[0]*n) for n in split_n]
result_1,result_2,result_3,result_4,result_5,result_6=np.split(data, indices)
color_box=['b','g','r','c','m','y','k']
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(result_1[:,0],result_1[:,1],result_1[:,2],c=color_box[0])
ax.scatter(result_2[:,0],result_2[:,1],result_2[:,2],c=color_box[1])
ax.scatter(result_3[:,0],result_3[:,1],result_3[:,2],c=color_box[2])
ax.scatter(result_4[:,0],result_4[:,1],result_4[:,2],c=color_box[3])
ax.scatter(result_5[:,0],result_5[:,1],result_5[:,2],c=color_box[4])
ax.scatter(result_6[:,0],result_6[:,1],result_6[:,2],c=color_box[5])
plt.show()

#3次元空間にプロット
'''
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(circle_x,circle_y,hight)
plt.show()
'''

#PCAの場合
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

i_n=np.identity(kernel_matrix.shape[0])
j_n=i_n - ones_matrix

#KCAにおける固有値計算
value_solve=np.dot(j_n,kernel_matrix)
lamda,v=np.linalg.eig(value_solve)

#固有値をソート
ind=np.argsort(lamda)
x1=ind[-1]
x2=ind[-2]

#計算した結果におけるx1が最大値をもつデータを探す
max_x1=0
for serch in range(data.shape[0]):
    if v[serch][x1]>v[max_x1][x1]:
        max_x1=serch
print(data[max_x1,:])

#描写
split_n=[i*0.1 for i in range(1,10,2)]
indices=[int(v.shape[0]*n) for n in split_n]
result_1,result_2,result_3,result_4,result_5,result_6=np.split(v, indices)

#plt.scatter(v[:,x1],v[:,x2])
color_box=['b','g','r','c','m','y','k']
plt.scatter(result_1[:,x1],result_1[:,x2],c=color_box[0])
plt.scatter(result_2[:,x1],result_2[:,x2],c=color_box[0])
plt.scatter(result_3[:,x1],result_3[:,x2],c=color_box[2])
plt.scatter(result_4[:,x1],result_4[:,x2],c=color_box[3])
plt.scatter(result_5[:,x1],result_5[:,x2],c=color_box[0])
plt.scatter(result_6[:,x1],result_6[:,x2],c=color_box[0])
#plt.show()
save_name='kca_plot.jpg'
plt.savefig(save_name)
