#7-1. Rental Car: Write a program that asks the user what kind of rental car they would like .
#Print a message about that car, such as “Let me see if I can find you a Subaru .”
prompt = "Tells us your name, and also which rental car you would like."
prompt += "Let me see if I can find you a Subaru"

name = input(prompt)
print("\nGeorge and I want a safe car")
#7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group .
#If the answer is more than eight, print a message saying they’ll have to wait for a table .
#Otherwise, report that their table is ready .
table = input("How many people, are in the dinner group? ")
table = int(table)


if table >= 8:
    print("\nYou'll have to wait for a table.")
else:
    print("\nYour table is ready.")
#7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not .
number = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
number = int(number)

if number * 5 == 10:
    print("\nThe number " + str(number) + " is a multiple of 10.")
else:
    print("\nThe number " + str(number) + " is not a multiple of 10")
#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value .
#As they enter each topping, print a message saying you’ll add that topping to their pizza .
prompt = "\nTell me a topping on the pizza, and I will add the topping to the pizza:"
prompt += "\n\Enter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

    if message != 'quit':
        print(message)

#7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
#•	Use a conditional test in the while statement to stop the loop .
#•	Use an active variable to control how long the loop runs .
#•	Use a break statement to exit the loop when the user enters a 'quit' value .


#7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches . Then make an empty list called finished_sandwiches .
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
#As each sandwich is made, move it to the list of finished sandwiches .
#After all the sandwiches have been made, print a message listing each sandwich that was made .
sandwich_orders =['ham', 'italian', 'pork', 'turkey']
finished_sandwiches = ['turkey','pork','italian','ham']
while sandwich_orders:
    current_user = sandwich_orders.pop()
    print("Verifying user: " + current_user.title())
    finished_sandwiches.append(current_user)
    print("\nI made your sandwich:")
    for finished_sandwiches in finished_sandwiches:
        print(finished_sandwiches.title())
#7-10. Dream Vacation: Write a program that polls users about their dream vacation .
#Write a prompt similar to If you could visit one place in the world, where would you go?
#Include a block of code that prints the results of the poll .
prompt = "\nIf you could visit one celebrity in the world, who would you meet?"
prompt +="\nEnter celebrity to program."
message = ""
if message != "celebrity":
    message = input(prompt)
    print(message)


