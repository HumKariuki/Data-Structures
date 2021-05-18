password= 'apple'
attempts =0
Username='Kariuki'

while True:
    attempts+=1
    print(f'Attempt number{attempts}/3')

    if attempts <=3:
        user_password = input(('Enter your password: '))
        if user_password == password and attempts <=3:
            print('logged in successfully')
            print(f'How are  you {Username},Welcome ❤❤')
            break
        else:
            if attempts==3 and user_password !=password:
                print('Too many attempt try again later.')
                break
            else:
                print('wrong password, try again.')