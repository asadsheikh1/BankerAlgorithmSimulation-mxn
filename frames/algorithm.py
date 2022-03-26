from tkinter import ttk
import tkinter as tk


class Algorithm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg='#3b3b3b')
        self.set_available = []
        self.set_process_sequence = []
        self.set_safe = bool

        label_heading = ttk.Label(self, text="Deadlock Avoidance Algorithm", padding=(30, 15, 30, 15), anchor='center',
                                  style='FGBB.TLabel')
        label_heading.grid(row=0, column=0)

        button = ttk.Button(self, text="Graphical User Interface (GUI)", command=self.gui, style='FB.TButton')
        button.grid(row=1, column=0)

        self.frame_0 = ttk.Frame(self, style='BB.TFrame')
        self.frame_0.grid(row=2, column=0)

        self.frame_1 = ttk.Frame(self, style='BB.TFrame')
        self.frame_1.grid(row=3, column=0)

        self.frame_2 = ttk.Frame(self, style='BB.TFrame')
        self.frame_2.grid(row=4, column=0)

        self.frame_3 = ttk.Frame(self, style='BB.TFrame')
        self.frame_3.grid(row=5, column=0)

        self.frame_4 = ttk.Frame(self, style='BB.TFrame')
        self.frame_4.grid(row=6, column=0)

        self.frame_5 = ttk.Frame(self, style='BB.TFrame')
        self.frame_5.grid(row=7, column=0)

        self.frame_6 = ttk.Frame(self, style='BB.TFrame')
        self.frame_6.grid(row=9, column=0)

        btn_submit = ttk.Button(self.frame_6, text="Submit", command=self.algorithm, style='FB.TButton')
        btn_submit.grid(row=0, column=0, columnspan=3)

        btn_need = ttk.Button(self.frame_6, text="Find Need", command=self.find_need, style='FB.TButton')
        btn_need.grid(row=1, column=0)

        btn_available = ttk.Button(self.frame_6, text="Find Available", command=self.find_available, style='FB.TButton')
        btn_available.grid(row=1, column=1)

        btn_safe_seq = ttk.Button(self.frame_6, text="Find Safe Process Sequence", command=self.find_safe_seq,
                                  style='FB.TButton')
        btn_safe_seq.grid(row=1, column=2)

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        label_heading.columnconfigure(0, weight=1)
        button.columnconfigure(0, weight=1)
        self.frame_0.columnconfigure(0, weight=1)
        self.frame_1.columnconfigure(0, weight=1)
        self.frame_2.columnconfigure(0, weight=1)
        self.frame_3.columnconfigure(0, weight=1)
        self.frame_4.columnconfigure(0, weight=1)
        self.frame_5.columnconfigure(0, weight=1)
        self.frame_6.columnconfigure(0, weight=1)

    def gui(self):
        dict_no_of_instance_entry = {}
        self.dict_no_of_instance_text_var = {}
        label_no_of_instance = ttk.Label(self.frame_0, text="Number of Instances", style='FWBB2.TLabel')
        label_no_of_instance.grid(row=0, column=0)
        for j in range(self.controller.number_of_resource):
            self.dict_no_of_instance_text_var[f'no_of_instance_text_var{j}'] = tk.IntVar()
        for j in range(self.controller.number_of_resource):
            dict_no_of_instance_entry[f'no_of_instance_entry{j}'] = ttk.Entry(self.frame_0, style='BB.TEntry',
                                                                              textvariable=
                                                                              self.dict_no_of_instance_text_var[
                                                                                  f'no_of_instance_text_var{j}'],
                                                                              justify='center')
            dict_no_of_instance_entry[f'no_of_instance_entry{j}'].grid(row=0, column=j + 1)

        dict_alloc_entry = {}
        self.dict_alloc_text_var = {}
        label_alloc = ttk.Label(self.frame_1, text="Allocation", style='FWBB2.TLabel')
        label_alloc.grid(row=0, column=0)
        for i in range(self.controller.number_of_process):
            for j in range(self.controller.number_of_resource):
                self.dict_alloc_text_var[f'alloc_text_var{i}{j}'] = tk.IntVar()
        for i in range(self.controller.number_of_process):
            label_alloc = ttk.Label(self.frame_1, text=f"P{i}", style='FGBB2.TLabel')
            label_alloc.grid(row=i + 1, column=0)
            for j in range(self.controller.number_of_resource):
                dict_alloc_entry[f'alloc_entry{i}{j}'] = ttk.Entry(self.frame_1, textvariable=self.dict_alloc_text_var[
                    f'alloc_text_var{i}{j}'], justify='center', style='BB.TEntry')
                dict_alloc_entry[f'alloc_entry{i}{j}'].grid(row=i + 1, column=j + 1)

        dict_maximum_entry = {}
        self.dict_maximum_text_var = {}
        label_maximum = ttk.Label(self.frame_2, text="Maximum", style='FWBB2.TLabel')
        label_maximum.grid(row=0, column=0)
        for i in range(self.controller.number_of_process):
            for j in range(self.controller.number_of_resource):
                self.dict_maximum_text_var[f'maximum_text_var{i}{j}'] = tk.IntVar()
        for i in range(self.controller.number_of_process):
            label_maximum = ttk.Label(self.frame_2, text=f"P{i}", style='FGBB2.TLabel')
            label_maximum.grid(row=i + 1, column=0)
            for j in range(self.controller.number_of_resource):
                dict_maximum_entry[f'maximum_entry{i}{j}'] = ttk.Entry(self.frame_2, style='BB.TEntry',
                                                                       textvariable=self.dict_maximum_text_var[
                                                                           f'maximum_text_var{i}{j}'], justify='center')
                dict_maximum_entry[f'maximum_entry{i}{j}'].grid(row=i + 1, column=j + 1)

        dict_need_entry = {}
        self.dict_need_text_var = {}
        label_need = ttk.Label(self.frame_3, text="Need", style='FWBB2.TLabel')
        label_need.grid(row=0, column=0)
        for i in range(self.controller.number_of_process):
            for j in range(self.controller.number_of_resource):
                self.dict_need_text_var[f'need_text_var{i}{j}'] = tk.IntVar()
        for i in range(self.controller.number_of_process):
            label_need = ttk.Label(self.frame_3, text=f"P{i}", style='FGBB2.TLabel')
            label_need.grid(row=i + 1, column=0)
            for j in range(self.controller.number_of_resource):
                dict_need_entry[f'need_entry{i}{j}'] = ttk.Entry(self.frame_3, textvariable=self.dict_need_text_var[
                    f'need_text_var{i}{j}'], justify='center', style='BB.TEntry')
                dict_need_entry[f'need_entry{i}{j}'].grid(row=i + 1, column=j + 1)

        dict_available_entry = {}
        self.dict_available_text_var = {}
        label_available = ttk.Label(self.frame_4, text="Available", style='FWBB2.TLabel')
        label_available.grid(row=0, column=0)
        for j in range(self.controller.number_of_resource):
            self.dict_available_text_var[f'available_text_var{j}'] = tk.IntVar()
        for j in range(self.controller.number_of_resource):
            dict_available_entry[f'available_entry{j}'] = ttk.Entry(self.frame_4, style='BB.TEntry',
                                                                    textvariable=self.dict_available_text_var[
                                                                        f'available_text_var{j}'], justify='center')
            dict_available_entry[f'available_entry{j}'].grid(row=0, column=j + 1)

        dict_safe_seq_entry = {}
        self.dict_safe_seq_text_var = {}
        label_safe_seq = ttk.Label(self.frame_5, text="Safe Process Sequence", style='FWBB2.TLabel')
        label_safe_seq.grid(row=0, column=0)
        for j in range(self.controller.number_of_process):
            self.dict_safe_seq_text_var[f'safe_seq_text_var{j}'] = tk.IntVar()
        for j in range(self.controller.number_of_process):
            dict_safe_seq_entry[f'safe_seq_entry{j}'] = ttk.Entry(self.frame_5, style='BB.TEntry',
                                                                  textvariable=self.dict_safe_seq_text_var[
                                                                      f'safe_seq_text_var{j}'], justify='center')
            dict_safe_seq_entry[f'safe_seq_entry{j}'].grid(row=0, column=j + 1)

        for child in self.frame_0.winfo_children():
            child.grid_configure(padx=(5, 5))

        for child in self.frame_1.winfo_children():
            child.grid_configure(padx=(5, 5))

        for child in self.frame_2.winfo_children():
            child.grid_configure(padx=(5, 5))

        for child in self.frame_3.winfo_children():
            child.grid_configure(padx=(5, 5))

        for child in self.frame_4.winfo_children():
            child.grid_configure(padx=(5, 5))

        for child in self.frame_5.winfo_children():
            child.grid_configure(padx=(5, 5))

        for child in self.frame_6.winfo_children():
            child.grid_configure(padx=(5, 5), pady=(5, 5))

    def algorithm(self):
        self.allocation = [[0 for _ in range(self.controller.number_of_resource)] for _ in
                           range(int(self.controller.number_of_process))]
        self.maximum = [[0 for _ in range(self.controller.number_of_resource)] for _ in
                        range(self.controller.number_of_process)]
        self.need_matrix = [[0 for _ in range(self.controller.number_of_resource)] for _ in
                            range(self.controller.number_of_process)]

        for i in range(self.controller.number_of_process):
            for j in range(self.controller.number_of_resource):
                self.allocation[i][j] = self.dict_alloc_text_var[f'alloc_text_var{i}{j}'].get()
        for i in range(self.controller.number_of_process):
            for j in range(self.controller.number_of_resource):
                self.maximum[i][j] = self.dict_maximum_text_var[f'maximum_text_var{i}{j}'].get()

        for i in range(self.controller.number_of_process):
            for j in range(self.controller.number_of_resource):
                self.need_matrix[i][j] = self.maximum[i][j] - self.allocation[i][j]

        allocated_instance = [0] * self.controller.number_of_resource

        for i in range(self.controller.number_of_process):
            for j in range(self.controller.number_of_resource):
                allocated_instance[j] += self.allocation[i][j]

        f = open('algorithm.txt', 'a')
        f.write(f"\n\nAllocation: {self.allocation}")
        f.write(f"\nMaximum: {self.maximum}")
        f.write(f"\nNeed Matrix: {self.need_matrix}")
        f.write(f"\n\nAllocated Resources: {allocated_instance}")

        print(f"\nAllocated Resources: {allocated_instance}")

        available = [self.dict_no_of_instance_text_var[f'no_of_instance_text_var{i}'].get() - allocated_instance[i]
                     for i in range(self.controller.number_of_resource)]

        self.set_available = [
            self.dict_no_of_instance_text_var[f'no_of_instance_text_var{i}'].get() - allocated_instance[i] for i in
            range(self.controller.number_of_resource)]

        f.write(f"\nAvailable Resources: {available}\n")
        print(f"Available Resources: {available}\n")

        running = [True] * self.controller.number_of_process
        process_sequence = [] * self.controller.number_of_process
        count = self.controller.number_of_process

        while count != 0:
            safe = False
            for i in range(self.controller.number_of_process):
                if running[i]:
                    executing = True
                    for j in range(self.controller.number_of_resource):
                        if self.need_matrix[i][j] > available[j]:
                            executing = False
                            break
                    if executing:
                        f.write(f"\nProcess {i} is executing...")
                        print(f"Process {i} is executing...")
                        process_sequence += [i]
                        running[i] = False
                        count -= 1
                        safe = True
                        for j in range(self.controller.number_of_resource):
                            available[j] += self.allocation[i][j]
                        break
            if not safe:
                self.set_safe = safe
                f.write("Deadlock: The processes are in an unsafe state.")
                print("Deadlock: The processes are in an unsafe state.")
                break

            self.set_safe = safe
            self.set_process_sequence = process_sequence

            f.write(f"\nThe processes are in a safe state.")
            f.write(f"\nAvailable Resources: {available}\n")
            f.write(f"\nProcess Sequence: {process_sequence}")

            print(f"The processes are in a safe state.")
            print(f"Available Resources: {available}\n")
            print(f"Process Sequence: {process_sequence}")

    def find_need(self):
        for i in range(self.controller.number_of_process):
            for j in range(self.controller.number_of_resource):
                self.dict_need_text_var[f'need_text_var{i}{j}'].set(self.need_matrix[i][j])

    def find_available(self):
        for j in range(self.controller.number_of_resource):
            self.dict_available_text_var[f'available_text_var{j}'].set(self.set_available[j])

    def find_safe_seq(self):
        if self.set_safe:
            for j in range(self.controller.number_of_process):
                self.dict_safe_seq_text_var[f'safe_seq_text_var{j}'].set(self.set_process_sequence[j])
        else:
            for j in range(self.controller.number_of_process):
                self.dict_safe_seq_text_var[f'safe_seq_text_var{j}'].set(0)
