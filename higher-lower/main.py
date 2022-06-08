import random
import art
from game_data import data



def choosedp():
  return random.choice(data)
  
  
def format(data):
  name = data['name']
  description = data['description']
  country = data['country']
  return (f'{name} is a {description} from {country}')

def check(answer, a, b):
    if a > b:
      return answer == 'a'
    else:
      return answer == 'b'
      


def game():
  NOTENDGAME = True
  score = 0 
  compare_a = choosedp()
  compare_b = choosedp()
  while NOTENDGAME:
    print(art.logo)
    compare_a = compare_b
    compare_b = choosedp()

    
    if compare_a == compare_b:
      compare_b = choosedp()
    
    print(f'Compare A: {format(compare_a)}')
    print(art.vs)
    print(f'Compare B: {format(compare_b)}')
    
    a = compare_a['follower_count']
    b = compare_b['follower_count']
    
    guess = input ('Who has more followers? A or B\n').lower()

    answer = check(guess,a,b)
    
    
    if answer:
      score += 1
      print(f'correct')
    else: 
      print (f'wrong. final score is {score}')
      NOTENDGAME is False
    
game()

