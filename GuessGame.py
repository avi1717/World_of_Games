import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    # print(f"Generate secret number {secret_number}")
    return secret_number


def get_guess_from_user(difficulty):
    try:
        player_number = int(input(f"Please select number from 1 to {difficulty}: "))
        if player_number > difficulty or player_number == 0:
            print("Major error")
            raise ValueError("Please choose again")
        else:
            print(f"You have selected {player_number}")
        return player_number
    except Exception as e:
        print(f"Exception {e}")


def compare_results(secret_number, player_number):
    if secret_number == player_number:
        return True
    else:
        return False


def play(difficulty):
    if difficulty == 1:
        if compare_results(generate_number(10), get_guess_from_user(10)):
            print("!!! YOU WON !!!")
        else:
            print("!!! YOU LOST !!!")

    if difficulty == 2:
        if compare_results(generate_number(20), get_guess_from_user(20)):
            print("!!!!! YOU WON !!!!!")
        else:
            print("!!!!! YOU LOST !!!!!")

    if difficulty == 3:
        if compare_results(generate_number(40), get_guess_from_user(40)):
            print("!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!")

    if difficulty == 4:
        if compare_results(generate_number(60), get_guess_from_user(60)):
            print("!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!")

    if difficulty == 5:
        if compare_results(generate_number(100), get_guess_from_user(100)):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
