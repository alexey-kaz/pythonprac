import tkinter as tk


class Application(tk.Frame):
    """Sample tkinter application class"""

    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize"""
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        """Create all the widgets"""


class App(Application):
    def insert(self):
        self.S.set((self.S.get() + self.itemVar.get())[0:10])

    def show(self):
        self.textLabel['text'] = self.S.get()

    def mouse(self, event):
        if str(event.type) == 'Enter':
            self.textLabel['text'] = 'Hi Mouse'
        elif str(event.type) == 'Leave':
            self.textLabel['text'] = 'Bye Mouse'

    def alpha(self, txt):
        return len(txt) <= 10

    def create_widgets(self):
        super().create_widgets()
        alpha = self.register(self.alpha)
        self.options = ('One', 'Two', 'Three')
        self.S = tk.StringVar()
        self.itemVar = tk.StringVar()

        self.E = tk.Entry(self, textvariable=self.S, validate='key', validatecommand=(alpha, '%P'))
        self.E.grid(row=0, columnspan=3)

        self.optionMenu = tk.OptionMenu(self, self.itemVar, *self.options)
        self.optionMenu.grid(row=1, column=0)

        self.Q = tk.Button(self, text="Insert", command=self.insert)
        self.Q.grid(row=1, column=1)
        self.Q = tk.Button(self, text="Show", command=self.show)
        self.Q.grid(row=1, column=2)

        self.textLabel = tk.Label(self, text='Default')
        self.textLabel.grid(row=3, columnspan=3)
        self.textLabel.bind("<Enter>", self.mouse)
        self.textLabel.bind("<Leave>", self.mouse)


app = App(title="20210315_2")
app.mainloop()
