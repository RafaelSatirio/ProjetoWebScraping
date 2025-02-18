import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Web Scrapping - Satirio")

# Adicionando um rótulo (label)
label = tk.Label(janela, text="Olá, mundo!")
label.pack()

# Adicionando um botão
botao = tk.Button(janela, text="Clique aqui", command=lambda: print("Botão clicado!"))
botao.pack()

# Rodando a aplicação
janela.mainloop()