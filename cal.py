import tkinter as tk

def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except Exception as e:
        resultado.set("Erro")

# Criar janela
janela = tk.Tk()
janela.title("Calculadora")

# Variável para armazenar o resultado
resultado = tk.StringVar()

# Entrada de texto
entrada = tk.Entry(janela, textvariable=resultado)
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botões numéricos e operadores
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

for i, btn in enumerate(botoes):
    tk.Button(janela, text=btn, width=5, command=lambda x=btn: entrada.insert(tk.END, x)).grid(row=i // 4 + 1, column=i % 4)

# Botão de calcular
tk.Button(janela, text='C', width=5, command=lambda: entrada.delete(0, tk.END)).grid(row=5, column=0, columnspan=2)
tk.Button(janela, text='=', width=5, command=calcular).grid(row=5, column=2, columnspan=2)

# Iniciar loop de eventos
janela.mainloop()
