"""

prime displayer using tkinter

Author : Raj Patra

Version 1.0

"""

try:  # python2 imports
    from Tkinter import *
except ImportError:  # python3 failed, try python2 imports
    from tkinter import *

number = 2


def isPrime(number):
    for i in range(2, number):
        if(number % i) == 0:
            return False

    return True


def prime_text(text):
    def count():
        global number
        if isPrime(number):
            text.insert(END, str(number)+',')
            number += 1
            text.after(1, count)
        else:
            number += 1
            text.after(1, count)
    count()


root = Tk()
root.title("Displaying primes")

label = Label(root, text="PRIME NUMBERS...", bg='black', fg='white', font=('Algerian', 20))
label.pack(side=TOP, fill=X)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text = Text(root, width=55, height=15, bg='black', fg='white')
text.pack(side=TOP, fill=BOTH, expand=1)

scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

prime_text(text)
button = Button(root, text="Start")
button.pack(side=LEFT, fill=X)
button1 = Button(root, text="Stop", command=root.destroy)
button1.pack(side=RIGHT, fill=X)

root.mainloop()