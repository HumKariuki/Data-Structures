import pandas as pd
import numpy as np
info= np.array(['p','a','n','d','a','s'])
a=pd.Series(info)
print(a)

x= pd.Series(4, index=[0,1,2,3])
print(x)

class animal:
    def speak(self):
        print("animals speaking")


five_adder=lambda num: num+5
print(five_adder(5))

multiplier=lambda n1,n2: n1*n2
print (multiplier(2,3))
print (multiplier(6,3))

from math import sqrt
sqrt(9)

print(sqrt)

import pandas as pd
mpg=pd.read_csv('mpg.csv')
