from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createwidgets()

    def level_up(self):
        print("Hello")
        #TODO: Create Level UP logic

    def browse_char(self):
        print("browse")
        #TODO: Create browse char logic

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

        hp_text = Label(master, text="HP")
        hp_text.grid(row=4, column=0)

        hp_e_text = Label(master, text="HP")
        hp_e_text.grid(row=4, column=4)

        str_text = Label(master, text="STR")
        str_text.grid(row=5, column=0)

        str_e_text = Label(master, text="STR")
        str_e_text.grid(row=5, column=4)

        mag_text = Label(master, text="MAG")
        mag_text.grid(row=6, column=0)

        mag_e_text = Label(master, text="MAG")
        mag_e_text.grid(row=6, column=4)

        skl_text = Label(master, text="Skl")
        skl_text.grid(row=7, column=0)

        skl_e_text = Label(master, text="Skl")
        skl_e_text.grid(row=7, column=4)

        spd_text = Label(master, text="Spd")
        spd_text.grid(row=8, column=0)

        spd_e_text = Label(master, text="Spd")
        spd_e_text.grid(row=8, column=4)

        lck_text = Label(master, text="Lck")
        lck_text.grid(row=9, column=0)

        lck_e_text = Label(master, text="Lck")
        lck_e_text.grid(row=9, column=4)

        def_text = Label(master, text="Def")
        def_text.grid(row=10, column=0)

        def_e_text = Label(master, text="Def")
        def_e_text.grid(row=10, column=4)

        res_text = Label(master, text="Res")
        res_text.grid(row=11, column=0)

        res_e_text = Label(master, text="Res")
        res_e_text.grid(row=11, column=4)

        levelUpCharachter = Button(master, text="Level Up Character", command=self.level_up)
        levelUpCharachter.grid(row=12, column=0, columnspan=2)

        browseCharachter = Button(master, text="Browse Characters", command=self.level_up)
        browseCharachter.grid(row=0, column=6, columnspan=2)


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()