size =input("what size pizza you want(S/M/L)?")
bill=0
if size ==  'S' or size == 's':
    bill +=100
    print("small pizza price is 100 RS.")
elif size == 'M' or size == 'm':
    bill +=200
    print("medium pizza price is 200RS.")
else:
    bill +=300
    print("Large pizza price is 300Rs.")
add_pepperoni = input("do you want pepperoni(Y/N)?")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
 if size == 'S' or size == 's':
    bill +=30
 else:
    bill +=50
extra_cheese= input("do you want extra cheese(Y/N)?")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill +=20
    print(f"your final {bill}")
