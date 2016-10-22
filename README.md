# Ace
Ace

https://waffle.io/Asudano/Ace/join

https://balsamiq.com/products/mockups/

Different Growth Stats:
HP = health points
Str = strength
Mag = Magic
Skl = Skill
Spd = Speed
Lck = Luck
Def = Defense (against stength)
Res = Resistance (against magic)

All characters have a stat for each of these, but characters who are primarily Mages will have higher Mag/Res growths than Str/Def, and vice versa for physical classes like Cavalier/Knight/etc.

Growth Modeling:

Still in a base class:
character's base stats + (number of levels grown)*(growth rate for that stat in that class)
Example
Want to find Marth's expected Str at Level 10, Marth can only be a Lord
5 + (10)(.5) = 10

In a promoted class:
character's base stats + (number of levels grown)*(growth rate for that stat in base class) + promotion gain for that class + (number of levels grown)*(growth rate for that stat in promoted class)
Example
Caeda as a level 5 Dracoknight (promoted from Pegasus Knight), Spd
12 + (20)*(.85) + 0 + (5)(.85)

The only thing to watch here are that none of the stats go over the caps for that class.
