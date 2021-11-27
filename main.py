from tkinter import *
from tkinter import Tk
from tkinter import messagebox


# cores -----------------------------
cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters


janela=Tk()
janela.title('')
janela.geometry('310x300')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief='flat')
frame_baixo.grid(row=1, column=0,  sticky=NSEW)

l_nome= Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25 bold'), bg=cor1, fg=cor4)
l_nome.place(x=5, y=5)

l_linha= Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1 bold'), bg=cor2, fg=cor4)
l_linha.place(x=10, y=45)


credenciais = ['Joao', '123456789']

def verifica_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin': 
        messagebox.showinfo('Login', 'Seja bem vindo Admin! ')
    elif credenciais [0] == nome and credenciais [1] == senha:
         messagebox.showinfo('Login ', 'Seja bem vindo de volta! ' + credenciais[0])

         for widget in frame_baixo.winfo_children():
            widget.destroy()

         for widget in frame_cima.winfo_children():
            widget.destroy()

         nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha')

def nova_janela():
    l_nome= Label(frame_cima, text='USUARIO : ' + credenciais[0], anchor=NE, font=('Ivy 20 bold'), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=5)

    l_linha= Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1 bold'), bg=cor2, fg=cor4)
    l_linha.place(x=10, y=45)

    l_nome= Label(frame_baixo, text='Seja bem vindo' + credenciais[0], anchor=NE, font=('Ivy 20 bold'), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=105)


l_nome= Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_pass= Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)


b_confirmar= Button(frame_baixo, command=verifica_senha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=cor2, fg=cor1, relief='raised', overrelief=RIDGE)
b_confirmar.place(x=15, y=180)




janela.mainloop()