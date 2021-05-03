import matplotlib.pyplot as hum
values=(6,7,8,9)
labels=("k","j","l","m")
colors=("g","y","b","r")

hum.pie(values,labels=labels,colors=colors)
hum.show()

country=("c","d","e")
values=(6,7,8)

mg=("r","g","b")
hum.bar(country,values)



hum.title("humic")
hum.xlabel(country)
hum.ylabel(values)
hum.show()

import matplotlib.pyplot as plt

Country = ['USA', 'Canada', 'Germany', 'UK', 'France']
GDP_Per_Capita = [45000, 42000, 52000, 49000, 47000]

plt.bar(Country, GDP_Per_Capita)
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show()



import csv
