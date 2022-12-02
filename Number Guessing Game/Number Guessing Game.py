#This code will first select a random integer and assign it to the variable "prize". It will then take the bids of 4 different players and use if statements to compare them to the actual number. 
#The winner will be determined by whoevers guess was closest to the actual number. If someone guesses the exact number, they also win an additional 500 dollars. If their guess goes over the actual value, they lose.

#Establish price of prize using randint
from random import randint
prize = int(randint(500, 3000))

#Take the guesses of the 4 players
guess1 = int(input('Player 1, place your bid!: '))
guess2 = int(input('Player 2, place your bid!: '))
guess3 = int(input('Player 3, place your bid!: '))
guess4 = int(input('Player 4, place your bid!: '))

if guess1 == prize:
    print('Ding ding ding! One player got it exactly right and gets $500!')
    print(f'Actual price is ${prize}! Player 1 come on up!')
elif guess1 < prize:
    diff1 = prize - guess1
elif guess1 > prize:
    diff1 = 1000000

if guess2 == prize:
    print('Ding ding ding! One player got it exactly right and gets $500!')
    print(f'Actual price is ${prize}! Player 2 come on up!')
elif guess2 < prize:
    diff2 = prize - guess2
elif guess2 > prize:
    diff2 = 1000000

if guess3 == prize:
    print('Ding ding ding! One player got it exactly right and gets $500!')
    print(f'Actual price is ${prize}! Player 3 come on up!')
elif guess3 < prize:
    diff3 = prize - guess3
elif guess3 > prize:
    diff3 = 1000000

if guess4 == prize:
    print('Ding ding ding! One player got it exactly right and gets $500!')
    print(f'Actual price is ${prize}! Player 4 come on up!')
elif guess4 < prize:
    diff4 = prize - guess4
elif guess4 > prize:
    diff4 = 1000000

#Assign the differences to a list
diffs = [diff1, diff2, diff3, diff4]

#Use the min funtion to determine which guess is closest to the actual number
if min(diffs) == 1000000:
    print('Buzz! Awww... everyone has overbid!.')
elif min(diffs) == diff1:
    print(f'Actual prize is {prize}! Player 1 come on up!')
elif min(diffs) == diff2:
    print(f'Actual prize is {prize}! Player 2 come on up!')
elif min(diffs) == diff3:
    print(f'Actual prize is {prize}! Player 3 come on up!')
elif min(diffs) == diff4:
    print(f'Actual prize is {prize}! Player 4 come on up!')
