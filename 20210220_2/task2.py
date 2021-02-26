import tkinter as tk
from subprocess import run

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def showdir(self):
        self.bttn.set(run("dir", capture_output=True, shell=True).stdout)

    def showdate(self):
        self.bttn.set(run("date", capture_output=True, shell=True).stdout)

    def showgit(self):
        self.bttn.set(run("git", capture_output=True, shell=True).stdout)

    def createWidgets(self):
        self.bttn = tk.StringVar()
        self.dirButton = tk.Button(self, text='dir', command=self.showdir)
        self.dateButton = tk.Button(self, text='date', command=self.showdate)
        self.gitButton = tk.Button(self, text='git', command=self.showgit)
        self.textLabel = tk.Label(self, textvariable=self.bttn)
        self.dirButton.grid(row=0, column=1)
        self.dateButton.grid(row=0, column=2)
        self.gitButton.grid(row=0, column=3)
        self.textLabel.grid(columnspan=4)


app = Application()
app.master.title('task2.py')
app.mainloop()
