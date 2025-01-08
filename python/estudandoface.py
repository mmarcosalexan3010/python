import tkinter as tk

def estudando_aparencia():
    label.config(text='sei la pow ')

root = tk.Tk()
root.title('testando alguma prr')

button = tk.Button(root, text='clica aqui vagabundo', command=estudando_aparencia)
button.pack()

label = tk.Label(root, text='')
label.pack()

root.mainloop()