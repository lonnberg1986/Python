from random import randint
import requests
#Make sure you have termcolor module installed with pip3 | python3 -m pip install termcolor
from termcolor import colored
#Make sure you have pyfiglet module installed with pip3 | pip3 install pyfiglet
import pyfiglet #for help, run help(pyfiglet)
#help(pyfiglet)

#Create a tuple for valid colors accepted by termcolor colored function
termcolor_options = ("grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
#Select a random color from the termcolor_options
random_color = termcolor_options[randint(0,len(termcolor_options)-1)]

#Ask the user for a topic for the jokes
print(f"What would you like to search for?")
#Get the terminal input given by the user
term_input = input()
#Print the name of the application in pyfiglet font with random color
print(colored(pyfiglet.figlet_format("icanhazdadjokes"), random_color))

#Get response for GET request from https://icanhazdadjoke.com/search
url = "https://icanhazdadjoke.com/search"
response =requests.get(
	url,
	headers={"Accept": "application/json"},
	params={"term": term_input}
).json()

#get the number of jokes from the response
num_of_jokes = response["total_jokes"]
#print the total number of jokes with the search keyword
print(f"Total of {num_of_jokes} joke(s) related to {term_input}")
print("Selecting a random joke from results...")
#print a random joke from the results
print(response["results"][randint(0,num_of_jokes - 1)]["joke"])
