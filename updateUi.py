from tkinter import *
from GameData import GameData
from State import State
from StatEnum import Stat
from CharacterInstance import CharacterInstance
from UserLogs import UserLogs


class updateUi(Frame):
    def __init__(self, user_logs, master=None):
        Frame.__init__(self, master)
        self.charattribute = []
        self.createwidgets()
        self.user_logs = user_logs

    def update_f(self):

        # 1. select character instance from UserLogs
        char_instance = self.user_logs.get_char_instance(str(self.charattribute[0].get()))

        # 2. Create new State
        stat_dict = {Stat.HP: int(self.charattribute[3].get()), Stat.Str: int(self.charattribute[4].get()),
                     Stat.Mag: int(self.charattribute[5].get()), Stat.Skl: int(self.charattribute[6].get()),
                     Stat.Spd : int(self.charattribute[7].get()), Stat.Lck : int(self.charattribute[8].get()),
                     Stat.Def : int(self.charattribute[9].get()), Stat.Res : int(self.charattribute[10].get()), }
        state = State(int(self.charattribute[2].get()), str(self.charattribute[1].get()), stat_dict)

        # 3. Add state to character instance
        char_instance.add_new_state(state)

        # 4. Add character Instance to user logs
        self._user_logs.update_logs(char_instance)

    def createlabels(self, charachter_name, grideN):
        master = self.master
        charname = Label(master, text=charachter_name)
        charname.grid(row=grideN, column=0, columnspan=1, sticky=E + W)
        self.charattribute.append(charname)

    def createtextbox(self, attribute, gridN):
        master = self.master
        textbox = Entry(master)
        textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
        textbox.insert(0, attribute)
        self.charattribute.append(textbox)

    def createwidgets(self):
        master = self.master

        self.createlabels("Character Name", 0)
        self.createtextbox("",0)

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
        self.createtextbox("",7)

        self.createlabels("Lck", 8)
        self.createtextbox("", 8)

        self.createlabels("Def", 9)
        self.createtextbox("", 9)

        self.createlabels("Res", 10)
        self.createtextbox("",10)

        update = Button(master, text="update", command=self.update_f)
        update.grid(row=11, column=0, columnspan=2, sticky=E+W)



if __name__ == "__main__":
    root = Tk()
    app = updateUi(master=root)
    app.mainloop()
    root.destroy()