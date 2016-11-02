from tkinter import *
from GameData import GameData
from State import State
from StatEnum import Stat
from CharacterInstance import CharacterInstance
from UserLogs import UserLogs



class NewCharacterUI(Frame):
    def __init__(self, game_data, user_logs, master=None):
        Frame.__init__(self, master)
        self.char_attribute = []
        self.create_widgets()
        self.game_data = game_data
        self.user_logs = user_logs

    def create(self):
        character_data = self.game_data.get_character_data(str(self.charattribute[0].get()))
        stat_dict = {Stat.HP: int(self.charattribute[3].get()), Stat.Str: int(self.charattribute[4].get()),
                     Stat.Mag: int(self.charattribute[5].get()), Stat.Skl: int(self.charattribute[6].get()),
                     Stat.Spd : int(self.charattribute[7].get()), Stat.Lck : int(self.charattribute[8].get()),
                     Stat.Def : int(self.charattribute[9].get()), Stat.Res : int(self.charattribute[10].get()), }
        state = State(int(self.charattribute[2].get()), str(self.charattribute[1].get()), stat_dict)
        char_inst = CharacterInstance(character_data, state)
        self.user_logs.update_logs(char_inst)


    def create_labels(self, charachter_name, grideN):
        master = self.master
        char_name = Label(master, text=charachter_name)
        char_name.grid(row=grideN, column=0, columnspan=1, sticky=E + W)

    def create_text_box(self, attribute, gridN):
        master = self.master
        textbox = Entry(master)
        textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
        textbox.insert(0, attribute)
        self.char_attribute.append(textbox)

    def create_widgets(self):
        master = self.master

        self.create_labels("Character Name", 0)
        self.create_text_box("", 0)

        self.create_labels("Class", 1)
        self.create_text_box("", 1)

        self.create_labels("Level", 2)
        self.create_text_box("", 2)

        self.create_labels("HP", 3)
        self.create_text_box("", 3)

        self.create_labels("STR", 4)
        self.create_text_box("", 4)

        self.create_labels("MAG", 5)
        self.create_text_box("", 5)

        self.create_labels("Skl", 6)
        self.create_text_box("", 6)

        self.create_labels("Spd", 7)
        self.create_text_box("", 7)

        self.create_labels("Lck", 8)
        self.create_text_box("", 8)

        self.create_labels("Def", 9)
        self.create_text_box("", 9)

        self.create_labels("Res", 10)
        self.create_text_box("", 10)

        level_up_character = Button(master, text="Create", command=self.create)
        level_up_character.grid(row=11, column=0, columnspan=2, sticky=E + W)


if __name__ == "__main__":
    root = Tk()
    game_data = GameData("shadow_dragon.csv")
    user_logs = UserLogs("log.csv")
    app = NewCharacterUI(game_data, user_logs, master=root)
    app.mainloop()
    root.destroy()
