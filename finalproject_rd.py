#!/usr/bin/env python3

import random

def run_quiz():
    print("Welcome to a galaxy far, far away!")
    print("Your answers will decide the path you take.")

    # Quiz questions
    questions = [
        "Q1: Which color lightsaber would you choose?\n(a) Blue\n(b) Red\n(c) Green\n",
        "Q2: What is your preferred combat style?\n(a) Lightsaber duel\n(b) Force lightning\n(c) Mind control\n",
        # Add more questions as needed
    ]

    # Quiz score variables
    jedi_score = 0
    sith_score = 0

    # Logic for quiz scoring
    for question in questions:
        print(question)
        answer = input().lower()

        if answer == "a":
            jedi_score += 1
        elif answer == "b":
            sith_score += 1
        elif answer == "c":
            jedi_score += 1
            sith_score += 1
        else:
            print("Invalid answer! Skipping this question.")

    # Determine score and character
    if jedi_score > sith_score:
        player_type = "Jedi"
    elif sith_score > jedi_score:
        player_type = "Sith"
    else:
        player_type = random.choice(["Jedi", "Sith"])  # Randomly choose if scores are tied

    print(f"You are a {player_type}!")
    return player_type


def generate_map(player_type):
    if player_type == "Jedi":
        # Generate Jedi map
        map_layout = [
            ["Room A (Artifact): +/- 1 to combat roll", "Room B (Yoda's Room)", "Room C (Combat)"],
        ]
    elif player_type == "Sith":
        # Generate Sith map
        map_layout = [
            ["Room A (Artifact): +/- 1 to combat roll", "Room B (Yoda's Room)", "Room C (Combat)"],
        ]
    else:
        raise ValueError("Invalid player type!")

    return map_layout


def interact_room_a():
    print("You examine the artifact in Room A.")
    choice = input("Do you want to (1) Take artifact or (2) Leave artifact? ")

    if choice == "1":
        bonus = random.choice([-1, 1])
        print(f"You take the artifact and it affects your combat roll by {bonus}.")
        return bonus
    elif choice == "2":
        print("You decide to leave the artifact.")
    else:
        print("Invalid choice! The artifact remains untouched.")

    return 0


def interact_yodas_room():
    print("You enter Yoda's Room.")
    print("Yoda, the wise Jedi Master, is sitting in meditation.")

    while True:
        print("Options:")
        print("1. Ask Yoda for advice")
        print("2. Leave the room")
        choice = input()

        if choice == "1":
            yoda_quotes = [
                "Do or do not. There is no try.",
                "Fear is the path to the dark side. Fear leads to anger, anger leads to hate, hate leads to suffering.",
                "Patience you must have, my young Padawan.",
                "In a dark place we find ourselves, and a little more knowledge lights our way.",
                "The greatest teacher, failure is.",
            ]
            advice = random.choice(yoda_quotes)
            print("Yoda says:", advice)
        elif choice == "2":
            print("You leave the room.")
            break
        else:
            print("Invalid choice! Please try again.")


def interact_combat():
    print("You enter the Combat Room.")
    ready = input("Are you ready to roll? (yes/no) ")

    if ready.lower() == "yes":
        player_roll = random.randint(1, 10)
        darth_vader_roll = random.randint(1, 10)

        print("You roll the dice...")
        print("You rolled:", player_roll)
        print("Darth Vader rolls the dice...")
        print("Darth Vader rolled:", darth_vader_roll)

        if player_roll > darth_vader_roll:
            print("You win! The Force is with you.")
            print("Congratulations! You have completed your mission.")
            print("May the Force be with you, always!")
            exit()
        elif player_roll < darth_vader_roll:
            print("You lose! Darth Vader has defeated you.")
            print("Game over. Try again and embrace the light side!")
            exit()
        else:
            print("It's a tie! The fate of the galaxy remains uncertain.")
    elif ready.lower() == "no":
        print("You decide not to engage in combat. Wise choice!")
    else:
        print("Invalid choice! Combat is inevitable.")


def move_rooms(map_layout, current_room):
    print("Current Room:", current_room)
    print("Options:")
    print("a. Move to Room A (Artifact Room)")
    print("b. Move to Room B (Yoda's Room)")
    print("c. Move to Room C (Combat Room)")
    print("d. Quit game")
    choice = input().lower()

    if choice == "a":
        current_room = map_layout[0][0]
        bonus = interact_room_a()
        current_room += f" (Bonus: {bonus})"
    elif choice == "b":
        current_room = map_layout[0][1]
        interact_yodas_room()
    elif choice == "c":
        current_room = map_layout[0][2]
        interact_combat()
    elif choice == "d":
        print("Quitting the game. Goodbye!")
        exit()
    else:
        print("Invalid choice! Please try again.")

    return current_room


def play_game():
    player_type = run_quiz()
    map_layout = generate_map(player_type)

    current_room = map_layout[0][0]

    print("Instructions:")
    print("You are in a galaxy far, far away.")
    print("You will be presented with a series of rooms.")
    print("You can interact with objects, characters, or make choices in each room.")
    print("Navigate the rooms wisely to achieve your objective!")
    print("\n")

    print("Map Layout:")
    for row in map_layout:
        print(" | ".join(row))

    while True:
        print("\n")
        print("===" * 10)
        current_room = move_rooms(map_layout, current_room)


play_game()

