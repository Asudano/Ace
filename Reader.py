from CharacterData import CharacterData

def read_infile(infile):
	state = 0
	game_characters = [] # list of characters and their game data
	max_stats = {} # nested dictionary {class: {stat name: stat}}
	promotion_gains = {} # nested dictionaries {base_class: {promoted_class: {stat name: {stat gains/losses}}}}
	base_classes = [] # list of base classes
	promoted_classes = [] # list of promoted classes
	
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
			stat_list = {}
			stat_list['HP'] = int(array[1])
			stat_list['Str'] = int(array[2])
			stat_list['Mag'] = int(array[3])
			stat_list['Skl'] = int(array[4])
			stat_list['Spd'] = int(array[5])
			stat_list['Lck'] = int(array[6])
			stat_list['Def'] = int(array[7])
			stat_list['Res'] = int(array[8])
			max_stats[class_name] = stat_list
		elif(state == 3):
			# start reading in promotion gains
			base_class_name = array[0]
			if(base_class_name not in base_classes):
				base_classes.append(base_class_name)
			promo_class_name = array[1]
			if(promo_class_name not in promoted_classes):
				promoted_classes.append(promo_class_name)
			stat_list = {}
			stat_list['HP'] = int(array[2])
			stat_list['Str'] = int(array[3])
			stat_list['Mag'] = int(array[4])
			stat_list['Skl'] = int(array[5])
			stat_list['Spd'] = int(array[6])
			stat_list['Def'] = int(array[7])
			stat_list['Res'] = int(array[8])
			promo_gains = {}
			promo_gains[promo_class_name] = stat_list
			promotion_gains[base_class_name] = promo_gains
		elif(state == 4):
			# start reading in character base stats
			index = -1
			count = 0
			for char in game_characters:
				if(char.getName() == array[0]):
					index = count
				count += 1
			game_characters[index].setBaseClassAndStats(array)

	return (game_characters, max_stats, promotion_gains, base_classes, promoted_classes)
