## number guessing game

A simple python project that allows the player to guess a number between 1 and 100.
The player can choose if he/she want to know the maximum or minimum value (optional).
They have a total of 10 attempts.
If they ran out of atempts, player can come back after 3 hours or they can end the game.



## How it works

* Uses python's random module to generate between 1 and 100.

* Displays the result in each guess and also shows how many attempts is left.

* Lets the user to decide whether to end the game or to continue after 3 hours.

* All guess of the players are displayed at the end of the game.

* If the player repeats a value it will show an error and exits the game. But,player can try again after some time


## EXAMPLE OUTPUT
```

Welcome to the number guessing game!
You have 10 attempts to guess the number,all the best.

Do you want to know the minimum or maximum level(y/n)?: y
(min/max)?: min
minimum value is 1
Guess the number(between 1 and 100):23
Too High! Try again
You have 9 attempts left.
Guess the number(between 1 and 100):9
Too low!Try again 
You have 8 attempts left.

Do you want to know the minimum or maximum level(y/n)?: n
Ok, You can continue the game


#If anything other than 'y' or 'n' is given

Do you want to know the minimum or maximum level(y/n)?: ok
Invalid input!! please check your input and try again

#If the player ran out of attempts

Sorry you are out of attempts. You can come back after 3 hours or you can end the game
Comeback after 3 hours/end the game?: end the game.
Thank you for playing the game, and the number is 45
Your guess are [23,9,39,59,48,40,44,43,42,49]

Comeback after 3 hours/end the game?: comeback after 3 hours
Come back after 3 hours with full energy!we are rooting for you.

#If the player repeat a number

You have already given that number please check and try again later

#If the player guess the number correctly

Congragulations!You guessed the number in 3 attempts

```

## How to run

1. Make sure you installed python program.
2. Open a terminal in thiis folder.
3. Run the command.