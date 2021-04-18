"""interface.py."""
import tkinter as tk
import logic


class Application(tk.Frame):
    """Sample tkinter application class."""

    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize."""
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
        """create_widgets."""
        self.options = ('One', 'Two', 'Three')
        self.V = tk.StringVar()
        self.itemVar = tk.StringVar()

        self.E = tk.Entry(self)
        self.E.grid(row=0, columnspan=3)

        self.optionMenu = tk.OptionMenu(self, self.itemVar, *self.options)
        self.optionMenu.grid(row=1, column=0)

        self.In = tk.Button(self, text='Insert')
        self.In.grid(row=1, column=1)

        self.S = tk.Button(self, text='Show')
        self.S.grid(row=1, column=2)

        self.textLabel = tk.Label(self, text='Default')
        self.textLabel.grid(row=3, columnspan=3)

        logic.settings(self)
