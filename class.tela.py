from tkinter import *

def TabuleiroOne(root):
    root.fontePadrao = ("Arial", "10")
    root.primeiroContainer = Frame()
    root.primeiroContainer["pady"] = 10
    root.primeiroContainer.pack()

def botaoIniciar(root):
    root.autenticar = Button(root)
    root.autenticar["text"] = "Autenticar"
    root.autenticar["font"] = ("Calibri", "8")
    root.autenticar["width"] = 12
  #  root.self.autenticar["command"] = #self.verificaSenha
  
root = Tk()
TabuleiroOne(root)
botaoIniciar(root)
root.mainloop()