import random

world = 'Hello World'
age = 23
name = "Emmanuel Koduah Tweneboah"
print(world)

number = int(input("Enter a number: "))

if number%2 ==1:
    print(f"{number} is an odd number")
elif number%2 == 0:
    print(f"{number} is an even number")

#########
print(f"I am {age} years old")
print(f"My name is {name}")
print(f"My name is {name} and I am {age} years old")

random.random()              # selects a value between 0.0 and 1.0
random.randint(100,200)      # integers between 100 and 200
random.randrange(100,200,2)  # even numbers between 100 and 200


right_guess = random.randint(1,10)
print(right_guess)
number_Of_guess = 3
guess = 1
while(guess <= number_Of_guess):
    guess_input = int(input('Guess a number from 1 to 10: '))
    if guess_input == right_guess:
        print(f"{guess_input} is the right number. You won")
        break;  
    guess += 1      
else:
    print("YOU FAILED!!!!")


# Declare a list [1, 4, 9, 16, 25]or tuple (1, 4, 9, 16, 25), 
# and using the for-loop print out all values that are even.
    
mylist =  [1, 4, 9, 16, 25]

for x in mylist:
    if x%2==0:
         print(x)

   
thistuple = ("apple", "banana", "cherry")
print(thistuple)

current_age = 23
first_age = 1

thisList = []

while first_age <= current_age:
    thisList.append(first_age);
    print(first_age)
    first_age += 1
print(thisList)
print(sum(thisList))























