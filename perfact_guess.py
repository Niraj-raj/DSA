import random
randnumber=random.randint(1,200)
# print(randnumber)
gusses=0
userinput=None
while(userinput!=randnumber):
    gusses=gusses+1
    userinput=int(input("enter the numbers: "))
    if randnumber==userinput:
        print("you are correct ")
    else:
        if randnumber>userinput:
            print("you gassed it wrong! enter larger number")
        else:
            print("you gassed it wrong! enter smaller number")  
print(f"you found the numbers in {gusses} gusses ") 

'''with open("highscore.txt","r") as f:
    highscore=int(f.read())
if(highscore>gusses):
    print("you have just broken the record...")
    with open("highscore.txt","w") as f:
        f.write(str(highscore))'''
        