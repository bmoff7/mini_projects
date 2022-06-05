#BlackJack
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playgame = True
def deal_card():
    playercards = []
    dealercards = []
    playercards = (random.sample(cards,2))
    dealercards = (random.sample(cards,2))
    print (f'Your cards {playercards}: Current score: {sum(playercards)}')
    print (f'Computer first card is {dealercards[0]}')
    hitstay = 'hit'

    while sum(playercards) < 22:
      if sum(playercards) == 21:
        print ('BlackJack. You win.')
        return playgame is False
      else:  
        hitstay = input('Will you hit or stay\n').lower()
  
          
        if hitstay == 'hit':
          playercards.extend(random.sample(cards, 1))
          print (playercards)
          print(f'Your cards {playercards}: Total score: {sum(playercards)}')
      
        while sum(dealercards) < 18:
            dealercards.extend(random.sample(cards,1))      
            print(f'Computer total is {sum(dealercards)}')
  
      if sum(playercards) > 21:
        print('You busted')
        return playgame is False
      elif sum(dealercards) > 21:
        print('You win because the dealer busted')
        return playgame is False
      if sum(playercards) > sum(dealercards):
        print(f'Your score: {sum(playercards)} | Computer score: {sum(dealercards)}. You Win')
        return playgame is False
      elif sum(playercards) == sum(dealercards):
        print(f'Your score: {sum(playercards)} | Computer score: {sum(dealercards)}. Draw')
        return playgame is False
      else:
        print(f'Your score: {sum(playercards)} | Computer score: {sum(dealercards)}. You Lose')
        return playgame is False
  
while playgame:
    
    
    choose = input('Do you want to play BlackJack? Type yes or no\n')
    if choose == 'yes':
        print(logo)
        deal_card()
    else:
        print('Thanks for playing')
        playgame = False



