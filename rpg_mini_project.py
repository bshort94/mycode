#!/usr/bin/env python3

import random
import openai

# Set your OpenAI API key
openai.api_key = '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'


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
            ["Jedi Room 1", "Jedi Room 2", "Yoda's Room"]
        ]
    elif player_type == "Sith":
        # Generate Sith map
        map_layout = [
            ["Sith Room 1", "Sith Room 2", "Sith Room 3"]
        ]
    else:
        raise ValueError("Invalid player type!")

    return map_layout


def roll_dice():
    return random.randint(1, 6)


def combat(player_type, combat_multiplier):
    player_roll = roll_dice()
    enemy_roll = roll_dice()

    player_roll *= combat_multiplier

    print(f"{player_type} roll: {player_roll}")
    print(f"Enemy roll: {enemy_roll}")

    if player_roll > enemy_roll:
        print("You win the game!")
        return True
    elif player_roll < enemy_roll:
        print("You lose the game!")
        return False
    else:
        print("It's a tie!")
        return False


def make_decision(room_number, player_type, combat_multiplier):
    if room_number == "Jedi Room 1":
        print("You find a lightsaber on the ground. Do you pick it up? (Y/N)")
        decision = input().upper()

        if decision == "Y":
            combat_multiplier += 1
            print("You picked up the lightsaber. Your combat multiplier increased by 1.")
        else:
            combat_multiplier -= 1
            print("You left the lightsaber behind. Your combat multiplier decreased by 1.")

    return combat_multiplier


def get_yoda_advice(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        temperature=0.5,
        top_p=1.0
    )
    advice = response.choices[0].text.strip().capitalize()

    return advice


def visit_yodas_room():
    print("You enter Yoda's room. He imparts his wisdom upon you:")
    prompt = "Give me life advice, Yoda."

    yoda_speaks = "Yoda says:"
    prompt_with_yoda = f"{yoda_speaks} {prompt}"
    advice = get_yoda_advice(prompt_with_yoda)
    print(f"{yoda_speaks} {advice[len(yoda_speaks):]}")


def move_rooms(map_layout, current_room):
    room_choice = input("Choose the room number to move to or 'yoda' to visit Yoda's room: ")

    if room_choice.lower() == "yoda":
        if current_room == "Yoda's Room":
            print("You are already in Yoda's room.")
        else:
            print("Moving to Yoda's room...")
            current_room = "Yoda's Room"
            visit_yodas_room()
    else:
        try:
            room_choice = int(room_choice)
            if 1 <= room_choice <= len(map_layout[0]):
                current_room = map_layout[0][room_choice - 1]
                print(f"Moving to {current_room}...")
            else:
                print("Invalid room number!")
        except ValueError:
            print("Invalid input!")

    return current_room


def play_game():
    player_type = run_quiz()
    map_layout = generate_map(player_type)
    current_room = map_layout[0][0]
    combat_multiplier = 1

    print("Game Start!")
    print("Rooms: ", map_layout[0])
    print(f"You are in {current_room}.\n")

    while True:
        current_room = move_rooms(map_layout, current_room)
        if current_room == "Yoda's Room":
            continue

        combat_multiplier = make_decision(current_room, player_type, combat_multiplier)
        result = combat(player_type, combat_multiplier)
        if not result:
            print("Game Over!")
            break

        print(f"You are in {current_room}.\n")


play_game()

