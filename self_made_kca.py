import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from sklearn.decomposition import PCA
import pandas as pd

def kernel_gause(x_i,x_j):
    beta=0.1
    x_norm=np.linalg.norm(x_j-x_i)
    return np.exp(-(x_norm**2)*beta)

#data=np.loadtxt("example_elipsoid_data.csv",delimiter=",")
data=np.loadtxt("example_swithroll_data.csv",delimiter=",")
#data=np.loadtxt("example_2circles.csv",delimiter=",")


'''
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
ax.scatter(r
'''

#カ-ネル行列の生成
kernel_matrix=[]
ones_matrix=[]
data=np.array(data)
for i in range(data.shape[0]):
    a=[]
    for j in range(data.shape[0]):
        result_gause=kernel_gause(data[i,:],data[j,:])
        a.append(result_gause)
    kernel_matrix.append(a)

kernel_matrix=np.array(kernel_matrix)
N=kernel_matrix.shape[0]
print(N)
ones_matrix=np.ones((N,N))/N
print(ones_matrix)

i_n=np.identity(N)
j_n=i_n - ones_matrix

#KCAにおける固有値計算
value_solve=np.dot(j_n,kernel_matrix)
#value_solve= kernel_matrix - ones_matrix * kernel_matrix - kernel_matrix* ones_matrix + ones_matrix * kernel_matrix * ones_matrix
lamda,v=np.linalg.eig(value_solve)

#固有値をソート
ind=np.argsort(lamda)
x1=ind[-1]
x2=ind[-2]

#描写
split_n=[i*0.1 for i in range(1,10,2)]
indices=[int(v.shape[0]*n) for n in split_n]
result_1,result_2,result_3,result_4,result_5,result_6=np.split(v, indices)

#plt.scatter(v[:,x1],v[:,x2])
color_box=['b','g','r','c','m','y','k']
plt.scatter(result_1[:,x1],result_1[:,x2],c=color_box[0])
plt.scatter(result_2[:,x1],result_2[:,x2],c=color_box[1])
plt.scatter(result_3[:,x1],result_3[:,x2],c=color_box[2])
plt.scatter(result_4[:,x1],result_4[:,x2],c=color_box[3])
plt.scatter(result_5[:,x1],result_5[:,x2],c=color_box[4])
plt.scatter(result_6[:,x1],result_6[:,x2],c=color_box[5])
plt.show()
#save_name='kca_plot_beta_1.0.jpg'
#save_name='kca_plot_swithroll_0..jpg'
#save_name='kca_plot_2circles.jpg'
#plt.savefig(save_name)
