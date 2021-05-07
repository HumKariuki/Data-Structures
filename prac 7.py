def adder(*num):
    sum=0
    for n in num:

        sum= sum+n
        print("Sum:",sum)
        adder(3,5)
        adder(4,5,6,7)
        adder(1,2,3,4,5,6)
### line plots
import matplotlib.pyplot as plt
x=[5,2,9,4,7]
y=[10,5,8,4,2]
plt.plot(x,y)
plt.show()


### bar plotting

x=[5,2,9,4,7]
y=[10,5,8,4,2]
plt.bar(x,y)
plt.show()

y=[13,1,2,6,4]
plt.hist(y)
plt.show()

first_name='Humphrey'
last_name='Kariuki'
full_name=first_name+' '+last_name
print(full_name)

squares=[]
for x in range(1,11):
    print(x)
