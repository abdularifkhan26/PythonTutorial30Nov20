import random
n = random.randint(0,100)
number_of_guesses=1
print("NUmber of guesses is limited to 5 times: ")
while (number_of_guesses<=5):
    i = int(input("Please enter your number:\n"))
    if i<n:
        print("increase your number\n")
    elif i>n:
        print("Decrease your number")
    else:
        print("you won\n")
        print(number_of_guesses, "no of guesses you took to finish")
        break

    print(5-number_of_guesses,"number of guesses left")
    number_of_guesses = number_of_guesses + 1
if(number_of_guesses>5):
    print("Game Over")
    print("The winning number was: ", n)

