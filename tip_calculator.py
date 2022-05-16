#tip calculator

#find a total
#choose a tip 
#split between people

print ('Welcome to the tip calculator.\n')
total = input('What was the total bill?\n')
tip = input('What percentage tip would you like to give? 10, 12, or 15?\n')
split = input('How many people to split the bill?\n')


payment = ((float(total) + (float(total)*int(tip))/100)/int(split))
r_payment = round(payment,2)
message = (f'Each person should pay: ${r_payment} ')
print (message) 
       
