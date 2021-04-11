"""logic.py."""


def insert(self):
    """insert."""

    def func():
        self.V.set((self.V.get() + self.itemVar.get())[0:10])

    return func()


def show(self):
    """show."""

    def func():
        self.textLabel['text'] = self.V.get()

    return func()


def mouse(self, event):
    """mouse."""

    def func():
        if str(event.type) == 'Enter':
            self.textLabel['text'] = 'Hi Mouse'
        elif str(event.type) == 'Leave':
            self.textLabel['text'] = 'Bye Mouse'

    return func()


def settings(self):
    """Set up."""
    check = self.register(alpha)
    self.textLabel.bind("<Enter>", lambda event: mouse(self, event))
    self.textLabel.bind("<Leave>", lambda event: mouse(self, event))
    self.E.configure(textvariable=self.V, validate='key', validatecommand=(check, '%P'))
    self.In.configure(command=lambda: insert(self))
    self.S.configure(command=lambda: show(self))


def alpha(txt):
    """alpha."""
    return len(txt) <= 10
