import random





player1 = input('Please enter in your name player1 \n')
player2 = input('Please enter in your name player2 \n')

dice1 = random.randint(1,6) + random.randint(1,6)
dice2 = random.randint(1,6) + random.randint(1,6)

if dice1 > dice2:
    print(player1, "You win you rolled", dice1, "&", player2, "rolled", dice2)
elif dice2 > dice1:
    print(player2, "You win you rolled", dice2, "&", player1, "rolled", dice1  )
else:
    print(player1,"&", player2, "You rolled the same it is a tie")
    



