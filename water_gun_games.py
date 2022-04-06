import random
def gamewin(comp,your):
    if comp==your:
        return None
    elif comp=='s':
        if your=='w':
            return False
        elif your=='g':
            return True  
    elif comp=='w':
        if your=='g':
            return False
        elif your=='s':
            return True 
    elif comp=='g':
        if your=='s':
            return False
        elif your=='w':
            return True        
                      
print("computer terns:snake(s),water(w),gun(g)?")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w' 
elif randno==3:
    comp='g'

your=input("your turn:snake(s),water(w),gun(g)?")   
a=gamewin(comp,your) 
print(f"computer chosen is {comp}")
print(f"you chosen is {your}")
if a==None:
    print("game is tie")
elif a:
    print("you win")
else:
    print("you loss")