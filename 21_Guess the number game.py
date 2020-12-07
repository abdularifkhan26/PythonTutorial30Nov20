import random
n = random.randint(0,50)
# Will generate random number from 0 to 50
number_of_guesses=1
print("NUmber of guesses is limited to 7 times: ")
while (number_of_guesses<=7):
    i = int(input("Please enter your number:\n"))
    if i<n:
        print("increase your number\n")
    elif i>n:
        print("Decrease your number")
    else:
        print("you won\n")
        print(number_of_guesses, "no of guesses you took to finish")
        break
# Increase the number of guesses to improve winning probability
    print(7-number_of_guesses,"number of guesses left")
    number_of_guesses = number_of_guesses + 1
if(number_of_guesses>7):
    print("Game Over")
    print("The winning number was: ", n)
#Thanks to Harry for motivating me for Python 
