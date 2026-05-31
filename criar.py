import csv
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
    