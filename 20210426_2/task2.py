import tkinter as tk

class View(tk.Frame):
    def __init_(self, master=None, model = None, **kw):
        super().__init__(master, **kw)
        self.model = model
        self.grid()
        self.E = tk.Entry(self)
        self.E.grid()
        self.L = tk.Label(self)
        self.L.grid()
        self.B = tk.Button(self, text="Copy", command=self.model.copy)
        self.B.grid()


class Model:
	def setup(self, view):
		self.view = view
	
	def copy(self):
		self.view.L["text"] = self.view.E.get()

		
if __name__ == '__main__':
    m = Model()
    v = View(model=m)
    m.setup(v)
    v.mainloop()
