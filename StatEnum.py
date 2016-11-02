from enum import Enum

class Stat(Enum):
	HP = 0
	Str = 1
	Mag = 2
	Skl = 3
	Spd = 4
	Lck = 5
	Def = 6
	Res = 7

def stat_dict(array):
	# TODO: Add doc string
	d = {}
	d[Stat.HP] = int(array[0])
	d[Stat.Str] = int(array[1])
	d[Stat.Mag] = int(array[2])
	d[Stat.Skl] = int(array[3])
	d[Stat.Spd] = int(array[4])
	d[Stat.Lck] = int(array[5])
	d[Stat.Def] = int(array[6])
	d[Stat.Res] = int(array[7])
	return d