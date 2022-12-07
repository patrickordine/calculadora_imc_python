import sqlite3
import tkinter
from tkinter import *

c1='#A5D8FF'
c2='#ffffff'

root = Tk()
class app():
    def __init__(self):
        self.root = root
        self.janela()
        self.frame()
        root.mainloop()
    def janela(self):
        self.root.title("Calculadora de IMC - índice de Massa Corporal")
        self.root.configure(bg=c1)
        self.root.geometry("480x250")
        self.root.resizable(False, False)

    def frame(self):
        self.nome = StringVar()
        self.label_nome = Label(text='Nome do Paciente', bg=c1)
        self.label_nome.place(relx=0.015, rely=0.015)

        self.in_nome = Entry(textvariable=self.nome)
        self.in_nome.place(relx=0.26, rely=0.015, relwidth=0.7)

        self.endereco = StringVar()
        self.label_endereco = Label(text='Endereço Completo', bg=c1)
        self.label_endereco.place(relx=0.015, rely=0.115)

        self.in_endereco = Entry(textvariable=self.endereco)
        self.in_endereco.place(relx=0.26, rely=0.115, relwidth=0.7)

        self.altura = DoubleVar()
        self.label_altura = Label(text='Altura (cm)', bg=c1)
        self.label_altura.place(relx=0.015, rely=0.215)

        self.in_altura = Entry(textvariable=self.altura, justify=RIGHT)
        self.in_altura.place(relx=0.26, rely=0.215)

        self.peso = DoubleVar()
        self.label_peso = Label(text='Peso(Kg)', bg=c1)
        self.label_peso.place(relx=0.015, rely=0.315)

        self.in_peso = Entry(textvariable=self.peso, justify=RIGHT)
        self.in_peso.place(relx=0.26, rely=0.315)

        self.imc = StringVar()
        self.lb_imc = Label(textvariable=self.imc)
        self.resultado = Label(textvariable=self.imc, bg=c2)
        self.resultado.place(relx=0.55, rely=0.215, relwidth=0.41, relheight=0.3)

        botao1 = tkinter.Button(text='Calcular', command=self.btn_click)
        botao1.place(relx=0.26, rely=0.7, relwidth=0.2)

        botao2 = tkinter.Button(text='Reiniciar', command=self.btn_reiniciar)
        botao2.place(relx=0.46, rely=0.7, relwidth=0.2)

        botao3 = tkinter.Button(text='Sair', command=root.destroy)
        botao3.place(relx=0.76, rely=0.7, relwidth=0.2)

    def btn_click(self):

        con = sqlite3.connect("bddados.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS dados(nome TEXT, endereco TEXT, altura INTEGER,peso INTEGER)")
        cur.execute("INSERT INTO dados(nome, endereco, altura, peso) VALUES (?,?,?,?)",
                    (self.nome.get(), self.endereco.get(), self.altura.get(), self.peso.get()))
        con.commit()

        p = self.peso.get()
        a = (self.altura.get())/100
        resultadoimc = p/(a*a)

        if resultadoimc < 16.99:
            situacao = '%0.2f - ' %(resultadoimc) + 'Muito abaixo do peso'
        elif resultadoimc < 18.5:
            situacao = '%0.2f - ' %(resultadoimc) + 'Abaixo do peso'
        elif resultadoimc < 25:
            situacao = '%0.2f - ' %(resultadoimc) + 'Peso normal'
        elif resultadoimc < 30:
            situacao = '%0.2f - ' %(resultadoimc) + 'Acima do peso'
        elif resultadoimc < 35:
            situacao = '%0.2f - ' %(resultadoimc) + 'Obesidade I'
        elif resultadoimc < 40:
            situacao = '%0.2f - ' %(resultadoimc) + 'Obesidade II (severa)'
        else:
            situacao = '%0.2f - ' %float(resultadoimc) + 'Obesidade III (mórbida)'
        return self.imc.set(situacao)

    def btn_reiniciar(self):
        app()

app()
