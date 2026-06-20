import os
import csv
import subprocess
import win32print
import win32api
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def search_NextOp():
    """Lê o último número de OP no ops.csv e retorna o próximo ID"""
    try:
        with open("ops.csv", "r", encoding="utf-8") as file: 
            reader = csv.reader(file)
            rows = list(reader)
            
            if rows and rows[-1]:
                last_row = rows[-1]
                return int(last_row[0]) + 1
    except (FileNotFoundError, ValueError, IndexError):
        pass 
    return 1 

def search_Op():
    with open("ops.csv", "r", encoding="utf-8") as file: 
        reader = csv.reader(file)
        return list(reader)

def imprimir_no_windows(caminho_arquivo):
    """Envia o arquivo para a impressora padrão do Windows silenciosamente"""
    print(f"Enviando '{caminho_arquivo}' para a impressora padrão do Windows...")
    # O comando ShellExecute com "print" abre o leitor de PDF em background e manda imprimir
    win32api.ShellExecute(0, "print", caminho_arquivo, None, ".", 0)
    print("Comando de impressão enviado!")

def imprimir_no_linux(caminho_arquivo):
    """Envia o arquivo para a impressora padrão no Linux/Mac"""
    print(f"Enviando '{caminho_arquivo}' para a impressora no Linux...")
    # O comando 'lp' imprime direto na impressora padrão do sistema
    subprocess.run(["lp", caminho_arquivo], check=True)
    print("Comando de impressão enviado!")

def save_csv(dados):
    """Recebe a lista de dados e salva no date.csv"""
    with open("date.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(dados)
        print("Dados salvos no CSV com sucesso!")
        
def save_pdf_fake(dados_dict):
    """Gera um arquivo PDF legítimo com os dados da OP e retorna o nome do arquivo"""
    # Usa o número da OP para dar nome ao arquivo (ex: OP_10.pdf). Se estiver vazio, usa "Sem_OP"
    numero_op = dados_dict.get('op') or "Sem_OP"
    nome_arquivo = f"OP_{numero_op}.pdf"
    
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    
    # Cabeçalho
    c.drawString(100, 750, f"ORDEM DE PRODUÇÃO - N° {numero_op}")
    c.setLineWidth(1)
    c.line(100, 735, 500, 735)
    
    c.setFont("Helvetica", 12)
    y = 700 
    
    linhas = [
        f"Data entrada: {dados_dict.get('data_entrada', '')}",
        f"Data entrega: {dados_dict.get('data_entrega', '')}",
        f"Cliente: {dados_dict.get('cliente', '')}",
        f"Firma: {dados_dict.get('firma', '')}",
        f"Referência: {dados_dict.get('referencia', '')}",
        f"Tipo: {dados_dict.get('ft', '')}",
        f"Desenhista: {dados_dict.get('desenhista', '')}",
        f"Status: {dados_dict.get('status', '')}"
    ]
    
    for linha in linhas:
        c.drawString(100, y, linha)
        y -= 25 
    
    c.save()
    print(f"PDF '{nome_arquivo}' gerado e salvo com sucesso!")
    
    # Retorna o nome do arquivo para que o main.py saiba o que mandar para a impressora
    return nome_arquivo