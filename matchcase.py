x=int(input("enetr the any one number: "))

match x :
    case 0 :
        print("x is zero")
    
    case 4 :
        if x%2==0 :
             print("x is divad 2")

        else :
            print("error")

# case_ one type of else
    case _  :     
        print(x)           
     