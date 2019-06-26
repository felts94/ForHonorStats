'''
Name: Kyle Felter ( change this )
Description: For honor cli stats app

How to use this:

  open Terminal
  cd to where this code is

  Get stats:
  python3 ForHonor.py stats FlavourousBread

  Get Rivals:
  python3 ForHonor.py rivals

  Get Random Hero:
  python3 ForHonor.py randhero
'''

# sys will allow you to read in command line args
import sys
import random
import requests

# This function should take in a name and print stats
# it also appends the persons name to the rivals list, or adds one to matches if they already exist
def getStats(name: str):
    print('your code here')
    # example using requests
    # This does a request to a website and prints the result
    response = requests.get("http://worldclockapi.com/api/json/est/now")
    print(response.json())

    print("Stats of", name, "\n--\nImplement this")

# Shows a list of Rivals
def getRivals():
    print('your code here')
    print('This should print a list of people you have encountered while using this app')

# prints a random hero
def RandHero():
    print('Your code here')
    print('Your Random Hero is:', random.randint(0,100))

# Main function, you should decide which function to call here
def main():
    print("get args")
    for v in sys.argv:
        # Loops through all args passed
        print("Command Line Arg:", v)

    # These are the functions you need to implement
    print('\n\nGet Stats:')
    getStats("FlavourousBread")
    
    print('\n\nGet Rivals:')
    getRivals()

    print('\n\nGet Random Hero:')
    RandHero()

## Dont worry about this, it calls the main function for you
if __name__ == "__main__":
    main()
