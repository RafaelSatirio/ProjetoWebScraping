import tkinter as tk

def capturar_link():
    link_digitado = input_link.get()

# Criando a Janela principal
janela = tk.Tk()
janela.title("Web Scrapping - Satirio")

# Adicionando um Rótulo
label = tk.Label(janela, text="Extração de Dados - Project")
label.pack()

rotulo_link = tk.Label(janela, text="Digite o link que deseja Extrair Dados")
rotulo_link.pack(pady=10)

input_link = tk.Entry(janela, width=30)
input_link.pack(pady=5)

# Rodando a aplicação
janela.mainloop()