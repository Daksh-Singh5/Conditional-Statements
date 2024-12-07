costprice = float(input("Enter the cost price of the stuff: "))
sellprice = float(input("Enter the sell price of the stuff: "))

if costprice<sellprice:
    print("You had a profit of💲",sellprice-costprice )
else:
    print("You had a loss of💲",costprice-sellprice)
