import tkinter as tk
from tkinter import ttk

def inverter_palavra():
    # Obtém o texto digitado pelo usuário
    palavra = entrada.get()
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    # Exibe a palavra invertida
    resultado_label.config(text=f"Palavra invertida: {palavra_invertida}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Inversor de Palavras")
janela.geometry("400x300")
janela.configure(bg="#FFD700")  # Fundo dourado

# Título do aplicativo
titulo = tk.Label(
    janela,
    text="INVERSOR DE PALAVRAS",
    font=("Arial Black", 16),
    bg="#FFD700",
    fg="#8B0000"
)
titulo.pack(pady=10)

# Frame para centralizar os widgets
frame = tk.Frame(janela, bg="#FFD700")
frame.pack(pady=10)

# Label para instrução
instrucao = tk.Label(
    frame,
    text="Digite uma palavra:",
    font=("Arial", 12),
    bg="#FFD700",
    fg="#000080"
)
instrucao.grid(row=0, column=0, padx=10, pady=10)

# Caixa de texto para entrada do usuário
entrada = ttk.Entry(frame, width=20, font=("Arial", 12))
entrada.grid(row=0, column=1, padx=10, pady=10)

# Botão para executar a inversão
botao = tk.Button(frame, text="Inverter", command=inverter_palavra, font=("Arial",14,"bold"), bg="purple", fg="greenyellow")
botao.grid(row=1, column=0, columnspan=2, pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(
    janela,
    text="",
    font=("Arial", 14),
    bg="#FFD700",
    fg="#006400"
)
resultado_label.pack(pady=20)

# Loop da interface gráfica
janela.mainloop()
