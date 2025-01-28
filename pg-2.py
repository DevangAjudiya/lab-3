#writ your own function to conver string carecter into uppar/lowar/togal case.
def case():
    a=input("enter the string=")
    print("in lowercase")
    for c in a:
        if 65<=ord(c)<=90 :
            print(chr(ord(c)+32),end="")  
        else:
            print(c,end="")
    print("in upercase")
    for c in a:
        if 97<=ord(c)<=123:
            print(chr(ord(c)-32),end="")  
        else:
            print(c,end="")
    print("in topalcase")
    for c in a:
        if 97<=ord(c)<=123:
            print(chr(ord(c)-32),end="")  
        elif 65<=ord(c)<=90:
            print(chr(ord(c)+32),end="")
        else:
            print(c,end="")
            
   
   
case()                 
