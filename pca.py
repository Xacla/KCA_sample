import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from sklearn.decomposition import PCA
import pandas as pd

def kernel_gause(x_i,x_j):
    beta=0.001
    x_norm=np.linalg.norm(x_j-x_i)
    return np.exp(x_norm*(-beta))

#data=np.loadtxt("example_elipsoid_data.csv",delimiter=",")
data=np.loadtxt("example_swithroll_data.csv",delimiter=",")

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

#PCAの場合
pca=PCA()
pca.fit(data)
pca_data=pca.fit_transform(data)
#plt.scatter(pca_data[:,0],pca_data[:,1])
#plt.show()

result_1,result_2,result_3,result_4,result_5,result_6=np.split(pca_data, indices)
plt.scatter(result_1[:,0],result_1[:,1],c=color_box[0])
plt.scatter(result_2[:,0],result_2[:,1],c=color_box[1])
plt.scatter(result_3[:,0],result_3[:,1],c=color_box[2])
plt.scatter(result_4[:,0],result_4[:,1],c=color_box[3])
plt.scatter(result_5[:,0],result_5[:,1],c=color_box[4])
plt.scatter(result_6[:,0],result_6[:,1],c=color_box[5])
plt.show()
