import tkinter as tk
import sqr


class View(tk.Frame):

    def __init__(self, master=None, model=None, **kw):
        super().__init__(master, **kw)

        self.model = model
        self.grid()

        self.la = tk.Label(self, text="a = ")
        self.la.grid(row=0, column=0)

        self.lb = tk.Label(self, text="b = ")
        self.lb.grid(row=1, column=0)

        self.lc = tk.Label(self, text="c = ")
        self.lc.grid(row=2, column=0)

        self.ea = tk.Entry(self)
        self.ea.grid(row=0, column=1)

        self.eb = tk.Entry(self)
        self.eb.grid(row=1, column=1)

        self.ec = tk.Entry(self)
        self.ec.grid(row=2, column=1)

        self.l = tk.Label(self)
        self.l.grid(row=3, columnspan=3)

        self.btn = tk.Button(self, text="Solve", command=self.model.square)
        self.btn.grid(row=1, column=2)

    def square(self):
        return sqr.solveSquare(int(self.ea.get()), int(self.eb.get()), int(self.ec.get()))


