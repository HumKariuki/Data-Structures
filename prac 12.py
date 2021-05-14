message='hello world'
print(message[:6])
print(message*2)

message='hello'
name=input('Enter your name: ')
print(message,name)

num1=4
num2= input('Enter a number: ')
print(num1+int(num2))

name=input('Enter your name: ')
print(f'Hello {name}, How are you?')

Dollars=input('Enter the dollar amount: ')
dirhams=int(Dollars)*3.56
print(Dollars,dirhams)

minimum_age= 18
user_age=input('Enter your age: ')
if int(user_age) >= minimum_age:
    print(name+' '+ 'you are over eighteen.')
else:
    print(name+' '+'you are under eighteen.')

username='kariuki'
password= '9679'
access=False

entered_username=input('Enter your username: ')
entered_password=input('Enter your password: ')

if entered_username==username and entered_password== password:
    access=True

if access:
    print(f'welcome {entered_username}')

else:print('wrong password and/or username.')




