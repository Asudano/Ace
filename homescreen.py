from tkinter import *
from NewCharachterUi import NewCharacterUI
from compareCharUi import CompareCharUi
from suggestteamUi import SuggestTeamUi
from updateUi import UpdateUi
from visualizeprogressUI import visualizeprogressUi
from GameData import GameData
from UserLogs import UserLogs


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.game_data = GameData("shadow_dragon.csv")
        self.user_logs = UserLogs("log.csv")
        self.create_widgets()

    def new_character_f(self):
        root = Tk()
        app = NewCharacterUI(self.game_data,self.user_logs, master=root)
        app.mainloop()
        root.destroy()

    def compare_char_f(self):
        root = Tk()
        app = CompareCharUi(self.user_logs, master=root)
        app.mainloop()
        root.destroy()

    def suggest_team_f(self):
        root = Tk()
        app = SuggestTeamUi(self.user_logs, master=root)
        app.mainloop()
        root.destroy()

    def update_f(self):
        root = Tk()
        app = UpdateUi(master=root)
        app.mainloop()
        root.destroy()

    def visualize_progress_f(self):
        root = Tk()
        app = visualizeprogressUi(master=root)
        app.mainloop()
        root.destroy()

    def create_widgets(self):
        master = self.master

        browse_character = Button(master, text="New Characters", command=self.new_character_f)
        browse_character.grid(row=0, column=0, columnspan=2, sticky=E + W)

        compare_char = Button(master, text="Compare Character", command=self.compare_char_f)
        compare_char.grid(row=0, column=3, columnspan=2, sticky=E + W)

        suggest_team = Button(master, text="Suggest Team", command=self.suggest_team_f)
        suggest_team.grid(row=1, column=3, columnspan=2, sticky=E + W)

        update = Button(master, text="Update", command=self.update_f)
        update.grid(row=1, column=0, columnspan=2, sticky=E + W)

        visualize_progress = Button(master, text="Visualize Progress", command=self.visualize_progress_f)
        visualize_progress.grid(row=2, column=0, columnspan=2, sticky=E + W)


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
