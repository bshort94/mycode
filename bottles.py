#!/usr/bin/env python

# Range of bottles

for bottle_count in range(5, 0, -1):
    
    print(f"{bottle_count} bottles of beer on the wall!") 
    
    print(f"{bottle_count} bottles of beer! Take one down, pass it around!")

# Take one bottle awar

    minus_bottle = bottle_count - 1 
    
    if minus_bottle > 0: 
        print(f"{minus_bottle} bottles of beer on the wall!") 
        
    else:

        print("No more bottles of beer on the wall!") 

