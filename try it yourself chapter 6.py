# 6-1. Person: Use a dictionary to store information about a person you know .
#  Store their first name, last name, age, and the city in which they live .
# You should have keys such as first_name, last_name, age, and city .
# Print each piece of information stored in your dictionary .
dictionary_0 = {'first_name': 'Joseph', 'last_name':'Lopez', 'age': '19','city': 'Seattle'}
print(dictionary_0['first_name'])
print(dictionary_0['last_name'])
print(dictionary_0['age'])
print(dictionary_0['city'])
#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers .
#  Think of five names, and use them as keys in your dictionary .
#  Think of a favorite number for each person, and store each as a value in your dictionary .
#  Print each person’s name and their favorite number .
# For even more fun, poll a few friends and get some actual data for your program .
favorite_numbers = {
    'Mark': '9',
    'Joseph': '7',
    'Rose': '17',
    'George': '6',
    'Sarah': '2',
    }
print("Mark's favorite number is " +
      favorite_numbers['Mark'].title() + ".")
print("Joseph's favorite number is " +
       favorite_numbers['Joseph'].title() + ".")
print("Rose's favorite number is " +
      favorite_numbers['Rose'].title() + ".")
print("George's favorite number is " +
      favorite_numbers['George'].title() + ".")
print("Sarah's favorite number is " +
      favorite_numbers['Sarah'].title() + ".")
#6-3. Glossary: A Python dictionary can be used to model an actual dictionary .
#However, to avoid confusion, let’s call it a glossary .
#•	Think of five programming words you’ve learned about in the previous chapters .
#Use these words as the keys in your glossary, and store their meanings as values .
#•	Print each word and its meaning as neatly formatted output .
#You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line .
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output .
values_words ={
    'String': 'A series of characters',
    'List': 'A collection of words in a particular order',
    'Comment': 'A tool used to add notes without being part of code',
    'Looping': 'Performing the same action or set of actions on a list',
    'Tuple': 'A list that has parentheses instead of squares'
}
print("String is " +
      values_words['String'].title() + ".")
print("List is " +
      values_words['List'].title() + ".")
print("Comment is " +
      values_words['Comment'].title() + ".")
print("Looping is " +
      values_words['Looping'].title() + ".")
print("Tuple is " +
      values_words['Tuple'].title() + ".")
#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values .
#When you’re sure that your loop works, add five more Python terms to your glossary .
#When you run your program again, these new words and meanings should automatically be included in the output .
values_words = {
    'String': 'A series of characters',
    'List': 'A collection of words in a particular order',
    'Comment': 'A tool used to add notes without being part of code',
    'Looping': 'Performing the same action or set of actions on a list',
    'Tuple': 'A list that has parentheses instead of squares',
    'if statement': 'A statement used to test conditions',
    'if-else statements': 'A statement in which passes and has a different action',
    'if-elif-else statement': 'A test that goes through each item in order to see if passes',
    'Dictionary': 'A tool used in order to connect pieces of related information',
    'Key-values': 'A item used to connect values together in a string or list'
}
for key, value in values_words.items():
    print("\nKey: " + key)
    print("Value: " + value)
#6-6. Polling: Use the code in favorite_languages.py (page 104) .
#•	Make a list of people who should take the favorite languages poll .
#Include some names that are already in the dictionary and some that are not .
#•	Loop through the list of people who should take the poll .
#If they have already taken the poll, print a message thanking them for responding .
#    If they have not yet taken the poll, print a message inviting them to take the poll .
favorite_languages = {
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'dan': 'ruby',
    'rose': 'c',
    'mark': 'python'
}
friends = ['edward','phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi + name.title() +"
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
if 'jacob' not in favorite_languages.keys():
    print("Jacob, please take the poll!")
#6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet .
#In each dictionary, include the kind of animal and the owner’s name .
#Store these dictionaries in a list called pets .
#Next, loop through your list and as you do print everything you know about each pet .
pets = {
    'type1': {
     'owner': 'Joseph',
    'pet': 'rabbit'
    },
    'type2': {
    'owner': 'Tiffany',
    'pet': 'Dog'
    },
    'type3': {
    'owner': 'George',
    'pet': 'Parrot'
    },
    'type4': {
    'owner': 'Anna',
    'pet': 'Iguana'
    }
}
for username, users_info in pets.items():
    print("\nOwner:")
    full_name = users_info['owner']
    pet = users_info['pet']

    print("\tFull name: " + full_name.title())
    print("\tpet: " + pet.title())
#6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number .
#Then print each person’s name along with their favorite numbers .
favorite_numbers = {
    'person1': {
        'name':'Mark',
        'numbers':'9,5'
    },
    'person2': {
        'name':'Joseph',
        'numbers':'7,12'
     },
    'person3': {
        'name':'Rose',
        'numbers':'17,3',
                },
    'person4': {
        'name':'George',
        'numbers':'6,14',
                },
    'person5': {
        'name':'Sarah',
        'numbers':'2,4'
    }
    }
for username, users_info in favorite_numbers.items():
    print("\nName:")
    full_name = users_info['name']
    favorite_numbers = users_info['numbers']

    print("\tFullname: " + full_name.title())
    print("\tfavorite_numbers: " + favorite_numbers.title())
#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways .
#Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output .
values_words = {
    'String': 'A series of characters',
    'List': 'A collection of words in a particular order',
    'Comment': 'A tool used to add notes without being part of code',
    'Looping': 'Performing the same action or set of actions on a list',
    'Tuple': 'A list that has parentheses instead of squares',
    'if statement': 'A statement used to test conditions',
    'if-else statements': 'A statement in which passes and has a different action',
    'if-elif-else statement': 'A test that goes through each item in order to see if passes',
    'Dictionary': 'A tool used in order to connect pieces of related information',
    'Key-values': 'A item used to connect values together in a string or list'
}
for key, value in values_words.items():
    print("\nWord: " + key)
    print("Definition: " + value)





