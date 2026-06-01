import csv 

def search_NextOp():
    """Read last number of OP the archive ops.csv and return next id"""
    """L> idea for read own main csv"""
    try:
        with open("ops.csv", "r", encoding="utf-8") as file: 
            reader = csv.reader(file)
            rows = list(reader)
            
            if rows and rows[-1]:
                last_row = rows[-1]
                return int(last_row[0]) + 1
    except (FileNotFoundError, ValueError, IndexError):
        pass 
    return 1 # Return 1 if archivement not exist, if empty or fails

def save_csv(dados):
    """Receives a list with data and save in data.csv"""
    with open("date.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(dados)
        print("Dados salvos com sucesso!")
        
def save_pdf_fake(dados_dict):
    """Receive a dict and save simulate a repository of text/pdf"""
    with open("data.pdf", "a", encoding="utf-8") as file:
        file.write(f"Data entrada: {dados_dict['data_entrada']}\n")
        file.write(f"Data entrega: {dados_dict['data_entrega']}\n")
        file.write(f"Client: {dados_dict['client']}\n")
        file.write(f"Firma: {dados_dict['firma']}\n")
        file.write(f"Ordem de Produção: {dados_dict['op']}\n")
        file.write(f"Referência: {dados_dict['referencia']}\n")
        file.write(f"Tipo: {dados_dict['ft']}\n")
        file.write(f"Desenhista: {dados_dict['desenhista']}\n")
        file.write(f"Status: {dados_dict['status']}\n")
        file.write("-" * 40 + "\n")
    print("Dados salvos no PDF com sucesso")