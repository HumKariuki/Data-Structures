import matplotlib.pyplot as plt
values=(67,77,40,90,50)
labels=("chelsea", "man city","arsenal","man united" ,"liverpool")
colors=("b","#95B3C6","g","r","y")

plt.pie(values,labels=labels,colors=colors)
plt.show()


import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
file=pd.read_csv("ameshousing.csv")

fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
x=file["SalePrice"]
y=file["Gr Liv Area"]
z=file["Overall Qual"]

ax.scatter(x,y,z,c="r")
plt.xticks(rotation=60)
plt.show()
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig= plt.figure()

ax=fig.gca(projection="3d")

x=np.arange(-10,10,0.40)
y=np.arange(-10,10,0.40)
x,y= np.meshgrid(x,y)
R=np.sqrt(x**2+y**2)
z=np.sin(R)

surf=ax.plot_surface(x,y,z, cmap=cm.Spectral)

fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()

file= pd.read_csv("vgsales.csv")

platform=file["Platform"]
genres=file["Genre"]

data= [platform,genres]

fig,ax = plt.subplots(2)
ax[0].hist(data,histtype="step")
ax[1].hist(data,histtype="stepfilled")
plt.xticks(rotation=60)
plt.show()

plt.hist(data,histtype="step",alpha=0.5)
plt.hist(data,histtype="stepfilled")
plt.xticks(rotation=75)
plt.show()

fig_2, ax=plt.subplots()
ps3 = file["platform"].value_counts(dropna=False)

plt.plot(ps3)
plt.hist(platform,histtype="step",alpha=0.5)
plt.xticks(rotation=75)
plt.show()

