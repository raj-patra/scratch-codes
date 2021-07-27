__author__ = "github.com/raj-patra"

from tkinter import *
import random, string, time

start = time.time()

def display(text):
    def loop():
        global start
        if (time.time()-start) > 10:
            start = time.time()
            text.delete('1.0', END)
        text.insert(CURRENT, ''.join(random.choice(string.printable)))
        text.after(1, loop)

    loop()

root = Tk()
root.title("Code Sushi")

"""Uncomment to enable scrollbar"""
# scroll = Scrollbar(root)
# scroll.pack(side=RIGHT, fill=Y)
# scroll.config(command=text.yview)
# text.config(yscrollcommand=scroll.set)

text = Text(root, width=130, height=30, bg='#111111', fg='#39FF14')
text.pack(side=TOP, fill=BOTH, expand=1)

display(text)
root.mainloop()
