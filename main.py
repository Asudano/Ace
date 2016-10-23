import sys
from CharacterData import CharacterData
import Reader
import Calculations

def main():
	f = open("./shadow_dragon.csv", "r")
	(game_characters, max_stats, promotion_gains, base_classes, promoted_classes) = Reader.read_infile(f)

if __name__ == "__main__":
    main()
