from tkinter import *
from tkinter import ttk

#cores

cor1 = "#1e1f1e" #Preto
cor2 = "#feffff" #Branco
cor3 = "#38576b" #Azul escuro
cor4 = "#eceff1" #Cinza
cor5 = "#FFAB40" #Laranja

janela =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

janela.mainloop()