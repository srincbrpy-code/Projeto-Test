import tkinter as tk

#cores
COR_FUNDO = "#1E1E1E"
COR_TEXTO = "#FFFFFF"
COR_BOTAO = "#FFFFFF"
COR_BOTAO2 = "#FFBB00"
COR_BOTAO_TEXTO = "#5F5F5F"

janela = tk.Tk()
janela.title("Calculadora Primata")
janela.geometry("235x318")
janela.resizable(False, False)

frame_tela = tk.Frame(janela, width=235, height=50, bg=COR_FUNDO)
frame_tela.grid(row=0, column=0)

frame_botoes = tk.Frame(janela, width=235, height=268)
frame_botoes.grid(row=1, column=0)

#calculo
def entrar_valores(event):
    text = command=eval("app_label['text'] + str(event)")
    app_label['text'] = text



#terminal
def limpar():
    app_label['text'] = ""

app_label = tk.Label(frame_tela, text="", width=16, height=2, padx=7, relief=tk.FLAT, anchor="e", justify="right", font=("Ivy 18"), bg=COR_FUNDO, fg=COR_TEXTO)
app_label.place(x=0, y=0)

#botões
b_1 = tk.Button(frame_botoes, text="C", width=11, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=limpar, font=("Ivy 13 bold"))
b_1.place(x=0, y=0)
b_2 = tk.Button(frame_botoes, text="%", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("%"), font=("Ivy 13 bold"))
b_2.place(x=118, y=0)
b_3 = tk.Button(frame_botoes, text="/", width=5, height=2, bg=COR_BOTAO2, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("/"), font=("Ivy 13 bold"))
b_3.place(x=177, y=0)
b_4 = tk.Button(frame_botoes, text="7", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("7"), font=("Ivy 13 bold"))
b_4.place(x=0, y=53)
b_5 = tk.Button(frame_botoes, text="8", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("8"), font=("Ivy 13 bold"))
b_5.place(x=59, y=53)
b_6 = tk.Button(frame_botoes, text="9", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("9"), font=("Ivy 13 bold"))
b_6.place(x=118, y=53)
b_7 = tk.Button(frame_botoes, text="*", width=5, height=2, bg=COR_BOTAO2, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("*"), font=("Ivy 13 bold"))
b_7.place(x=177, y=53)
b_8 = tk.Button(frame_botoes, text="4", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("4"), font=("Ivy 13 bold"))
b_8.place(x=0, y=106)
b_9 = tk.Button(frame_botoes, text="5", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("5"), font=("Ivy 13 bold"))
b_9.place(x=59, y=106)
b_10 = tk.Button(frame_botoes, text="6", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("6"), font=("Ivy 13 bold"))
b_10.place(x=118, y=106)
b_11 = tk.Button(frame_botoes, text="-", width=5, height=2, bg=COR_BOTAO2, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("-"), font=("Ivy 13 bold"))
b_11.place(x=177, y=106)
b_12 = tk.Button(frame_botoes, text="1", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("1"), font=("Ivy 13 bold"))
b_12.place(x=0, y=159)
b_13 = tk.Button(frame_botoes, text="2", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("2"), font=("Ivy 13 bold"))
b_13.place(x=59, y=159)
b_14 = tk.Button(frame_botoes, text="3", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("3"), font=("Ivy 13 bold"))
b_14.place(x=118, y=159)
b_15 = tk.Button(frame_botoes, text="+", width=5, height=2, bg=COR_BOTAO2, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("+"), font=("Ivy 13 bold"))
b_15.place(x=177, y=159)
b_16 = tk.Button(frame_botoes, text="0", width=11, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("0"), font=("Ivy 13 bold"))
b_16.place(x=0, y=212)
b_17 = tk.Button(frame_botoes, text=".", width=5, height=2, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, command=lambda: entrar_valores("."), font=("Ivy 13 bold"))
b_17.place(x=118, y=212)
b_18 = tk.Button(frame_botoes, text="=", width=5, height=2, bg=COR_BOTAO2, fg=COR_BOTAO_TEXTO, font=("Ivy 13 bold"))
b_18.place(x=177, y=212)

def calcular():
    expressao = app_label['text']
    try:
        resultado = str(eval(expressao))
        app_label['text'] = resultado
    except:
        app_label['text'] = "Erro"
b_18.config(command=calcular)

def limpar():
    app_label['text'] = ""
janela.mainloop()