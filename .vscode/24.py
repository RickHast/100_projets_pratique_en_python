from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, yscrollcommand=scrollbar.set)
text.insert(END, "Texte très long...\n" * 50)
text.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=text.yview)

root.mainloop()