from tkinter import ttk
import tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.number_of_processes = list(range(1, 11))
        self.number_of_resources = list(range(1, 11))

        self.configure(bg='#3b3b3b')

        label_heading = ttk.Label(self, text="Deadlock Avoidance Algorithm", padding=(30, 15, 30, 15), anchor='center',
                                  style='FGBB.TLabel')
        label_heading.grid(row=0, column=0)

        self.frame = ttk.Frame(self, style='BB.TFrame')
        self.frame.grid(row=1, column=0)

        label_number_of_process = ttk.Label(self.frame, text="Select Number of Process: ", anchor='center',
                                            style='FWBB.TLabel')
        label_number_of_process.grid(row=0, column=0, sticky='EW')
        self.box_number_of_process = ttk.Combobox(self.frame, textvariable=controller.number_of_process,
                                                  values=self.number_of_processes, state='readonly', width=40,
                                                  font=('Century Gothic Bold', 16), justify='center',
                                                  style='BB.TCombobox')
        self.box_number_of_process.grid(row=0, column=1)

        label_number_of_resource = ttk.Label(self.frame, text="Select Number of Resource: ", anchor='center',
                                             style='FWBB.TLabel')
        label_number_of_resource.grid(row=1, column=0, sticky='EW')
        self.box_number_of_resource = ttk.Combobox(self.frame, textvariable=controller.number_of_resource,
                                                   values=self.number_of_resources, state='readonly', width=40,
                                                   font=('Century Gothic Bold', 16), justify='center',
                                                   style='BB.TCombobox')
        self.box_number_of_resource.grid(row=1, column=1)

        btn_next = ttk.Button(self.frame, text="Next", command=self.both_func, style='FB.TButton')
        btn_next.grid(row=2, column=0, columnspan=2)

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=(20, 20), pady=(20, 20))

        for child in self.winfo_children():
            child.grid_configure(padx=(20, 20), pady=(20, 20))

    def both_func(self):
        self.initialize()
        self.controller.show_frame("Algorithm")

    def initialize(self):
        self.controller.number_of_process = int(self.box_number_of_process.get())
        self.controller.number_of_resource = int(self.box_number_of_resource.get())
