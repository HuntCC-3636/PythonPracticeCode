import random

computer_choice = random.choice(['rock','paper','scissors'])

user_choice = input('do you want rock, paper, or scissors \n')

if computer_choice == user_choice:
    print('TIE! computer choose rock')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You Win! Computer choose paper ")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You Win! Computer choose rock ")
elif user_choice =='rock' and computer_choice == 'scissors':
    print("You Win! Computer choose scissors")

else :
    print("You Lose! computer choose " + computer_choice)