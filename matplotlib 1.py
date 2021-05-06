from matplotlib import pyplot as plt
print (6*6)
ages_x=(25,26,27,28,29,30,31,32,33,34,35)

dev_y=(38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752)

plt.plot(ages_x,dev_y,label="All Devs")


py_dev_y=(45372,48876,53850,57287,63016,65998,70003,70000,71456,75370,83640)

plt.plot(ages_x,py_dev_y,label="Python")
plt.title("median Salary (usd)by age")
plt.xlabel("ages")
plt.ylabel("Median Salary")
### method 2 plt.legend(["All Devs","python"])
## using legend tou have to know the order
plt.legend()
plt.show()

plt.plot(ages_x,py_dev_y,label="Python")
plt.title("median Salary (usd)by age")
plt.xlabel("ages")
plt.ylabel("Median Salary")
### method 2 plt.legend(["All Devs","python"])
## using legend tou have to know the order
plt.legend()
plt.show()

### adding colors
from matplotlib import pyplot as plt
print (6*6)
ages_x=(25,26,27,28,29,30,31,32,33,34,35)

dev_y=(38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752)

plt.plot(ages_x,dev_y,"k--",marker=".",label="All Devs")


py_dev_y=(45372,48876,53850,57287,63016,65998,70003,70000,71456,75370,83640)

plt.plot(ages_x,py_dev_y,color="b",marker="o",label="Python")
plt.title("median Salary (usd)by age")
plt.xlabel("ages")
plt.ylabel("Median Salary")
### method 2 plt.legend(["All Devs","python"])
## using legend tou have to know the order
plt.legend()
plt.show()


### adding colors
from matplotlib import pyplot as plt
print (6*6)
ages_x=(25,26,27,28,29,30,31,32,33,34,35)

dev_y=(38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752)

plt.plot(ages_x,dev_y,color="y",marker=".",label="All Devs")


py_dev_y=(45372,48876,53850,57287,63016,65998,70003,70000,71456,75370,83640)

plt.plot(ages_x,py_dev_y,color="#5A7D9A",marker="o",label="Python")
plt.title("median Salary (usd)by age")
plt.xlabel("ages")
plt.ylabel("Median Salary")
### method 2 plt.legend(["All Devs","python"])
## using legend tou have to know the order
plt.legend()
plt.show()

students=(40,55,100,80,25)
plt.pie(students)
grade=("A","B","C","D","E")
exp = (0,0,0.2,0,0)
plt.pie(students,labels=grade,explode=exp,autopct="%2.1f%%")
plt.show()

plt.legend()
plt.show()

students=(40,55,100,80,25)
plt.pie(students)
grade=("A","B","C","D","E")
exp = (0,0,0.2,0,0)
plt.pie(students,labels=grade,explode=exp,autopct="%2.1f%%")
plt.show()