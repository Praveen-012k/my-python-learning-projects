import random
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
2      (____)
---.__(___)
'''
paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock,paper,scissors]
user_input = int(input("what do you choose 0 for rock 1 for paper 2 for scissors"))
computer_choice = random.randint(0,2)
print("computer chose :")
print(images[computer_choice])
if user_input == 0 :
    print("you choose:",images[0])
elif user_input ==1:
    print("you choose :",images[1])
elif user_input == 2:
    print("you choose",images[2])


if user_input == 0 and computer_choice == 1:
    print("you lose")
elif user_input == 1 and computer_choice ==0:
    print("you win!")
elif user_input == 0 and computer_choice == 2:
    print("you win")
elif user_input == 2 and computer_choice ==0:
    print("you lose")
elif user_input == 2 and computer_choice ==1:
    print("you lose")
elif user_input == 1 and computer_choice ==2:
    print("you win")
else:
    print("wrond input !!\n please enter 0 for rock 1 for paper 2 for scissors ")