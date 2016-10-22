import sys
from CharacterData import CharacterData
import Reader

def main():
	f = open("./shadow_dragon.csv", "r")
	(game_characters, max_stats, promotion_gains) = Reader.read_infile(f)

if __name__ == "__main__":
    main()
