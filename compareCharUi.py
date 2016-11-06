from tkinter import *
from UserLogs import UserLogs
from StatEnum import Stat

class CompareCharUi(Frame):
	"""Manages the UI for the character comparison screen.
	"""

	def __init__(self, user_logs, master=None):
		"""inits a new CompareCharUi object to compare two 
		user-specified characters

		Args:
		    user_logs : UserLogs variable containing user data
		    master : tkinter.widget identifying the parent widget
		"""
		Frame.__init__(self, master)
		self.char_attribute = []
		self.user_logs = user_logs
		self.create_widgets()

	def create_labels(self, character_name, grideN, colN):
		"""Creates a label for a UI element

		Args:
		    character_name : str that specifies the name of the 
		        character
		    gridN : int that specifies the number of rows
		    colN : int that specifies the number of columns
		"""
		master = self.master
		char_name = Label(master, text=character_name)
		char_name.grid(row=grideN, column=0, columnspan=1, sticky=E + W)

	def create_text_box(self, attribute, gridN):
		"""Creates a text box element

		Args:
		    attribute : str that specifies the attribute for text box
		    gridN : int that specifies number of rows
		"""
		master = self.master
		textbox = Entry(master)
		textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
		textbox.insert(0, attribute)
		self.char_attribute.append(textbox)

	def compare_f(self):
		"""Shows the stats of two different characters for comparison
		"""
		name1 = self.user_logs.get_char_instance(str(self.char_attribute[0].get()))
		name2 = self.user_logs.get_char_instance(str(self.char_attribute[1].get()))
		curr_state1 = name1.get_current_state()
		curr_state2 = name2.get_current_state()
		
		master = self.master
		# names
		char_name1 = Label(master, text=self.char_attribute[0].get())
		char_name1.grid(row=4, column=0, columnspan=1)
		char_name2 = Label(master, text=self.char_attribute[1].get())
		char_name2.grid(row=4, column=1, columnspan=2)
		# HP
		hp1 = Label(master, text=curr_state1.get_stat_value(Stat.HP))
		hp1.grid(row=5, column=0, columnspan=1)
		hp2 = Label(master, text=curr_state2.get_stat_value(Stat.HP))
		hp2.grid(row=5, column=1, columnspan=2)		
		# Str
		str1 = Label(master, text=curr_state1.get_stat_value(Stat.Str))
		str1.grid(row=6, column=0, columnspan=1)
		str2 = Label(master, text=curr_state2.get_stat_value(Stat.Str))
		str2.grid(row=6, column=1, columnspan=2)				
		# Mag
		mag1 = Label(master, text=curr_state1.get_stat_value(Stat.Mag))
		mag1.grid(row=7, column=0, columnspan=1)
		mag2 = Label(master, text=curr_state2.get_stat_value(Stat.Mag))
		mag2.grid(row=7, column=1, columnspan=2)				
		# Skl
		skl1 = Label(master, text=curr_state1.get_stat_value(Stat.Skl))
		skl1.grid(row=8, column=0, columnspan=1)
		skl2 = Label(master, text=curr_state2.get_stat_value(Stat.Skl))
		skl2.grid(row=8, column=1, columnspan=2)				
		# Spd
		spd1 = Label(master, text=curr_state1.get_stat_value(Stat.Spd))
		spd1.grid(row=9, column=0, columnspan=1)
		spd2 = Label(master, text=curr_state2.get_stat_value(Stat.Spd))
		spd2.grid(row=9, column=1, columnspan=2)				
		# Lck
		lck1 = Label(master, text=curr_state1.get_stat_value(Stat.Lck))
		lck1.grid(row=10, column=0, columnspan=1)
		lck2 = Label(master, text=curr_state2.get_stat_value(Stat.Lck))
		lck2.grid(row=10, column=1, columnspan=2)				
		# Def
		def1 = Label(master, text=curr_state1.get_stat_value(Stat.Def))
		def1.grid(row=11, column=0, columnspan=1)
		def2 = Label(master, text=curr_state2.get_stat_value(Stat.Def))
		def2.grid(row=11, column=1, columnspan=2)				
		# Res
		res1 = Label(master, text=curr_state1.get_stat_value(Stat.Res))
		res1.grid(row=12, column=0, columnspan=1)
		res2 = Label(master, text=curr_state2.get_stat_value(Stat.Res))
		res2.grid(row=12, column=1, columnspan=2)
		
	def create_widgets(self):
		"""Creates display elements for update screen
		"""
		master = self.master
		self.create_labels("Character 1 Name", 0, 0)
		self.create_text_box("", 0)
		"""name1 = StringVar(master)
		list_of_names = self.user_logs.get_all_names()
		name1.set(list_of_names[0])
		name1_drop = OptionMenu(
			master, 
			name1, 
			list_of_names)
		name1_drop.grid(row=0, column=1, columnspan=2, sticky=E + W)
		self.char_attribute.append(name1)"""

		self.create_labels("Character 2 Name", 1, 0)
		self.create_text_box("", 1)
		"""name2 = StringVar(master)
		list_of_names = self.user_logs.get_all_names()
		name2.set(list_of_names[0])
		name2_drop = OptionMenu(
			master, 
			name2, 
			list_of_names)
		name2_drop.grid(row=1, column=1, columnspan=2, sticky=E + W)
		self.char_attribute.append(name2)"""
		
		compare = Button(master, text="Compare", command=self.compare_f)
		compare.grid(row=2, column=0, columnspan=2, sticky=E+W)

if __name__ == "__main__":
	root = Tk()
	user_logs = UserLogs("log.csv")
	app = CompareCharUi(user_logs, master=root)
	app.mainloop()
	root.destroy()

