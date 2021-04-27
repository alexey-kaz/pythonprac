import view


class Model:

    def start(self, view):
        self.view = view

    def square(self):
        self.view.l["text"] = self.view.square()
