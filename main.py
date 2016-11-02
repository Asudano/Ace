import sys
from CharacterData import CharacterData
from GameData import GameData
import Calculations
# from TrackerEnums import GameClass, GameCharacter

def main():
	data = GameData("./shadow_dragon.csv")
	"""
	Uncomment for some output demonstrating performance
	
	for c in data.game_characters:
		print c.name
		for b in c.game_class_options:
			print b
			print c.growth_rate_class[b]
			
		# not sure how to not use a list here
		print c.base_stats[0].level
		print c.base_stats[0].game_class
		print c.base_stats[0].get_stat_value('HP')
		
	"""
	# move this later
	(data.base_classes).append('Lord')
	(data.base_classes).append('Thief')
	(data.base_classes).append('Ballistician')
	(data.base_classes).append('Chameleon')
	(data.base_classes).append('Manakete')
	Calculations.math_model(data.game_characters, data.max_stats, data.promotion_gains, data.base_classes, data.promoted_classes, 'Caeda', 10, 'Pegasus Knight')
	
if __name__ == "__main__":
    main()
