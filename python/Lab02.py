# 1. Name:
#      Brandon Odle
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      Takes matching usernames and passwords from a list and compares them to what the user entered to determine if they can gain access
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out how to get it to match the right username with the right password
# 5. How long did it take for you to complete the assignment?
#      Roughly 2 hours


# Imports the json module
import json

# Error handling in case the file isn't present
try:
    # Opens the file and converts usernames and passwords into lists
    with open("Lab02.json") as file:
        data = json.load(file)
        usernames, passwords = data["username"], data["password"]
except:
    print("The file \"Lab02.json\" could not be found.")
    quit()

# Gets the username and passwords as inputs from the user and stores them
username = input("Please input your username:")
password = input("Please input your password:")

# Checks to see if the username is in the list and if it and the password match
if username in usernames and passwords[usernames.index(username)] == password:
    print("You are authenticated to use this system.")
else:
    print("You are not authorized to use this system.")