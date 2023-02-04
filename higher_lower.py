#to start use this program please run this commands in order
#1) python3 -m venv venv
#2) pip3 install replit
from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    # Add art
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    # Make game repeatable.
    while game_should_continue:
        # Make B become the next A.
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        
        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        #guess input handler
        while not guess == 'a' and not guess == 'b':
            print("Please enter a valid value to continue.")
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        ## Get follower count.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        #check the answer
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear screen between rounds.
        clear()
        print(logo)

        # Check if user is correct.
        if is_correct:
            # Score Keeping.
            score += 1
            # Feedback.
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            # Feedback.
            print(f"Sorry, that's wrong. Final score: {score}")

game()

# end game, asking to the users if they wants to play again
while input("Do you want to play Higher Lower again? Type 'y' or 'n': ") == "y":
    clear()
    game()