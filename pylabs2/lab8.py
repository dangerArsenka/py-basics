#'Introduction to programming':Task 8.2
#Tsadzikidze Arsen, FB-24, 26
print('Introduction to programming:Task 8.2')
print('Tsadzikidze Arsen, FB-24, 26')

import tkinter as tk

class BaseCounter:
    def __init__(self, master):
        self.master = master
        self.master.title("Base Counter")

        # Create label and textbox
        self.label_bases = tk.Label(master, text="Bases:")
        self.label_bases.grid(row=0, column=0, padx=5, pady=5, sticky="W")
        self.textbox_bases = tk.Entry(master, width=50)
        self.textbox_bases.grid(row=0, column=1, padx=5, pady=5)

        # Create buttons
        self.button_clear = tk.Button(master, text="Clear", command=self.clear_fields)
        self.button_clear.grid(row=1, column=0, padx=5, pady=5)

        self.button_count = tk.Button(master, text="Count", command=self.count_bases)
        self.button_count.grid(row=1, column=1, padx=5, pady=5)

        self.button_goodbye = tk.Button(master, text="Goodbye", command=master.quit)
        self.button_goodbye.grid(row=1, column=2, padx=5, pady=5)

        # Create labels for displaying counts
        self.label_A = tk.Label(master, text="A: 0")
        self.label_A.grid(row=2, column=0, padx=5, pady=5, sticky="W")

        self.label_T = tk.Label(master, text="T: 0")
        self.label_T.grid(row=3, column=0, padx=5, pady=5, sticky="W")

        self.label_C = tk.Label(master, text="C: 0")
        self.label_C.grid(row=4, column=0, padx=5, pady=5, sticky="W")

        self.label_G = tk.Label(master, text="G: 0")
        self.label_G.grid(row=5, column=0, padx=5, pady=5, sticky="W")

    def clear_fields(self):
        self.textbox_bases.delete(0, tk.END)
        self.label_A.config(text="A: 0")
        self.label_T.config(text="T: 0")
        self.label_C.config(text="C: 0")
        self.label_G.config(text="G: 0")

    def count_bases(self):
        bases = self.textbox_bases.get().upper()
        a_count = bases.count('A')
        t_count = bases.count('T')
        c_count = bases.count('C')
        g_count = bases.count('G')

        # Update labels with counts
        self.label_A.config(text=f"A: {a_count}")
        self.label_T.config(text=f"T: {t_count}")
        self.label_C.config(text=f"C: {c_count}")
        self.label_G.config(text=f"G: {g_count}")

root = tk.Tk()
app = BaseCounter(root)
root.mainloop()

