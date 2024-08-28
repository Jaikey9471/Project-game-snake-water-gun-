import random

computer= random.choice([1,0,-1])
print("Please Enter a word is S, W ,G")
youstr= input('Enter yourchoice : ')

youdict={"s" : 1,"w" : -1,"g" : 0}

reversedict={-1:"water", 1:"snake",0:"gun"}

you=youdict[youstr]
print(f"you choice : {reversedict[you]}\n Computer choice : {reversedict[computer]}")

if(computer == you):
    print("Its Draw the match")

else:
    if(computer ==1 and you ==-1):
        print("you win")

    elif(computer == -1 and you ==0):
         print("you lose")

    elif(computer ==1 and you ==0):
         print("you win")

    elif(computer ==1 and you == -1):
         print("you lose")

    elif(computer ==0 and you == -1):
         print("you win")

    elif(computer ==0 and you ==1):
         print("you lose")

    else:
        print("somethings went wrong")

