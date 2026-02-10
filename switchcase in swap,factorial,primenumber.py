print("enter 1 for swaping number \n enter 2 for factorial \n enter 3 find prime number  ")
entered_number = input("enter any number you want : ")
a={10,20,30}


if entered_number == '1' : 
         x=int(input("enter the value of x: "))
         y=int(input("enter the value of y: "))
         temp=x
         x=y
         y=temp
         print(f"After swapping: x = {x}, y = {y}")

if entered_number == '2' :
        
        a= input("Enter elements separated by space: ")
        i=int(input("enter the value of i : "))
        f=1
        # a=int(input("enetr the possitive value of a :"))
        for X in range(1,len(a)):
                
                factorial=i*(i-f)
                f+1
                print(factorial)
        

if entered_number == '3':
    num=int(input("enter the any one number : "))
    if num>1:
      for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
    else:
         print(num , "is not a prime number")