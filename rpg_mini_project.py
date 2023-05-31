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
        while True:
            answer = input().lower()

            if answer in ["a", "b", "c"]:
                break
            else:
                print("Invalid answer! Please choose 'a', 'b', or 'c'.")

        if answer == "a":
            jedi_score += 1
        elif answer == "b":
            sith_score += 1
        elif answer == "c":
            jedi_score += 1
            sith_score += 1

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
            ["Jedi Room 1", "Jedi Room 2"],
            ["Jedi Room 3", "Jedi Room 4"]
        ]
    elif player_type == "Sith":
        # Generate Sith map
        map_layout = [
            ["Sith Room 1", "Sith Room 2"],
            ["Sith Room 3", "Sith Room 4"]
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
        print("You win the combat!")
        return True
    elif player_roll < enemy_roll:
        print("You lose the combat!")
        return False
    else:
        print("It's a tie!")
        return False


def make_decision(room_number, player_type, combat_multiplier):
    if room_number == 1:
        print("You find a lightsaber on the ground. Do you pick it up? (Y/N)")
        while True:
            decision = input().upper()

            if decision in ["Y", "N"]:
                break
            else:
                print("Invalid answer! Please choose 'Y' or 'N'.")

        if decision == "Y":
            combat_multiplier += 1
            print("You picked up the lightsaber. Your combat multiplier increased by 1.")
        else:
            combat_multiplier -= 1
            print("You left the lightsaber behind. Your combat multiplier decreased by 1.")

    elif room_number == 2:
        print("You encounter a group of enemies. Do you engage them? (Y/N)")
        while True:
            decision = input().upper()

            if decision in ["Y", "N"]:
                break
            else:
                print("Invalid answer! Please choose 'Y' or 'N'.")

        if decision == "Y":
            combat_multiplier += 2
            print("You engaged the enemies. Your combat multiplier increased by 2.")

    return combat_multiplier


def main():
    player_type = run_quiz()
    map_layout = generate_map(player_type)
    combat_multiplier = 1

    print(f"Welcome, {player_type}! Let's begin your adventure.")

    while True:
        print("Select a room:")
        for i, row in enumerate(map_layout):
            for j, room in enumerate(row):
                print(f"({i+1},{j+1}): {room}")

        while True:
            try:
                room_choice = input("Enter the room coordinates (row,column): ")
                room_choice = tuple(map(int, room_choice.split(',')))

                if (
                    len(room_choice) == 2
                    and room_choice[0] in [1, 2]
                    and room_choice[1] in [1, 2]
                ):
                    break
                else:
                    print("Invalid room coordinates! Please try again.")
            except ValueError:
                print("Invalid input! Please enter room coordinates as 'row,column'.")

        room_number = map_layout[room_choice[0] - 1][room_choice[1] - 1]
        combat_multiplier = make_decision(room_choice[0], player_type, combat_multiplier)
        result = combat(player_type, combat_multiplier)

        if result:
            print("Congratulations! You won the combat.")
        else:
            print("Game over. You lost the combat.")

        play_again = input("Do you want to play again? (Y/N)").upper()
        if play_again != "Y":
            break

    print("Thank you for playing!")


if __name__ == "__main__":
    main()

