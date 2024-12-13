height=int(input("what is your height?"))
if height>=3:
    print("can ride")
    age=int(input("what is your age?"))
    if age<=18:
        print("please pay 250 Rs.")
    else:
        print("please pay 500 RS.")
else:
    print("can't ride")
print("bye")
