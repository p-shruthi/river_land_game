# rivers_and_land
Game to find the length of river

Main Python program:

The read_csv.py file reads the file ' Task_Training_Data.csv' and filters only the name and email of the user.
The authenticate.py authenticate the user's name and email and only give access to play the game if the input matches the record from read_csv.py. Once the input match with the record, the user is left to start a game. The game() function from game_functionality is called to run a game.

Here we are taking the matrix input from the user, values in matrix(0's & 1's only).   

Each 0 represents land, and each 1 represents part of a river.
A river consists of any number of 1s that are either horizontally or vertically adjacent
(but not diagonally adjacent). The number of adjacent 1s forming a river determine its
size. 
I wrote a function returns an array of the sizes of all rivers represented in the
input matrix. The sizes need not to be in any particular order.


Now from returned array of sizes I need to print "Guess the size of River" on each index, take input from user as guesses for each entry.

If all entered sizes match then show You are the winner.
If 60% of the inputs match with sizes in array of river sizes,show you got second position.
else Show "Invest more money on Almonds, then come back".

After the execution of code: Ask if player wanted to play again: 
IF Yes : Redirect to the Matrix Input.
Else : Exit.
