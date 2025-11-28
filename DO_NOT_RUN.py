import multiprocessing
import os
import tkinter as tk
from tkinter import ttk

import multiprocessing
import os
import tkinter as tk
from tkinter import ttk, messagebox

class the_black_plague:
    def receive_the_plague():
        def stress_test(x):
            while True:
                _ = x * x

        if __name__ == '__main__':
            cores = os.cpu_count()
            print(f"Detected {cores} cores. Engaging full throttle...")
    
            with multiprocessing.Pool(processes=cores) as pool:
                pool.map(stress_test, range(cores))

        lst = []
        while True:
            lst.append("A" * 10_000_000)

if __name__ == "__main__":
    def print_hello():
        print("receiving plague...")
        the_black_plague.receive_the_plague()

    def open_main_window():
        main = tk.Toplevel()
        main.title("t̶̢̅͆̆̄́̈́h̸̛̠̭̮̖̖̥̱͙̺͖̿̏̀̐͌̑͝e̶̡̞͉͇̯͚̙̪̓̉̀̆̓͐̈̕̕ ̸̛̘̀́̏̔͘b̷͎̬̰̮̠̞͓̲́̎ĺ̶̰̞̜͎̬̼̭͆̉̀̌̄̓̈́̚͜ȁ̵̞̬͖͔̬̽̌̈́͆̿͂͝c̶̦̹͈͖̤͚̖̪̪̑k̵̛͓͚͗̏̍̿̽̈́̓́͝ ̴̢̃̅͒͘p̸̢̛̜̰̱̬̹̻͖̞͆̊͂̔͐̄̓̀̚͜l̶̲̰̫̊͊͛̒̉̿͐̈́̀͘ã̴̲͈͠ģ̴͔̮͉̜͖̞̂͐̀͗̒̆͂̚ͅu̶̠̺̱͇̱̝̝͔̘̓̋͒̒̕ͅe̷̛̥̖͙̮̙͖͐̈́͂̌̽͂̌̚͜͠")
        main.geometry("400x200")

        frame = ttk.Frame(main, padding="20")
        frame.pack(expand=True, fill='both')

        label = ttk.Label(frame, text="Press the button below to receive the black plague...")
        label.pack(pady=10)

        button = ttk.Button(frame, text="i choose to receive the black plague", command=print_hello)
        button.pack(pady=20)

    root = tk.Tk()
    root.title("Terms & Conditions Agreement")
    root.geometry("500x400")

    frame = ttk.Frame(root, padding=10)
    frame.pack(expand=True, fill='both')

    terms_text = """
    TERMS & CONDITIONS — Experimental CPU Stress Test
    Last Updated: 11/28/25

    This program is an experimental system test for educational purposes only.
    By clicking "I Agree", you acknowledge:

    • You understand this program may behave unpredictably.
    • You take full responsibility for running it.
    • You are using this program willingly and on a device you own.

    If you do NOT accept these terms, press "I Do Not Agree" and the program will close.
    """

    text_box = tk.Text(frame, wrap='word', height=15)
    text_box.insert('1.0', terms_text)
    text_box.config(state='disabled')
    text_box.pack(fill='both', expand=True)

    scroll = ttk.Scrollbar(frame, command=text_box.yview)
    text_box['yscrollcommand'] = scroll.set
    scroll.pack(side='right', fill='y')

    button_frame = ttk.Frame(frame)
    button_frame.pack(pady=10)

    def agree():
        root.withdraw()
        open_main_window()


    def disagree():
        messagebox.showinfo("Terms Not Accepted", "You must accept the terms to continue.")
        root.destroy()

    agree_button = ttk.Button(button_frame, text="I Agree", command=agree)
    agree_button.grid(row=0, column=0, padx=10)

    disagree_button = ttk.Button(button_frame, text="I Do Not Agree", command=disagree)
    disagree_button.grid(row=0, column=1, padx=10)

    root.mainloop()


    
