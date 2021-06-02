Username='hum'
password='9679'
access=False
attempts=0

while True:
    access=True
    attempts+=1
    pin=input('Enter your password: ')
    username=input('Enter you username: ')

    if attempts<=3 and pin==password and username==Username:
        print(f'attempt {attempts}')
        print(f'welcome {username}')
        break
    if attempts>3:
        print('Too many attempts try again later')
        break
    else:
        print('wrong username/paassword')
        break