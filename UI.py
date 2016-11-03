#This is not in use. This template is being saved but currently this design is not being used.


from tkinter import *
from NewCharachterUi import NewCharachterUI


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createwidgets()

    def level_up(self):
        print("Hello")
        # TODO: Create Level UP logic

    def browse_char(self):
        print("browse")
        root = Tk()
        app = NewCharachterUI(master=root)
        app.mainloop()
        root.destroy()
        # TODO: Create browse char logic

    def initilize_stat_labels(self, name, ys, ex, indexX):
        text_your_stat = Label(self.master, text=name + ": " + str(ys))
        text_your_stat.grid(row=indexX, column=0)
        text_expected_stat = Label(self.master, text=name + ": " + str(ex))
        text_expected_stat.grid(row=indexX, column=4)

    def createwidgets(self):
        master = self.master

        img = PhotoImage(file="CutoutAceSpade.gif").subsample(3, 3)
        player_widget = Label(master, image=img)
        player_widget.image = img
        player_widget.grid(row=0, column=0, rowspan=2)

        char_name = Label(master, text="Character Name: ")
        char_name.grid(row=2, column=0)

        class_text = Label(master, text="Class: ")
        class_text.grid(row=0, column=1)

        level_text = Label(master, text="Level: ")
        level_text.grid(row=1, column=1)

        your_stats_text = Label(master, text="Your Stats")
        your_stats_text.grid(row=3, column=0)

        expected_stats_text = Label(master, text="Expected Stats")
        expected_stats_text.grid(row=3, column=4)

        self.initilize_stat_labels("HP", 0, 0, 4)
        self.initilize_stat_labels("STR", 0, 0, 5)
        self.initilize_stat_labels("MAG", 0, 0, 6)
        self.initilize_stat_labels("Skl", 0, 0, 7)
        self.initilize_stat_labels("Spd", 0, 0, 8)
        self.initilize_stat_labels("Lck", 0, 0, 9)
        self.initilize_stat_labels("Def", 0, 0, 10)
        self.initilize_stat_labels("Res", 0, 0, 11)

        levelUpCharachter = Button(master, text="My Team", command=self.level_up)
        levelUpCharachter.grid(row=12, column=0, columnspan=2, sticky=E+W)

        browseCharachter = Button(master, text="New Characters", command=self.browse_char)
        browseCharachter.grid(row=0, column=6, columnspan=2)

        existingCharachter = Button(master, text="Existing Charachter", command=self.level_up)
        existingCharachter.grid(row=1, column=6, columnspan=2)


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
