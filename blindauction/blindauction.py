from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bids = {}
bidder = True

def find_highest_bidder(bids):
  mbid = 0
  for i in bids:
    bid_amount = bids[i]
    if bid_amount > mbid:
      mbid = bid_amount
      winner = i
  print(f'The winner is {winner} with a ${mbid} bid. Thanks for playing.')
  
while bidder: 
  name = input("Hello bidder, what is your name?\n")
  bidprice = int(input('What is your bid price?\n'))
  bids[name] = bidprice
  continuepy = input('Are there other bidders? Type yes or no\n')
  if continuepy == 'yes':
    clear()
  else:
    bidder = False
    find_highest_bidder(bids)



  
  
