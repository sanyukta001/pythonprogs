x=23
time=9
while(time>0):
    time-=1
    n=int(input("Enter your guess "))
    if(n==x):
        print("YOU WON!!!!")
        print("your no. of guesses left was",time)
        break
    else:
        print("wrong guess,No. of guesses left",time)
        if(n>x):
            print("guess with a lesser number ")
        else:
            print("guess with a greater number ")
if(n!=x and time==0):
    print("GAME OVER!!!!")
    print("YOU LOOSE!!!!")
    

    
