import tkinter as tk


class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title='<application>', **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky='NEWS')
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''


class App(Application):
    def create_widgets(self):
        self.figures = ['oval', 'rectangle', 'line']
        self.fig_help = tk.StringVar()
        self.move = False

        self.T = tk.Text(self, undo=True, font='fixed', borderwidth=2, relief='groove')
        self.T.bind('<Motion>', self.mouse)
        self.T.tag_configure('good', foreground='green')
        self.T.tag_configure('bad', foreground='red')
        self.T.grid(row=0, column=0, sticky='NEWS')

        self.B = tk.LabelFrame(self)
        self.B.grid(row=1, columnspan=2, sticky='NEWS')

        self.L = tk.Label(self.B, textvar=self.fig_help)
        self.L.grid(row=1, column=1)

        self.Q = tk.Button(self.B, text='Quit', command=self.master.quit)

        self.C = tk.Canvas(self, borderwidth=2, relief='groove')
        self.C.grid(row=0, column=1, sticky='NEWS')

        self.CC = tk.Button(self.B, text='CLEAR', command=self.clearCanvas, relief='groove')

        self.R = tk.Button(self.B, text='RUN', command=self.text2canvas, relief='groove')

        for O in self.L, self.CC, self.R, self.Q:
            O.grid(row=1, column=self.B.grid_size()[0], padx=20)

    def clearCanvas(self):
        self.C.delete('all')

    def addTag(self, new_tag, line_num, length):
        if new_tag:
            old_tag = 'bad' if new_tag == 'good' else 'good'
        else:
            return
        self.T.tag_remove(old_tag, '{}.0'.format(line_num), '{}.0 + {} chars'.format(line_num, length))
        self.T.tag_add(new_tag, '{}.0'.format(line_num), '{}.0 + {} chars'.format(line_num, length))

    def text2canvas(self):
        self.clearCanvas()
        text = self.T.get(1.0, tk.END).split('\n')
        for i, line in enumerate(text):
            if not line.lstrip():
                continue
            elif line[0] == '#':
                self.addTag('good', i + 1, len(line))
                continue
            figure = line.split()[0]
            newline = ', '.join(line.split()[1:])
            print('self.C.create_{}({})'.format(figure, newline))
            try:
                eval('self.C.create_{}({})'.format(figure, newline))
                self.addTag('good', i + 1, len(line))
            except Exception:
                self.addTag('bad', i + 1, len(line))

    def mouse(self, event):
        coords = '@' + str(event.x) + ',' + str(event.y)
        check_y = self.T.index(coords)[0]
        text = self.T.get('1.0', tk.END).split('\n')[int(check_y) - 1]
        if ''.join(ch for ch in text if ch.isalnum()) == '':
            self.fig_help.set('Nothing')
        elif text.startswith('#'):
            self.fig_help.set('Comment')
        elif text.split()[0] in self.figures:
            figure = text.split()[0]
            help_line = '{} x0, y0, x1, y1,\n width=\'width\', fill=\'color\''.format(figure)
            if figure != 'line':
                help_line += ', outline=\'color\''
            self.fig_help.set(help_line)
        else:
            self.fig_help.set('Error')


app = App(title='20210322_1')
app.mainloop()
