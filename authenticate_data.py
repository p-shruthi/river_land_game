from read_csv import *

def authenticate():
    count = 1

    while True:

        name = input('Please enter your name: ')
        email = input('Please enter your email: ')

        if count > 2:
            print('\nInput limit exceed!')
            break
        else:
            global name_list, email_list
            if name in name_list and email in email_list:
                print('\nYour input matched the file in our list')

                f = open('welcome_note.txt', '+r')
                message = f.read()
                print(message)

                def choice_to_enter():
                    choice = input("\nDo you want to get in? Enter 'Yes' or 'No' : ")

                    if choice == 'Yes':
                        f = open('game_instruction.txt', '+r')
                        message = f.read()
                        print(message)

                        play = input("\n Press 'P' to Play   ")
                        while play != 'P':
                            play = input("\n Press 'P' to Play   ")
                        if play == 'P':
                            from game_functionality import game
                            game()
                        elif play == 'P':
                            print('Invalid Entry')
                            play = input("\n Press 'P' to Play   ")

                    elif choice == 'No':
                        exit()
                    else:
                        print("Please enter 'Yes' or 'No'")
                        choice_to_enter()
                choice_to_enter()

            else:
                print('Incorrect name/email, please try again!')
                count = count + 1
authenticate()
