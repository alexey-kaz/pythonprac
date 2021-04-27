from model import Model
from view import View

if __name__ == "__main__":
    m = Model()
    v = View(model=m)
    m.start(v)
    v.mainloop()
