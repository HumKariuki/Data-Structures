for i in range (3):
    for j in range (3):
        print(i,j)
        if j ==2:
            print('loop j done')
            break
    if i ==2:
                print('loop i done')
                break

message='FIve plus five is'
answer=input('what is five plus five? ')
print (message,answer)

for i in range(2,10,2):
    print(i)

for i in range(2,10,3):
    print(i)

for i in range (2,9,3):
    if i >=3:
        continue
    else:
        print (i)


check=False
count=0
final_count=0
for i in range(0,21,2):
    if not check:
        count += 1

        if i ==6 or i ==10 or i==16:
            if not check and count > 4:
                check=True
                print(i)
            continue
        final_count = count
print(final_count)


start=True
number=89.2
message='This is a message'
num=input('Enter a number: ')
try:
    if int(num)<number:
        start=False
except ValueError:
 print('invalid Entry')

if start:
    print('Start is still true')
