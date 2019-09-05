import os

def run():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')