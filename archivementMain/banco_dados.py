import os
# import subprocess
import os
import csv
# import win32print
# import win32api

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

def search_Op():
        with open("ops.csv", "r", encoding="utf-8") as file: 
            reader = csv.reader(file)
            rows = list(reader)
            return rows
        
# def imprimir_no_linux(caminho_arquivo, nome_trabalho="Documento"):

#     # 1. Listar e escolher a impressora (Opcional se quiser usar a padrão)
#     # Para listar as impressoras no terminal do Ubuntu, você usaria o comando: lpstat -p -d
#     # Se você omitir o nome da impressora no comando, o Linux usa a impressora padrão do sistema automaticamente.
#     NOME_IMPRESSORA = "Sua_Impressora_Aqui"  # Substitua pelo nome exato da impressora no CUPS

#     # 2. Pasta com os arquivos
#     caminho = "/home/usuario/Desktop/Imprimir"  # Lembre-se de ajustar para o padrão de caminhos do Linux
#     lista_arquivos = os.listdir(caminho)

#     # 3. Mandar imprimir cada arquivo
#     for arquivo in lista_arquivos:
#         # Cria o caminho completo do arquivo
#         caminho_completo = os.path.join(caminho, arquivo)
        
#         # Ignora pastas, foca apenas em arquivos
#         if os.path.isfile(caminho_completo):
#             print(f"Enviando para impressão: {arquivo}")
            
#             # Se você quiser usar a impressora padrão do sistema:
#             comando = ["lp", caminho_completo]
            
#             # Se você quiser especificar uma impressora exata (Equivalente ao SetDefaultPrinter):
#             # comando = ["lp", "-d", NOME_IMPRESSORA, caminho_completo]
            
#             # Executa o comando de impressão do Linux
#             subprocess.run(comando, check=True)

# def imprimir_no_windows(caminho_arquivo):
#     # Listar impressoras disponíveis
#     lista_impressoras = win32print.EnumPrinters(2)
#     for idx, impressora in enumerate(lista_impressoras):
#         print(f"{idx}: {impressora[2]}")

#     # Escolher a impressora (Aqui você pode implementar uma lógica para escolher a impressora desejada)
#     escolha = int(input("Digite o número da impressora que deseja usar: "))
#     impressora_escolhida = lista_impressoras[escolha][2]

#     # Definir a impressora escolhida como padrão
#     win32print.SetDefaultPrinter(impressora_escolhida)

#     # Enviar o arquivo para impressão
#     win32api.ShellExecute(0, "print", caminho_arquivo, None, ".", 0)

#     # escolher qual impressora a gente vai querer usar
#     lista_impressoras = win32print.EnumPrinters(2)
#     impressora = lista_impressoras[4]

#     win32print.SetDefaultPrinter(impressora[2])

#     # mandar imprimir todos os arquivos de uma pasta
#     caminho = r"C:\Users\Python\Desktop\Imprimir Automaticamente com Python\Imprimir"
#     lista_arquivos = os.listdir(caminho)

#     # https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
#     for arquivo in lista_arquivos:
#         win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)

def save_csv(dados):
    """Receives a list with data and save in data.csv"""
    with open("date.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(dados)
        print("Dados salvos com sucesso!")
        
def save_pdf_fake(dados_dict):
    """Receive a dict and save simulate a repository of text/pdf"""
    with open("data.pdf", "a", encoding="utf-8") as file:
        # Usando .get() o código não trava mesmo se a chave sumir ou mudar de nome
        file.write(f"Data entrada: {dados_dict.get('data_entrada', '')}\n")
        file.write(f"Data entrega: {dados_dict.get('data_entrega', '')}\n")
        file.write(f"Client: {dados_dict.get('cliente', '')}\n")
        file.write(f"Firma: {dados_dict.get('firma', '')}\n")
        file.write(f"Ordem de Produção: {dados_dict.get('op', '')}\n")
        file.write(f"Referência: {dados_dict.get('referencia', '')}\n")
        file.write(f"Tipo: {dados_dict.get('ft', '')}\n")
        file.write(f"Desenhista: {dados_dict.get('desenhista', '')}\n")
        file.write(f"Status: {dados_dict.get('status', '')}\n")
        file.write("-" * 40 + "\n")
    print("Dados salvos no PDF com sucesso")