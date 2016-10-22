from CharacterData import CharacterData

def read_infile(infile):
	state = 0
	game_characters = [] # list of characters and their game data
	max_stats = {} # a dictionary mapping the name of a class to a list containing their maximum stats
	promotion_gains = {} # nested dictionary {base_class: {promoted_class: stat gains/losses}}
	
	for line in infile:
		# separators
		# Character,Class,HP GR,Str GR,Mag GR,Skl GR,Spd GR,Lck GR,Def GR,Res GR, - characters, their classes, and growth rates
		# Class_Max,HP,Str,Mag,Skl,Spd,Lck,Def,Res,, - max stats for specific classes
		# Base_Class,Promoted_Class,HP,Str,Mag,Skl,Spd,Def,Res,, - promotion gains
		# Character_Bases,Class,Level,HP,Str,Mag,Skl,Spd,Lck,Def,Res - character base stats
		array = line.split(',')
		if(array[0] == 'Character'):
			state = 1
			continue
		elif(array[0] == 'Class_Max'):
			state = 2
			continue
		elif(array[0] == 'Base_Class'):
			state = 3
			continue
		elif(array[0] == 'Character_Bases'):
			state = 4
			continue
			
		if(state == 1):
			# start reading in characters and growth rates
			# find character in list if it exists
			index = -1
			count = 0
			for char in game_characters:
				if(char.getName() == array[0]):
					index = count
				count += 1
			# if not, add it
			if(index == -1):
				new_char = CharacterData(array)
				game_characters.append(new_char)
			# otherwise edit it
			else:
				game_characters[index].addClassAndGrowthRates(array)
		elif(state == 2):
			# start reading in max stats for specific classes
			class_name = array[0]
			stat_list = array[1:9]
			max_stats[class_name] = stat_list
		elif(state == 3):
			# start reading in promotion gains
			base_class_name = array[0]
			promo_class_name = array[1]
			stat_list = array[2:9]
			promo_gains = {}
			promo_gains[promo_class_name] = stat_list
			promotion_gains[base_class_name] = promo_gains
		elif(state == 4):
			# start reading in character base stats
			# find character
			index = -1
			count = 0
			for char in game_characters:
				if(char.getName() == array[0]):
					index = count
				count += 1
			game_characters[index].setBaseClassAndStats(array)

	return (game_characters, max_stats, promotion_gains)