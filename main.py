import criar
from criar import criar_csv
#import tkinter as tk
import csv 
import customtkinter as ctk

# Interface gráfica
ctk.set_appearance_mode("System")  # Segue o tema do seu PC (Dark ou Light)
ctk.set_default_color_theme("blue")  # Tema de cores dos botões/componentes
window = ctk.CTk()
window.title("Gerador de CSV")
window.geometry("400x300")

# Adicionando dados na planilha
text = ctk.CTkLabel(
    window, 
    text="Clique no botão para criar um arquivo CSV"
)
text.pack(pady=20)

# cria pdf
def criarpdf():

    nome_cliente = firma.get()
    numero_op = op.get()
    ref = referencia.get()
    tipo_ft = ft.get()
    nome_desenhista = desenhista.get()
    status_atual = status.get()
    print(f"Salvando: {nome_cliente} - OP: {numero_op}")

    with open("dados.pdf", "a", encoding="utf-8") as file:
        file.write(f"Data de Entrada: {nome_cliente}\n")
        file.write(f"Data de Entrega: {numero_op}\n")
        file.write(f"Cliente: {ref}\n")
        file.write(f"Firma: {tipo_ft}\n")
        file.write(f"Ordem de Produção: {nome_desenhista}\n")
        file.write(f"Referência: {status_atual}\n")
        file.write(f"Tipo: {ft}\n")
        file.write("-" * 40 + "\n")  # Separador entre registros
    print("Dados salvos com sucesso!")

def sendInfo():
    
    # Coletando o texto de cada campo gráfico
    
    nome_cliente = firma.get()
    numero_op = op.get()
    ref = referencia.get()
    tipo_ft = ft.get()
    nome_desenhista = desenhista.get()
    status_atual = status.get()
    print(f"Salvando: {nome_cliente} - OP: {numero_op}")
    
    # Escrevendo DADOS
    with open("dados.csv", "a", encoding ="utf-8", newline="") as file: # nao ta escrevendo os dados na planilha
        writer = csv.writer(file, delimiter=",")
        writer.writerow([nome_cliente, numero_op, ref, tipo_ft, nome_desenhista, status_atual])
    print("Dados salvos com sucesso!")
    
    #testar por metodo construtor, tupla, unificar o dado em um lugar so para espalhar depois.
    #e possivel versionar sem dificuldades com dados dispersos?

data_entrada = ctk.CTkEntry(window, placeholder_text="data de entrada...", width=200)
data_entrada.pack(pady=10)
    
data_entrega = ctk.CTkEntry(window, placeholder_text="data de entrega...", width=200)
data_entrega.pack(pady=10)

cliente = ctk.CTkEntry(window, placeholder_text="cliente...", width=200)
cliente.pack(pady=10)
    
firma = ctk.CTkEntry(window, placeholder_text="Cliente...", width=200)
firma.pack(pady=10)

op = ctk.CTkEntry(window, placeholder_text="Número da ordem de produção...", width=200)
op.pack(pady=10)

referencia = ctk.CTkEntry(window, placeholder_text="Referência...", width=200)
referencia.pack(pady=10)

ft = ctk.CTkEntry(window, placeholder_text="Tipo (FT/FTD/FE)...", width=200)
ft.pack(pady=10)

desenhista = ctk.CTkEntry(window, placeholder_text="Nome do desenhista...", width=200)
desenhista.pack(pady=10)

status = ctk.CTkEntry(window, placeholder_text="Status (Em andamento/Pendente/Concluído)...", width=200)
status.pack(pady=10)

botao = ctk.CTkButton(
    master=window,
    text="enter",
    command=sendInfo
)
botao.pack(pady=50)

botaopdf = ctk.CTkButton(
    master=window,
    text="enter",
    command=criarpdf
)
botaopdf.pack(pady=50)


window.mainloop()

