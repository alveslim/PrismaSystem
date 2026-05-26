import csv

def criar_csv():
    data_entrada = input("Digite a data de entrada (YYYY-MM-DD): ")
    data_entrega = input("Digite a data de entrega (YYYY-MM-DD): ")
    cliente = input("Digite o nome do cliente: ")
    firma = input("Digite o nome da firma: ")
    op = input("Digite o número da ordem de produção: ")
    referencia = input("Digite a referência: ")
    ft = input("Digite o tipo (FT/FTD/FE): ")   
    desenhista = input("Digite o nome do desenhista: ")
    status = input("Digite o status (Em andamento/Pendente/Concluído): ")
    
    with open("dados.csv", "a", encoding ="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow([data_entrada, data_entrega, cliente, firma, op, referencia, ft, desenhista, status])
    print("Dados salvos com sucesso!")

def criar_txt():
    data_entrada = input("Digite a data de entrada (YYYY-MM-DD): ")
    data_entrega = input("Digite a data de entrega (YYYY-MM-DD): ")
    cliente = input("Digite o nome do cliente: ")
    firma = input("Digite o nome da firma: ")
    op = input("Digite o número da ordem de produção: ")
    referencia = input("Digite a referência: ")
    ft = input("Digite o tipo (FT/FTD/FE): ")   
    desenhista = input("Digite o nome do desenhista: ")
    status = input("Digite o status (Em andamento/Pendente/Concluído): ")

    with open("dados.txt", "a", encoding="utf-8") as file:
        file.write(f"Data de Entrada: {data_entrada}\n")
        file.write(f"Data de Entrega: {data_entrega}\n")
        file.write(f"Cliente: {cliente}\n")
        file.write(f"Firma: {firma}\n")
        file.write(f"Ordem de Produção: {op}\n")
        file.write(f"Referência: {referencia}\n")
        file.write(f"Tipo: {ft}\n")
        file.write(f"Desenhista: {desenhista}\n")
        file.write(f"Status: {status}\n")
        file.write("-" * 40 + "\n")  # Separador entre registros
    print("Dados salvos com sucesso!")
