import random
opt=['rock','paper','scissor']
lim=int(input('Enter winning points '))
user=0
com=0
while(1):
    if com==lim:
        print('Computer Won the Game')
        break
    elif user==lim:
        print('User Won the Game')
        break
    print()
    u_choice=input(' 1.Rock, 2.Paper, 3.Scissor : ').lower()
    if u_choice not in opt:
        print('Invalid Input')
    else:
        c_choice=opt[random.randint(0,2)]
        if (u_choice=='rock' and c_choice=='scissor') or (u_choice=='paper' and c_choice=='rock') or (u_choice=='scissor' and c_choice=='paper'):
            print('User Won..!!')
            user=user+1
            print(f"User Score : {user} ,Computer Score : {com}")
        elif(u_choice==c_choice):
            print('Draw Match..')
        else:
            print('Computer Won..!')
            com+=1
            print(f"User Score : {user} ,Computer Score : {com}")
            
