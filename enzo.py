#this progect made by enzo
print("welcome in banque misr")
main_pasword=1234
Try=3
name=input("enter ur name : ")
print(F"hello {name}")
print("u have 3 chances")
while True : 
    pasword=int(input("enter ur pasword :"))
    if pasword!=main_pasword :
        print("pasword is false")
        Try-= 1
        if Try==0 : 
          break
    else :
        print(F"welcome {name} pasword is true")
        
    balance=3000
    selection=int(input("enter a process :"))
    if selection==1 :
        print(balance)
    elif selection==2 :
        despoit=int(input("enter ur money :"))
        print(F"ur money is {balance+despoit}")
    elif selection==3 :
        withdraw=int(input('enter ur money what do u withdraw :'))
        print(F"ur balance now is {balance-withdraw}")
        if withdraw>balance :
            print("ur money donot enough")
    else :
        print('thank you')
    break
        

    
