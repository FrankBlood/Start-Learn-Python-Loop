#!usr/bin/python
# Filename: if.py
number=23
#guess=int(raw_input('Enter an integer:')) Python2.7
guess=int(input('Enter an integer:'))#Python 3.5

if guess == number:
	print('Congratulations, you guessed it.')
	print('but you do not win any prizes')
elif guess < number:
	print('No, it is a little higher than that')
else:
	print('No, it is a little lower than that')
print('Done')

#test

a=int(input('First number:'))
b=int(input('Second number:'))
print('Sum is:',a+b)