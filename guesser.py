import random
numofguesses = 0

# print("Hello!, What is your name")
# name = input()
name = raw_input("What is your name?")

number = random.randint(1,20)
print("Number I am thinking of is between 1 and 20 " ,name)

while numofguesses < 6:
    print("Take a Guess. ")
    guess = raw_input()
    guess = int(guess)

    numofguesses = numofguesses + 1
    if guess < number:
        print("Number is too Low")
    if guess > number:
        print("Number is too high")
    if guess == number:
       break
if guess == number:
       numofguesses = str(numofguesses)
       print("Well Done " ,name ,"You guessed the number in: " , numofguesses)

if guess != number:
       number = str(number)
       print("Wrong! Unlucky, The number was: " ,number)