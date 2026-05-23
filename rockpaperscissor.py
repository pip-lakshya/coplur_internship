import random
list=["Rock","Paper","Scissor"]
usercount=0
compcount=0

def userwin(ucount):
    ucount+=1
    print("\nUser won this one")
    print("------------")
    return ucount

def compwin(ccount):
    ccount+=1
    print("\nComputer won this one")
    print("------------")
    return ccount

def menu(ucount,ccount):
    choice=int(input("\nPress 1 for exit , press 2 for restart"))
    if(choice==2):
        ucount=0
        ccount=0
        print("\nGame restarted")
        print("------------------")
        return [ucount,ccount]
    elif(choice==1):
        ucount=4
        ccount=4
        print("\nExiting game.." \
        "Thanks for playing.")
        return [ucount,ccount]
    else:
        print("Incorrect Choice")

while(usercount<=3 or compcount<=3):
    print("---------------------------------")
    print("\nEnter user input->")
    user=int(input("\nEnter 1:Rock, 2:Paper, 3:Scissor "))
    comp=random.choice(list)
    print("\nComputer's choice:",comp)
    if(user==1):
        if(comp=="Rock"):
            print("\nDraw")
            print("------------")
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        elif(comp=="Paper"):
            compcount=compwin(compcount)
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        elif(comp=="Scissor"):
            usercount=userwin(usercount)
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        else:
            print("Invalid case")
    elif(user==2):
        if(comp=="Rock"):
            usercount=userwin(usercount)
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        elif(comp=="Paper"):
            print("\nDraw")
            print("------------")
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        elif(comp=="Scissor"):
            compcount=compwin(compcount)
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        else:
            print("Invalid case")
    elif(user==3):
        if(comp=="Rock"):
            compcount=compwin(compcount)
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        elif(comp=="Paper"):
            usercount=userwin(usercount)
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        elif(comp=="Scissor"):
            print("\nDraw")
            print("------------")
            print(f"Scores:\nComputer:{compcount}\nUser:{usercount}")
        else:
            print("Invalid case")
    if(compcount==3 and usercount<3):
        print("\n Computer won finally")
        [usercount,compcount]=menu(usercount,compcount)
    elif(usercount==3 and compcount<3):
        print("\n User won finally")
        [usercount,compcount]=menu(usercount,compcount)

    


