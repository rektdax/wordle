import re
import requests
import random
from rich.console import Console

#fetching a list of all 5-letter words in the English language
meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
word_list = pattern.findall(meaningpedia_resp.text)

#having the computer pick a random word
computer_choice = word_list[random.randint(0, len(word_list))]

#setting up the colors
SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

def correct_place(letter):
	return f'[black on green]{letter}[/]'

def correct_letter(letter):
	return f'[black on yellow]{letter}[/]'

def incorrect_letter(letter):
	return f'[black on white]{letter}[/]'

'''
while game_on:

	guess = Prompt.ask("Guess a 5-letter word: ").upper()

	while len(guess) != 5:
		print("Your guess must be a 5-letter word.")
		guess = Prompt.ask("Guess a 5-letter word: ").upper()

	guessed, pattern = check_guess(guess, computer_choice)
	full_wordle_pattern.append(pattern)



