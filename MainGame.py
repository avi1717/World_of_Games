from live import load_game, welcome
from gamedata import get_data
from GuessGame import play

print(welcome(get_data("config.json", "name")))
games = load_game()

for x in games.keys():
    if games.keys().__contains__(2):
        play(games.get(2))
    else:
        print("ERROR ! Game not found")
