#tip calculator

#find a total
#choose a tip 
#split between people

print ('Welcome to the tip calculator.\n')
total = input('What was the total bill?\n')
tip = input('What percentage tip would you like to give? 10, 12, or 15?\n')
split = input('How many people to split the bill?\n')


payment = ((int(total) + (int(total)*int(tip))/100)/int(split))
message = (f'Each person should pay: ${payment} ')
print (message) 
       
