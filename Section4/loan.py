#Get details of loan

money_owed = float(input("How much money do you owe, in dollars?\n"))         # 50,000
apr = float(input('What is the annual percentage rate of the loan?\n'))       # 5%
payment = float(input('How much will your monthly payment be in dollars?\n')) # $1,000
months =  int(input('How many months did you want to see the results for\n')) # 24 

month_rate = apr/100/12 

for i in range(months):

    # Calculate interest to pay
    interest_paid = money_owed*month_rate

    # Add interest
    money_owed = money_owed + interest_paid 

    if (money_owed - payment <= 0 ):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months5000')
        break


        # Make payment
        money_owed = money_owed - payment

    print('Paid' , payment, ' of which', interest_paid, 'was interest', end =' ')
    print('Now I owe' , money_owed)

