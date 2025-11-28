import multiprocessing
import os
import tkinter as tk
from tkinter import ttk

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

    root = tk.Tk()

    root.title("t̶̢̅͆̆̄́̈́h̸̛̠̭̮̖̖̥̱͙̺͖̿̏̀̐͌̑͝e̶̡̞͉͇̯͚̙̪̓̉̀̆̓͐̈̕̕ ̸̛̘̀́̏̔͘b̷͎̬̰̮̠̞͓̲́̎ĺ̶̰̞̜͎̬̼̭͆̉̀̌̄̓̈́̚͜ȁ̵̞̬͖͔̬̽̌̈́͆̿͂͝c̶̦̹͈͖̤͚̖̪̪̑k̵̛͓͚͗̏̍̿̽̈́̓́͝ ̴̢̃̅͒͘p̸̢̛̜̰̱̬̹̻͖̞͆̊͂̔͐̄̓̀̚͜l̶̲̰̫̊͊͛̒̉̿͐̈́̀͘ã̴̲͈͠ģ̴͔̮͉̜͖̞̂͐̀͗̒̆͂̚ͅu̶̠̺̱͇̱̝̝͔̘̓̋͒̒̕ͅe̷̛̥̖͙̮̙͖͐̈́͂̌̽͂̌̚͜͠")


    root.geometry("400x200") # Set a fixed size for the window

    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(expand=True, fill='both')

    #Label
    label = ttk.Label(main_frame, text="Press the button below to receive the black plague...")
    label.pack(pady=10)

    button = ttk.Button(
        main_frame,
        text="i choose to receive the black plague",
        command=print_hello
    )
    button.pack(pady=20)

    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    label.pack()
    button.pack()

    root.mainloop()

    
