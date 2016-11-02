from tkinter import *
from UserLogs import UserLogs
from StatEnum import Stat

class compare_char_Ui(Frame):
    def __init__(self, user_logs, master=None):
        Frame.__init__(self, master)
        self.charattribute = []
        self.user_logs = user_logs
        self.createwidgets()

    def create_labels(self, charachter_name, grideN, colN):
        master = self.master
        charname = Label(master, text=charachter_name)
        charname.grid(row=grideN, column=0, columnspan=1, sticky=E + W)

    def create_text_box(self, attribute, gridN):
        master = self.master
        textbox = Entry(master)
        textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
        textbox.insert(0, attribute)
        self.charattribute.append(textbox)

    def compare_f(self):
        name1 = self.user_logs.get_char_instance(str(self.charattribute[0].get()))
        name2 = self.user_logs.get_char_instance(str(self.charattribute[1].get()))
        curr_state1 = name1.get_current_state()
        curr_state2 = name2.get_current_state()

        self.create_labels(str(self.charattribute[0].get()), 2, 0)
        self.create_labels(str(self.charattribute[1].get()), 2, 1)

        self.create_labels(curr_state1.get_stat_value(Stat.HP), 3, 0)
        self.create_labels(curr_state2.get_stat_value(Stat.HP), 3, 1)

        self.create_labels(curr_state1.get_stat_value(Stat.Str), 4, 0)
        self.create_labels(curr_state2.get_stat_value(Stat.Str), 4, 1)

        self.create_labels(curr_state1.get_stat_value(Stat.Mag), 5, 0)
        self.create_labels(curr_state2.get_stat_value(Stat.Mag), 5, 1)

        self.create_labels(curr_state1.get_stat_value(Stat.Skl), 6, 0)
        self.create_labels(curr_state2.get_stat_value(Stat.Skl), 6, 1)

        self.create_labels(curr_state1.get_stat_value(Stat.Spd), 7, 0)
        self.create_labels(curr_state2.get_stat_value(Stat.Spd), 7, 1)

        self.create_labels(curr_state1.get_stat_value(Stat.Lck), 8, 0)
        self.create_labels(curr_state2.get_stat_value(Stat.Lck), 8, 1)

        self.create_labels(curr_state1.get_stat_value(Stat.Def), 9, 0)
        self.create_labels(curr_state2.get_stat_value(Stat.Def), 9, 1)

        self.create_labels(curr_state1.get_stat_value(Stat.Res), 10, 0)
        self.create_labels(curr_state2.get_stat_value(Stat.Res), 10, 1)

    def createwidgets(self):
        master = self.master
        self.create_labels("Character 1 Name", 0, 0)
        self.create_text_box("", 0)

        self.create_labels("Character 2 Name", 1, 0)
        self.create_text_box("", 1)
        compare = Button(master, text="Compare", command=self.compare_f)
        compare.grid(row=2, column=0, columnspan=2, sticky=E+W)

if __name__ == "__main__":
    root = Tk()
    user_logs = UserLogs("log.csv")
    app = compare_char_Ui(user_logs, master=root)
    app.mainloop()
    root.destroy()

