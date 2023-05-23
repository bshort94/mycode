#!/usr/bin/env python3

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm", "HomeLander"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!

fav = "HomeLander"
print(f"{fav}is my favorite character!") 

# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.

user = input("Choose a number between 1 and 100: ")
number = int(user) 


nums= [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!


big = max(nums) 
print(f"The largest number in the list is: {big}") 


