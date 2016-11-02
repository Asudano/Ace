from tkinter import *
from State import State
from StatEnum import Stat
from UserLogs import UserLogs



class UpdateUi(Frame):
    def __init__(self, user_logs, master=None):
        Frame.__init__(self, master)
        self.char_attribute = []
        self.create_widgets()
        self.user_logs = user_logs

    def update_f(self):
        # 1. select character instance from UserLogs
        char_instance = self.user_logs.get_char_instance(str(self.char_attribute[0].get()))

        # 2. Create new State
        stat_dict = {Stat.HP: int(self.char_attribute[3].get()), Stat.Str: int(self.char_attribute[4].get()),
                     Stat.Mag: int(self.char_attribute[5].get()), Stat.Skl: int(self.char_attribute[6].get()),
                     Stat.Spd: int(self.char_attribute[7].get()), Stat.Lck: int(self.char_attribute[8].get()),
                     Stat.Def: int(self.char_attribute[9].get()), Stat.Res: int(self.char_attribute[10].get()), }
        state = State(int(self.char_attribute[2].get()), str(self.char_attribute[1].get()), stat_dict)

        # 3. Add state to character instance
        char_instance.add_new_state(state)

        # 4. Add character Instance to user logs
        self.user_logs.update_logs(char_instance)

    def create_labels(self, charachter_name, grideN):
        master = self.master
        charname = Label(master, text=charachter_name)
        charname.grid(row=grideN, column=0, columnspan=1, sticky=E + W)
        self.char_attribute.append(charname)

    def create_textbox(self, attribute, gridN):
        master = self.master
        textbox = Entry(master)
        textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
        textbox.insert(0, attribute)
        self.char_attribute.append(textbox)

    def create_widgets(self):
        master = self.master

        self.create_labels("Character Name", 0)
        self.create_textbox("", 0)

        self.create_labels("Class", 1)
        self.create_textbox("", 1)

        self.create_labels("Level", 2)
        self.create_textbox("", 2)

        self.create_labels("HP", 3)
        self.create_textbox("", 3)

        self.create_labels("STR", 4)
        self.create_textbox("", 4)

        self.create_labels("MAG", 5)
        self.create_textbox("", 5)

        self.create_labels("Skl", 6)
        self.create_textbox("", 6)

        self.create_labels("Spd", 7)
        self.create_textbox("", 7)

        self.create_labels("Lck", 8)
        self.create_textbox("", 8)

        self.create_labels("Def", 9)
        self.create_textbox("", 9)

        self.create_labels("Res", 10)
        self.create_textbox("", 10)

        update = Button(master, text="update", command=self.update_f)
        update.grid(row=11, column=0, columnspan=2, sticky=E + W)


if __name__ == "__main__":
    root = Tk()
    user_logs = UserLogs("log.csv")
    app = UpdateUi(user_logs, master=root)
    app.mainloop()
    root.destroy()
