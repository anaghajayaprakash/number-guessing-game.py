import random

guesses = []
constant = 10
attempt = 0
n = random.randint(1, 100)

#welcoming players
print("Welcome to the number guessing game!")

print("You have total 10 attempts to guess the number, all the best")

#specifying minimum or maximum level
check = input("Do you want to know minimum or maximum level (y/n)?:")
check = check.lower()

if check == 'y':
    checking = input("(min/max)?:").lower()
    if checking == "min":
         print("minimum value is 1")
    else:            
         print("maximum value is 100")
elif check == 'n':
     print("Ok you can continue the game")
# if the user types anything other than 'n' or 'y'
else:
    print("Invalid input!! please check your input and try again")

             
while check == 'y' or check == 'n':
#asking for a guess
    guess = int(input("Guess the number (between 1 and 100):"))
#if the player repeats a number
    if guess in guesses:
        print("You have already given that number please check and try again later!")
        break
    else:
        guesses.append(guess)
        attempt += 1
        constant -= 1
    if constant <0:
        print("Sorry you are out of attempts. You can come back after 3 hours or you can end the game")
#choice of players        
        decision = input("(Come back after 3 hours/end the game)?:")
        decision = decision.lower()
        if decision == "end the game":
            print(f"Thank you for playing the game,and  the number is {n} ")
            print(f"Your guess are {guesses}")
            break
        else:
            print("Come back after 3 hours with full energy!we are rooting for you")
            break
    
#Guess is correct
    if guess == n:
        print(f"congragulations! You guessed the number in {attempt} attempts")
        break
#Guess is larger than the original number    
    elif guess > n:  
        print("Too High!Try again")
        print(f"You have {constant} attempts left")
#Guess is smaller than the original number
    else :
        print("Too low! Try again")
        print(f"You have {constant} attempts left")
