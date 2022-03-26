from tkinter import ttk
import tkinter as tk
from frames import StartPage, Algorithm


class DeadlockAvoidanceAlgorithm(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)

        style.configure('BB.TFrame', background='#3b3b3b')
        style.configure('BB.TEntry', background='#3b3b3b', font=('Century Gothic Bold', 16))
        style.configure('FWBB.TLabel', foreground='white', background='#3b3b3b', font=('Century Gothic Bold', 16))
        style.configure('FWBB2.TLabel', foreground='white', background='#3b3b3b', font=('Century Gothic Bold', 14))
        style.configure('FGBB.TLabel', foreground='#3b3b3b', background='gold', font=('Century Gothic Bold', 36))
        style.configure('FGBB2.TLabel', foreground='gold', background='#3b3b3b', font=('Century Gothic Bold', 12))
        style.configure('FB.TButton', foreground='#3b3b3b', font=('Century Gothic Bold', 14))

        self.title("Deadlock Avoidance Algorithm")
        self.state('zoomed')

        self.number_of_process = tk.IntVar()
        self.number_of_resource = tk.IntVar()

        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky='NSEW')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Algorithm):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='NSEW')

        self.show_frame("StartPage")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


app = DeadlockAvoidanceAlgorithm()
app.mainloop()
