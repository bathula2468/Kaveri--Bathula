height=int(input("enter the height"))
bill=0
if height>=3:
    print("you can ride")
    age=int(input("enter the age"))
    if age<12:
        bill=150
        print("your ticket is 150")
    elif age<=18:
            bill=250
            print("your ticket is 250")
    else:
                bill=500
                print("your ticket is 500")
    want_photo=input("do you want to take photo (y/N)?")
    if want_photo=='y':
     bill=bill+50
     print(f"your total{bill}")
    else:
         print("can't ride")
         print("enjoy the ride")
            
             
