computer_choice = 'rock'
user_choice = input('do you want rock, paper, or scissors \n')

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You Win!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You Win!")
elif user_choice =='rock' and computer_choice == 'scissors':
    print("You Win!")

else :
    print("You Lose!")