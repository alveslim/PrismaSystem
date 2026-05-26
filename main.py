import criar
from criar import criar_csv
import tkinter as tk
import customtkinter as ctk

# lendo csv
with open("dados.csv", "r", encoding="utf-8") as file:
    for line in file: 
        row = line.rstrip().split(",") #remove o \n e separa por vírgula e guarda em uma lista(linha
        print(f"date: {row[1]} - delivery date: {row[1]}")

# Interface gráfica
ctk.set_appearance_mode("System")  # Segue o tema do seu PC (Dark ou Light)
ctk.set_default_color_theme("blue")  # Tema de cores dos botões/componentes
window = ctk.CTk()
window.title("Gerador de CSV")
window.geometry("400x300")

# Botão para criar CSV  # ainda nao funciona(ideia de atualizar a planilha em tempo real)
text = ctk.CTkLabel(
    window, 
    text="Clique no botão para criar um arquivo CSV"
)
text.pack(pady=20)

# Botão para criar CSV
campo_texto = ctk.CTkEntry(
    window, 
    placeholder_text="Digite seu nome...", # Texto fantasma
    width=200                              # Largura do campo
)
campo_texto.pack(pady=10)

window.mainloop()

