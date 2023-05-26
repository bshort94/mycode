#!/usr/bin/env python

# Quiz to determine if user is a Jedi or Sith
# Function to compare what score is higher and print results

def determine_allegiance(jedi_score, sith_score):
    if jedi_score > sith_score:
        print("Welcome to the Jedi Order!")
        print("May The Force Be With You!")

    elif sith_score >= jedi_score:
        print("The dark side is a path to many abilites some may consider to be unnatural.")
        print("You are now a Sith.")

# Introduction

print("Welcome Force User!") 
print("Answer the following questions to determine your allegiance.")

# Variable to keep track of score

jedi_score = 0
sith_score = 0

# Question 1
# If user inputs anything besides a it will count as a Sith score by design

print("\nQuestion 1: Which trait do you value the most?")
print("a) Compassion and empathy") 
print("b) Power and strength") 

answer = input("Enter your answer (a or b): ") 

if answer.lower() == "a":
    jedi_score += 1
else:
    sith_score += 1

# Question 2

print("\nQuestion 2: How do you handle conflict?")
print("a) Seek peaceful resolutions")
print("b) Embrace aggression and dominance")

answer = input("Enter your answer (a or b): ")

if answer.lower() == "a":
    jedi_score += 1
else:
    sith_score += 1

# Question 3

print("\nQuestion 3: What is your approach to the Force?")
print("a) Balance between light and dark")
print("b) Harness the power of the dark side")

answer = input("Enter your answer (a or b): ")

if answer.lower() == "a":
    jedi_score += 1
else:
    sith_score += 1

# Quiz Complete

print("\nNo more questions!")
print("Searching your feelings.....")

determine_allegiance(jedi_score, sith_score) 
