import matplotlib.pyplot as plt
import numpy as np


fig=plt.figure()
ax1=fig.add_subplot(131)
ax2=fig.add_subplot(132)
ax3=fig.add_subplot(133)

ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax1.axvline(0.65)
ax3.scatter(np.linspace(0,1,5),np.linspace(0,5,5))

fig.delaxes(ax3)
plt.show()

x= np.linspace(0,10,100)
plt.plot(x,x, label='linear')
plt.legend()
plt.show()

### variables i plython

x=10
y=20
print(x+y)
print(x+3)
y=x+y
print(y)





