import tkinter as tk

# Função para capturar o texto digitado
def capturar_texto():
    texto_digitado = entrada.get()  # Captura o texto da caixa de entrada
    rotulo_resultado.config(text=f"Você digitou: {texto_digitado}")  # Exibe o texto em um rótulo
    print(f"Texto digitado: {texto_digitado}")  # Exibe o texto no terminal

# Criando a janela principal
janela = tk.Tk()
janela.title("Exemplo de Entrada de Texto")

# Adicionando um rótulo (label) para instruções
rotulo_instrucao = tk.Label(janela, text="Digite algo:")
rotulo_instrucao.pack(pady=3)  # Adiciona espaço vertical

# Adicionando uma caixa de entrada (Entry)
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=10)

# Adicionando um botão para capturar o texto
botao = tk.Button(janela, text="Enviar", command=capturar_texto)
botao.pack(pady=5)

# Adicionando um rótulo para exibir o resultado
rotulo_resultado = tk.Label(janela, text="")
rotulo_resultado.pack(pady=10)

# Rodando a aplicação
janela.mainloop()