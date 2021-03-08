import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def nextItem(self):
        index = self.options.index(self.itemVar.get()) if self.itemVar.get() in self.options else -1
        self.itemVar.set(self.options[(index+1) % len(self.options)])

    def createWidgets(self):
        """
        StringVars:
        -------
        ItemVar
        """
        self.itemVar = tk.StringVar()
        """
        Buttons:
        -------
        exit - closes window
        next item
        """
        self.exitButton = tk.Button(self, text='Exit')
        self.exitButton.grid(row=0, column=1)
        self.nextButton = tk.Button(self, text='Next item', command=self.nextItem)
        self.nextButton.grid(row=2, column=1)
        """ Label <MenuItem> """
        self.textLabel = tk.Label(self, text='<MenuItem>')
        self.textLabel.grid(row=1, column=1)
        """ Option menu consisting of items One, Two, Three """
        self.options = ('One', 'Two', 'Three')
        self.optionMenu = tk.OptionMenu(self, self.itemVar, *self.options)
        self.optionMenu.grid(row=3, column=1)


app = Application()
app.master.title('task1.py')
app.mainloop()
