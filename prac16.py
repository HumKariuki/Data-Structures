def calculate(a,b,c):
    results = c* (a-b)/2
    return results
print('start')
while True:
    check = input('Type y to perform calculation: ')
    if check == 'y':
        try:
                num1=int(input('First  number: '))
                num2=int(input('Second  number: '))
                num3=int(input('Third  number: '))
                print(calculate(num1,num2,num3))
        except ValueError:
            print('Invalid number found\nTry again')
        continue
    print('Exiting')
    break
print('finish')


def calculate(a,b,c):
    results=c*(a-b)/2
    print(results)

print('start')
for i in range (5):
    calculate(c=i*i,b=i,a=i+i)
    if i>3:
        print('results')

print('finish')