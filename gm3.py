import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
            if you=='r':
                return False
            elif you =='s':
                return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False

print("comp turn: Rock(r), paper(p),scissor(s)")
randN = random.randint(1,3)
print(randN)
if randN==1:
    comp='r'
elif randN==2:
    comp='p'
elif randN==3:
    comp='s'
you=input('your turn: Rock(r),paper(p),scissors(s)')
a= gameWin(comp,you)
print(f"comp choose",comp)
print(f"you choose",you)
if a==None:
    print('this game is tie!')
elif a:
    print('Congraturations you won!')
else:
    print('you lose!')