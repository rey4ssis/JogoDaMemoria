from tkinter import *


import random

tabuleiroPrincipal=[[],[],[],[]]

mylist = ['!','@','#','$','%','*','~','?','!','@','#','$','%','*','~','?']
listVisual=[['@', '*', '?', '#'], ['~', '$', '$', '~'], ['%', '@', '?', '%'], ['!', '#', '*', '!']]
random.shuffle(mylist)

for i in mylist:
  for listAp in tabuleiroPrincipal:
    if len(listAp)<=3:
      listAp.append(i)
      break

def Visualizar():
  for i in listVisual:
    print(i)



def tentativa(list):
  for j in tabuleiroPrincipal:
    print(j)


  op1=input("Digite a opção 1:")
  p2=input("Digite a opção 2:")

#   tentativa(list)
# Visualizar()

janela = Tk()
janela.geometry("400x400")
janela.minsize(400, 400) 
janela.maxsize(400, 400) 
janela.title("Joguinho da Mémoria")
texto = Label(janela, text="dfsgkjanlfgnjafskjlngakjdlfngkjdfngn")
texto.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="gzdfzgdfgzdfgdgzdgf")
texto_resposta.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="Clique aqui para iniciar o jogo")
botao.grid(column=0, row=2, padx=10, pady=10)
janela.mainloop()