age=int(input('Enter your age: '))
name=input('Enter your name: ')
if age>18:
    print(f'{name} You can drive')

elif age ==18:
    print(f'{name}not decide')
else:
    print(f'{name}You cannot drive')

class User:
    pass
user1=User()
user2=User()

user1.name='Mike'
user1.age=33
user1.Available=False

user2.name='James'
user2.age=26
user2.ready=True

print (user1.age)


Username= 'Kariuki'
Password= '9679'
access=False

attemtps=0
User_name=input('Enter your username: ')
User_password=int(input('Enter your password: '))

if User_name==Username and User_password==Password:
    print(f'welcome {Username}')
else:
    print('wrong password / username')

