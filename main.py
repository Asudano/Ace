import sys
from CharacterData import CharacterData
import Reader
import Calculations

def main():
	f = open("./shadow_dragon.csv", "r")
	(game_characters, max_stats, promotion_gains, base_classes, promoted_classes) = Reader.read_infile(f)
	# move this later
	base_classes.append('Lord')
	base_classes.append('Thief')
	base_classes.append('Ballistician')
	base_classes.append('Chameleon')
	base_classes.append('Manakete')
	Calculations.math_model(game_characters, max_stats, promotion_gains, base_classes, promoted_classes, 'Caeda', 10, 'Pegasus Knight')

if __name__ == "__main__":
    main()
