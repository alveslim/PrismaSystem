import csv
def search_Op():
        with open("op.csv", "r", encoding="utf-8") as file: 
            reader = csv.reader(file)
            rows = list(reader)
            print(rows)
search_Op()