from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createwidgets()

    def level_up(self):
        print("Hello")
        # TODO: Create Level UP logic

    def browse_char(self):
        print("browse")
        # TODO: Create browse char logic

    def initilize_stat_labels(self, name, indexX):
        text_your_stat = Label(self.master, text=name)
        text_your_stat.grid(row=indexX, column=0)
        text_expected_stat = Label(self.master, text=name)
        text_expected_stat.grid(row=indexX, column=4)

    def createwidgets(self):
        master = self.master

        img = PhotoImage(file="CutoutAceSpade.gif").subsample(3, 3)
        player_widget = Label(master, image=img)
        player_widget.image = img
        player_widget.grid(row=0, column=0, rowspan=2)

        char_name = Label(master, text="Character Name")
        char_name.grid(row=2, column=0)

        class_text = Label(master, text="Class")
        class_text.grid(row=0, column=1)

        level_text = Label(master, text="Level")
        level_text.grid(row=1, column=1)

        your_stats_text = Label(master, text="Your Stats")
        your_stats_text.grid(row=3, column=0)

        expected_stats_text = Label(master, text="Expected Stats")
        expected_stats_text.grid(row=3, column=4)

        self.initilize_stat_labels("HP", 4)
        self.initilize_stat_labels("STR", 5)
        self.initilize_stat_labels("MAG", 6)
        self.initilize_stat_labels("Skl", 7)
        self.initilize_stat_labels("Spd", 8)
        self.initilize_stat_labels("Lck", 9)
        self.initilize_stat_labels("Def", 10)
        self.initilize_stat_labels("Res", 11)

        levelUpCharachter = Button(master, text="Level Up Character", command=self.level_up)
        levelUpCharachter.grid(row=12, column=0, columnspan=2)

        browseCharachter = Button(master, text="Browse Characters", command=self.level_up)
        browseCharachter.grid(row=0, column=6, columnspan=2)


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
