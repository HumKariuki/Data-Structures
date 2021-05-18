numbers=(1,2,44,23,-15,97,32,11,39)
for i in numbers:
    if i < 10 or i > 10:
        print('success')
    elif i== 11 or (i<14 and not i ==12):
        print(f'is {i}')

    else:
        print('Everything Else')