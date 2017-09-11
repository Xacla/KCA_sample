import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import KernelPCA

def serch_min(result,number):
    smallest_positive=0
    for i in range(1,result.shape[0]):
        if result[smallest_positive][1]>result[i][1] and result[i][0]>0:
            smallest_positive=i
    print("smallest_",number,"_group:",smallest_positive)
    smallest_negative=0
    for i in range(1,result.shape[0]):
        if result[smallest_negative][1]>result[i][1] and result[i][0]<0:
            smallest_negative=i
    print("smallest_",number,"_group:",smallest_negative)

    return [smallest_positive,smallest_negative]

#data=np.loadtxt("example_elipsoid_data.csv",delimiter=",")
data=np.loadtxt("example_swithroll_data.csv",delimiter=",")
#data=np.loadtxt("example_2circles.csv",delimiter=",")

kpca=KernelPCA(kernel="rbf",gamma=0.3)#ガウシアンカーネルを使う.
x_kpca=kpca.fit_transform(data)
#x_back=kpca.inverse_transform(x_kpca)

split_n=[i*0.1 for i in range(1,10,2)]
indices=[int(x_kpca.shape[0]*n) for n in split_n]
result_1,result_2,result_3,result_4,result_5,result_6=np.split(x_kpca, indices)

min_1=serch_min(result_1,1)
min_2=serch_min(result_2,2)
min_3=serch_min(result_3,3)
min_4=serch_min(result_4,4)
min_5=serch_min(result_5,5)
min_6=serch_min(result_6,6)

min_box=np.array((min_1,min_2,min_3,min_4,min_5,min_6))
np.savetxt("min.csv",min_box,delimiter=",")

#plt.scatter(v[:,x1],v[:,x2])
color_box=['b','g','r','c','m','y','k']
plt.scatter(result_1[:,0],result_1[:,1],c=color_box[0])
plt.scatter(result_2[:,0],result_2[:,1],c=color_box[1])
plt.scatter(result_3[:,0],result_3[:,1],c=color_box[2])
plt.scatter(result_4[:,0],result_4[:,1],c=color_box[3])
plt.scatter(result_5[:,0],result_5[:,1],c=color_box[4])
plt.scatter(result_6[:,0],result_6[:,1],c=color_box[5])
plt.show()
