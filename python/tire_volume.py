# Imports the math and datetime functions
import math
import datetime

# Gets the width, aspect ratio, and diameter of the tire
width = int(input('Enter the width of the tire in mm:'))
aspect_ratio = int(input('Enter the aspect ratio of the tire:'))
diameter = int(input('Enter the diameter of the tire in inches:'))

# Calculates the volume of the tire using the information and the formula
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Prints the volume of the tire rounded to 2 decimal places
print(f'The volume of the tire is{volume: .2f} liters.')

# Gets the current date
date = datetime.datetime.now()

# Creates the text file and writes all the information to it
with open("volumes.txt", "at") as volumes_file:
    print(f"{date: %Y-%m-%d %I:%M %p}", file=volumes_file)
    print(f"The width of the tire is", width,"mm", file=volumes_file)
    print("The aspect ratio of the tire is", aspect_ratio, file=volumes_file)
    print("The diamter of the tire is", diameter,"inches", file=volumes_file)
    print(f"The volume of the tire is {volume: .2f} liters", file=volumes_file)