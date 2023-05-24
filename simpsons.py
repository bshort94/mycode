challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]
a = challenge[2][1]
b = challenge[2][0]

def print_challenge():
    print(f"My {a}! The {b} do nothing!")


print_challenge()


trial = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
a = trial[2]["eyes"]
b = trial[2]["goggles"]

def print_trial():
    print(f"My {b}! The {a} do nothing!")

print_trial() 
