import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.timeButton = tk.Button(self, text='Time')
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.timeLabel = tk.Label(self)
        self.timeButton.grid()
        self.quitButton.grid()
        self.timeLabel.grid()


app = Application()
app.master.title('Sample timer application')
app.mainloop()
