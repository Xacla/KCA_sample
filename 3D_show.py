import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def disp_plot(result,box,num):
    ax.scatter(result[:,0],result[:,1],result[:,2],c='g')
    for i in range(box.shape[1]):
        j=box[num][i]
        ax.scatter(result[j,0],result[j,1],result[j,2],c='r')
    plt.show()

#️⃣data=np.loadtxt("example_elipsoid_data.csv",delimiter=",")
data=np.loadtxt("example_swithroll_data.csv",delimiter=",")
min_box=np.loadtxt("min.csv",delimiter=",")
#data=np.loadtxt("example_2circles.csv",delimiter=",")

split_n=[i*0.1 for i in range(1,10,2)]
indices=[int(data.shape[0]*n) for n in split_n]
result_1,result_2,result_3,result_4,result_5,result_6=np.split(data, indices)
color_box=['b','g','r','c','m','y','k']
fig = plt.figure()
ax = Axes3D(fig)

#disp_plot(result_1,min_box,0)
#disp_plot(result_2,min_box,1)
disp_plot(result_3,min_box,2)
#disp_plot(result_4,min_box,3)
#disp_plot(result_5,min_box,4)
#disp_plot(result_6,min_box,5)
