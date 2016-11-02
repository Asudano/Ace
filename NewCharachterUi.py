from tkinter import *
from GameData import GameData
from State import State
from StatEnum import Stat
from CharacterInstance import CharacterInstance
from UserLogs import UserLogs



class NewCharachterUI(Frame):
    def __init__(self, game_data, user_logs, master=None):
        Frame.__init__(self, master)
        self.charattribute = []
        self.createwidgets()
        self.game_data = game_data
        self.user_logs = user_logs

    def create(self):
        chatacter_data = self.game_data.get_character_data(str(self.charattribute[0].get()))
        stat_dict = {Stat.HP: int(self.charattribute[3].get()), Stat.Str: int(self.charattribute[4].get()),
                     Stat.Mag: int(self.charattribute[5].get()), Stat.Skl: int(self.charattribute[6].get()),
                     Stat.Spd : int(self.charattribute[7].get()), Stat.Lck : int(self.charattribute[8].get()),
                     Stat.Def : int(self.charattribute[9].get()), Stat.Res : int(self.charattribute[10].get()), }
        state = State(int(self.charattribute[2].get()), str(self.charattribute[1].get()), stat_dict)
        char_inst = CharacterInstance(chatacter_data, state)
        self.user_logs.update_logs(char_inst)


    def createlabels(self, charachter_name, grideN):
        master = self.master
        charname = Label(master, text=charachter_name)
        charname.grid(row=grideN, column=0, columnspan=1, sticky=E + W)

    def createtextbox(self, attribute, gridN):
        master = self.master
        textbox = Entry(master)
        textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
        textbox.insert(0, attribute)
        self.charattribute.append(textbox)

    def createwidgets(self):
        master = self.master

        self.createlabels("Character Name", 0)
        self.createtextbox("", 0)

        self.createlabels("Class", 1)
        self.createtextbox("", 1)

        self.createlabels("Level", 2)
        self.createtextbox("", 2)

        self.createlabels("HP", 3)
        self.createtextbox("", 3)

        self.createlabels("STR", 4)
        self.createtextbox("", 4)

        self.createlabels("MAG", 5)
        self.createtextbox("", 5)

        self.createlabels("Skl", 6)
        self.createtextbox("", 6)

        self.createlabels("Spd", 7)
        self.createtextbox("", 7)

        self.createlabels("Lck", 8)
        self.createtextbox("", 8)

        self.createlabels("Def", 9)
        self.createtextbox("", 9)

        self.createlabels("Res", 10)
        self.createtextbox("", 10)

        levelUpCharachter = Button(master, text="Create", command=self.create)
        levelUpCharachter.grid(row=11, column=0, columnspan=2, sticky=E + W)


if __name__ == "__main__":
    root = Tk()
    game_data = GameData("shadow_dragon.csv")
    user_logs = UserLogs("log.csv")
    app = NewCharachterUI(game_data, user_logs, master=root)
    app.mainloop()
    root.destroy()
