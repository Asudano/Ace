from tkinter import *
from UserLogs import UserLogs

class SuggestTeamUi(Frame):
	"""Manages the team suggestion screen
	"""

	def __init__(self, user_logs, master=None):
		"""inits a new SuggestTeamUi object to suggest a team of 
		CharacterInstances for a user

		Args:
		    user_logs : the UserLogs singleton
		    master : tkinter.widget identifying the parent widget
		"""
		Frame.__init__(self, master)
		self.__user_logs = user_logs
		self.__num_char_inp = Entry(master)
		self.create_widgets()

	def suggest_f(self):
		"""Suggests a team based on the highest sum of scores in the 
		most recent State and displays the names
		"""
		master = self.master
		list_char_inst = self.__user_logs.recommend_team(int(
		        self.__num_char_inp.get()))
		for i in range(0, len(list_char_inst)):
			char_inst_label = Label(master, text=list_char_inst[i])
			char_inst_label.grid(
			        row=3+i, 
			        column=0, 
			        columnspan=1, 
			        sticky=E+W)

	def create_widgets(self):
		"""Creates display elements
		"""
		master = self.master
		num_char = Label(master, text="Number of Charachters")
		num_char.grid(row=0, column=0, columnspan=1, sticky=E + W)

		self.__num_char_inp.grid(row=0, column=1, columnspan=1, sticky=E + W)

		compare = Button(master, text="Suggest", command=self.suggest_f)
		compare.grid(row=2, column=0, columnspan=2, sticky=E+W)


if __name__ == "__main__":
	root = Tk()
	user_logs = UserLogs("log.csv")
	app = SuggestTeamUi(user_logs, master=root)
	app.mainloop()
	root.destroy()

