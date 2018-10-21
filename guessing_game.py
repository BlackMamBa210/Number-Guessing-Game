import random
import sys
import math

def start_game():
    user_input = '0'
    attempt_count = 0
    score_counter = 0
    random_number = int(random.randrange(1,100))

    first_name = input("What is your name?  ")
    answer = input("Do you want to play the Number Guessing Game? Y/N  ")
    
    if answer.lower() == "n":
          print("Have A Nice Day {}!".format(first_name))
          sys.exit()
    elif answer.lower() == "no":
          print("Have A Nice Day {}!".format(first_name))
          sys.exit()   
    else:
        print("\nWelcome {} to the Number Guessing Game!".format(first_name))
        print("\nThe lower the score the better!")
        print("Guess A Number From 1-100!")

    while user_input != random_number:
        try:
            user_input = int(input())
            attempt_count += 1
            score_counter += 25
        except ValueError:
            print("Oh no thats not a valid answer! Guess again!")
        except TypeError:
            print("Oh no thats not a valid answer! Guess again!")
        else:
            if user_input == random_number:
                print("Congratulations You Guessed It!")
                print("It took you {} attempts and you scored {} points!".format(attempt_count, score_counter))
                ending = input("Thank You For Playing The Number Guessing Game! Would you like to play again? Y/N  ")
                attempt_count == score_counter
                if attempt_count == 0:
                    print("\nCurrent best score is {}!".format(score_counter))
                    attempt_count == score_counter
                if ending.lower() == "n":
                    print("Have A Nice Day {}!".format(first_name))
                    sys.exit()
                if ending.lower() == "no":
                    print("Have A Nice Day {}!".format(first_name))
                    sys.exit()
                if ending.lower() == "":
                    continue
                start_game()
            elif user_input > 100:
                print("Sorry that number is out of the guessing range from 1-100! Guess Again!")
            elif user_input < 1:
                print("Sorry that number is out of the guessing range from 1-100! Guess Again!")
            elif user_input <= random_number:
                print("It's Higher! Guess Again! Mwahahahaha!")
            elif user_input >= random_number:
                print("It's Lower! Guess Again! Mwahahahaha!")
                
    user_input == random_number

        




if __name__ == '__main__':
    start_game()
   
