import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import KernelPCA

#data=np.loadtxt("example_elipsoid_data.csv",delimiter=",")
data=np.loadtxt("example_swithroll_data.csv",delimiter=",")
#data=np.loadtxt("example_2circles.csv",delimiter=",")

kpca=KernelPCA(kernel="rbf")
x_kpca=kpca.fit_transform(data)

split_n=[i*0.1 for i in range(1,10,2)]
indices=[int(x_kpca.shape[0]*n) for n in split_n]
result_1,result_2,result_3,result_4,result_5,result_6=np.split(x_kpca, indices)

#plt.scatter(v[:,x1],v[:,x2])
color_box=['b','g','r','c','m','y','k']
plt.scatter(result_1[:,0],result_1[:,1],c=color_box[0])
plt.scatter(result_2[:,0],result_2[:,1],c=color_box[1])
plt.scatter(result_3[:,0],result_3[:,1],c=color_box[2])
plt.scatter(result_4[:,0],result_4[:,1],c=color_box[3])
plt.scatter(result_5[:,0],result_5[:,1],c=color_box[4])
plt.scatter(result_6[:,0],result_6[:,1],c=color_box[5])
plt.show()
