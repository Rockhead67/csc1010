# try it yourself 5.1
from typing import List

car = 'chevy'
print("Is car == 'chevy'? I predict True.")
print(car == 'chevy')

print("\nIs car == 'ford'? I predict False")
print(car == 'ford')

buffet = 'ribs'
print("Is buffet == 'ribs'? I predict True.")
print(buffet == 'ribs')

print("\nIs buffet == 'nachos'? I predict False")
print(buffet == 'nachos')

book = 'encyclopedia'
print("Is book == 'encyclopedia'? I predict True")
print(book == 'encyclopedia')

print("\nIs book == 'bottle'? I predict False")
print(book == 'bottle')

soda = 'mountain dew'
print("Is soda == 'mountain dew'? I predict True")
print(soda == 'mountain dew')

print("\nIs soda == 'gatorade'? I predict False")
print(soda == 'gatorade')

xbox = 'microsoft'
print("Is xbox == 'microsoft'? I predict True")
print(xbox == 'microsoft')

xbox == 'sony'
print("\nIs xbox == 'sony'? I predict False")
print(xbox == 'sony')
# try it yourself 5.2
requested_steak = 'medium-rare'

if requested_steak != 'rare':
    print("I want medium not rare")

book =['novel', 'dictionary', 'encyclopedia', 'textbook']
for book in book:
    if book == 'novel':
        print(book.lower())
grade = 89
grade == 89

requested_grade = '90'
if requested_grade != '85':
    print("No lower than 90!")
age = 21
if age >= 18:
    print('You are old enough to drink!')
age = 21
if age <= 18:
    print('You are not old enough to drink!')
age = 16
if age < 16:
    print('You cant drive')
age = 16
if age > 16:
    print('You can drive')
clothes = 'shirt' 'and' 'sweater'
print("Is clothes = 'shirt' and 'sweater?' I predict True")
print(clothes == 'shirt' 'and' 'sweater')
cars = 'big and small'
print("Are cars big and small? I predict True")
print(cars == 'big and small')
print("Are cars medium and large? I predict False")
print(cars == 'medium and large')
requested_cars = ['audi', 'subaru', 'kia', 'chevy']
'audi' in requested_cars
'ford' in requested_cars

# try it yourself 5.3
alien_color = ['green', 'yellow', 'red', 'purple']
if 'green' in alien_color:
    print('player earns 5 points!')
if 'purple' in alien_color:
    print('False')
alien_color = ['red']
if 'red' in alien_color:
    print('player earns 10 points!')
# try it yourself 5.4
alien_color = ['blue', 'green', 'orange', 'black']
if 'green' in alien_color:
    print('player earns 5 points!')
else:
    print('player earns 10 points!')
    print('color not green')
# try it yourself 5.5
alien_color = ['green', 'purple', 'yellow', 'red']
if 'green' in alien_color:
    print('player earned 5 points.')
elif 'yellow' in alien_color:
    print('player earned 10 points.')
elif 'red' in alien_color:
    print('player earned 15 points.')
# try it yourself 5.6
person_life = 100
if person_life < 2:
    print('person is a baby')
elif person_life < 4:
    print('person is a toddler')
else: person_life < 13
print('person is a kid')
if  person_life  < 20:
    print('person is a teenager')
elif person_life  < 65:
    print('person is and adult')
else: person_life > 65
print('person is an elder')
# try it yourself 5.7
favorite_fruit = 'fruit'
if 'apple' in favorite_fruit:
    print('You like apples too?')
elif 'Tomato' in favorite_fruit:
    print('Tomato is the best fruit')
else: 'kiwi' in favorite_fruit
print('False')
if 'strawberry' in favorite_fruit:
    print('Strawberries are sweet')
elif 'orange' in favorite_fruit:
    print(False)
# try it yourself 5.8
names = ['admin', 'george', 'rocky', 'mary', 'goat']
if names in names:
    print('names')
    print("Hello,admin, would you like to see a status report?")
    print('Hello george, thank you for logging in again')
    print ('Hello rocky, thank you for logging in again')
    print ('Hello mary, thank you for logging in again')
    print ('Hello goat, thank you for logging in again')
# try it yourself 5.9
if 'list' is names:
    print('We need more users!')
# try it yourself 5.10
current_users = ['gerry', 'mark', 'rocko', 'sally', 'fart']
new_users = ['gerry', 'lucy', 'mark', 'owen', 'dave']
if 'gerry' in new_users:
    print('Choose new username')
if 'mark' in new_users:
    print('Choose new username')
# try it yourself 5.11
numbers = [list(range(1-10))]
for numbers in numbers:
    print(numbers)
if range(1-10) in numbers:
    print('1st,2nd,3rd,4th,5th,6th,7th,8th,9th')
