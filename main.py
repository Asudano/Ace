import sys
from CharacterData import CharacterData
import Reader
import Calculations
from TrackerEnums import GameClass, GameCharacter

def main():
	(game_characters, 
		max_stats, 
		promotion_gains, 
		base_classes, 
		promoted_classes) = Reader.read_infile("./shadow_dragon.csv")

if __name__ == "__main__":
    main()
