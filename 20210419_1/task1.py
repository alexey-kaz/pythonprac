import tkinter as tk
import gettext

gettext.install("task1", ".", names=("ngettext",))

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def click(self):
        self.count += 1
        self.bttn.set(ngettext('%d time', '%d times', self.count) % (self.count,))

    def createWidgets(self):
        self.count = 0
        self.bttn = tk.StringVar()
        self.bttn.set(ngettext('%d time', '%d times', self.count) % (self.count,))
        self.clickButton = tk.Button(self, text=_('Click me'), command=self.click)
        self.textLabel = tk.Label(self, textvariable=self.bttn)
        self.clickButton.grid(row=0, column=1)
        self.textLabel.grid(columnspan=2)


app = Application()
app.master.title('task1.py')
app.mainloop()
