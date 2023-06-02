import requests
import random

URL = "https://opentdb.com/api.php?amount=10&category=20&difficulty=medium&type=multiple"  

def get_trivia_questions():
    response = requests.get(URL)  # Send a GET request to the API URL
    data = response.json()  # Parse the JSON response into a Python dictionary
    results = data["results"]  # Extract the list of trivia questions from the dictionary

    for question in results:
        print("Question:", question["question"])  # Print the question

        answers = random.sample(question["incorrect_answers"], len(question["incorrect_answers"]))
        answers.append(question["correct_answer"])
        random.shuffle(answers)

        for i, answer in enumerate(answers):
            print(f"{i + 1}. {answer}")  # Print the answer options

        user_answer = input("Your answer (enter the number): ")  # Get user input
        correct_answer = answers.index(question["correct_answer"]) + 1

        if int(user_answer) == correct_answer:
            print("Correct answer!")
        else:
            print("Incorrect answer!")
        print()

def main():
    get_trivia_questions()

if __name__ == "__main__":
    main()

