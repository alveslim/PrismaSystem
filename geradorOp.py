import csv
#import collections import deque

with open("generatorOp.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)
    #print(rows)
    
if rows:
    LastRow = rows[-1]
    LastRow = int(LastRow[0]) + 1
print(LastRow)
dados = LastRow
def save_csv(dados):
    """Receives a list with data and save in data.csv"""
    with open("generatorOp.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(dados)
        print("Dados salvos com sucesso!")
save_csv(dados)
            
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

    #proxima_op = banco_dados.search_NextOp() 
    #op = ctk.CTkEntry(window, placeholder_text=f"Nº da OP (Sugestão: {proxima_op})...", width=250)
    #op.pack(pady=5)