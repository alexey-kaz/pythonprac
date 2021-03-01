import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)


app = Application()
app.master.title('task1.py')
app.mainloop()
