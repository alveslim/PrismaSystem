with open("dados.csv", "r", encoding="utf-8") as file:
    for line in file: 
        row = line.rstrip().split(",") #remove o \n e separa por vírgula e guarda em uma lista(linha
        print(f"date: {row[1]} - delivery date: {row[1]}")

        
