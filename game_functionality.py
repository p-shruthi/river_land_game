from authenticate_data import *

def game():
    try:
        R = int(input("\nEnter the number of rows:"))
        C = int(input("Enter the number of columns:"))

        if R and C in range(10):
            try:
                m = [[int(input()) for x in range(C)] for y in range(R)]
            except:
                print('\nPlease enter either 1 or 0')
                game()
        else:
            print('\nThe choice is large number. The system prefer small number')
            game()
    except:
        print('\nPlease enter a valid number')
        game()

    print('\nArray of sizes of all river = ', m)
    lines = []
    j = 0
    count = 0
    temp = 0
    for i in range(len(m)):
        while (j < len(m[0])):
            while (j < len(m[0]) and m[j][i] == 1):
                count += 1
                temp = i + 1
                while (temp < len(m[0]) and m[j][temp] == 1):
                    count += 1
                    m[j][temp] = 0
                    temp += 1
                j += 1
            if (count >= 1):
                lines.append(count)
            count = 0
            j += 1
        j = 0


    correct = []
    for i in range(len(lines)):
        guess = int(input('\nGuess the size of the river: '))
        if guess in lines:
            correct.append(guess)


    if len(correct) == len(lines):
        print('\nYou are the winner, all index matched')
    elif round(0.6 * len(lines)) <= len(correct) <= round(0.9 * len(lines)):
        print('\nyou got second position')
        print(correct, 'matched in', lines)
    else:
        print('\nYour Guess is wrong, then come back')
        print(correct, 'matched in', lines)

    def ask():
        question = input("\nDO YOU WANT TO PLAY AGAIN IF YES PRESS 'Y' ELSE PRESS 'N': \n> ")
        if question == 'Y':
            #from game_functionality_dupli import game
            return game()
        elif question == 'N':
            print('\nPress enter to quit.')

    ask()
game()