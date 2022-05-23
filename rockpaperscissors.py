import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
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

#Write your code below this line 👇
choices = ['rock', 'paper', 'scissors']
choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
choose = choose.lower()
if choose == '0':
  choose = choices[0]
elif choose == '1':
  choose = choices[1]
elif choose == '2':
  choose = choices[2]
print (f'You have chosen {choose}\n')

choices = ['rock', 'paper', 'scissors']
cpu = random.choice(choices)

print (f'The opponent has chosen {cpu}\n')

if choose == 'rock' and  cpu == 'paper':
  print(f'You chose {rock} \n Computer chose {paper} \n You lose')
elif choose == 'rock' and cpu == 'rock':
  print(f'You chose {rock} \n Computer chose {rock} \n Draw!')
elif choose == 'rock' and cpu == 'scissors':
  print(f'You chose {rock} \n Computer chose {scissors} \n You win!')
elif choose == 'paper' and cpu == 'paper':
  print(f'You chose {paper} \n Computer chose {paper} \n Draw!')
elif choose == 'paper' and cpu == 'rock':
  print(f'You chose {paper} \n Computer chose {rock} \n You win!')
elif choose == 'paper' and cpu == 'scissors':
  print(f'You chose {paper} \n Computer chose {scissors} \n You lose')
elif choose == 'scissors' and cpu == 'paper':
  print(f'You chose {scissors} \n Computer chose {paper} \n You win!')
elif choose == 'scissors' and cpu == 'rock':
  print(f'You chose {scissors} \n Computer chose {rock} \n You lose')
elif choose == 'scissors' and cpu == 'scissors':
  print(f'You chose {scissors} \n Computer chose {scissors} \n Draw!')
