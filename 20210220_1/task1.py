import time
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def showtime(self):
        self.timeLabel['text'] = time.ctime(time.time())

    def createWidgets(self):
        self.timeButton = tk.Button(self, text='Time', command=self.showtime)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.timeLabel = tk.Label(self)
        self.timeButton.grid()
        self.quitButton.grid(row=0, column=1)
        self.timeLabel.grid(columnspan=2)


app = Application()
app.master.title('Sample timer application')
app.mainloop()
