import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """
        Buttons:
        -------
        exit - closes window
        """
        self.exitButton = tk.Button(self, text='Exit')
        self.exitButton.grid(row=0, column=1)
        """ 
        Labels: 
        _______
        <MenuItem>
        """
        self.textLabel = tk.Label(self, text='<MenuItem>')
        self.textLabel.grid(row=1, column=1)


app = Application()
app.master.title('task1.py')
app.mainloop()
