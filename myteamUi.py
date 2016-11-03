# not currently used
from tkinter import *


class MyTeamUi(Frame):
    """
        MyTeamUi manages the MyTeam screen of the UI
    """

    def __init__(self, master=None):
		"""
			inits a new MyTeamUi object to suggest CharacterInstances for the user's team

            Args:
                master : tkinter.widget identifying the parent widget
		"""
        Frame.__init__(self, master)
        self.createwidgets()

    def compare_char_f(self):
        pass

    def suggest_team_f(self):
        pass

    def create_widgets(self):
        master = self.master

        compare_char = Button(master, text="Compare Character", command=self.compare_char_f)
        compare_char.grid(row=0, column=0, columnspan=2, sticky=E+W)

        suggest_team = Button(master, text="Suggest Team", command=self.suggest_team_f)
        suggest_team.grid(row=1, column=0, columnspan=2, sticky=E+W)


if __name__ == "__main__":
    root = Tk()
    app = MyTeamUi(master=root)
    app.mainloop()
    root.destroy()
