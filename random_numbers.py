from tkinter import *
import random
import string

number = random.randrange(0, 9)


def display(text):
    def loop():
        global number
        number = random.randrange(0, 2)
        if (number is 1):
            text.insert(CURRENT, ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)))
        else:
            text.insert(CURRENT, ' ')

        text.after(10, loop)

    loop()


root = Tk()
root.title("Code Sushi")

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text = Text(root, width=45, height=20, bg='#000000', fg='#0099BC')
text.pack(side=TOP, fill=BOTH, expand=1)

scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

display(text)
root.mainloop()
