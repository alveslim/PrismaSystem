import customtkinter as ctk
import banco_dados as banco_dados
from modelos import OrdemProducao

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Gerador de OPs")
window.geometry("400x700") # Aumentei um pouquinho a altura para caber os botões

# Label Principal
text = ctk.CTkLabel(window, text="Preencha os dados da OP abaixo:")
text.pack(pady=10)

# --- CAMPOS DE ENTRADA (GUI) ---
data_entrada = ctk.CTkEntry(window, placeholder_text="Data de entrada...", width=250)
data_entrada.pack(pady=5)
    
data_entrega = ctk.CTkEntry(window, placeholder_text="Data de entrega...", width=250)
data_entrega.pack(pady=5)

cliente = ctk.CTkEntry(window, placeholder_text="Cliente...", width=250)
cliente.pack(pady=5)
    
firma = ctk.CTkEntry(window, placeholder_text="Firma...", width=250)
firma.pack(pady=5)

proxima_op = banco_dados.search_NextOp() 
op = ctk.CTkEntry(window, placeholder_text=f"Nº da OP (Sugestão: {proxima_op})...", width=250)
op.pack(pady=5)

referencia = ctk.CTkEntry(window, placeholder_text="Referência...", width=250)
referencia.pack(pady=5)

ft = ctk.CTkEntry(window, placeholder_text="Tipo (FT/FTD/FE)...", width=250)
ft.pack(pady=5)

desenhista = ctk.CTkEntry(window, placeholder_text="Nome do desenhista...", width=250)
desenhista.pack(pady=5)

status = ctk.CTkEntry(window, placeholder_text="Status...", width=250)
status.pack(pady=5)

# --- FUNÇÕES DE DISPARO DOS BOTÕES ---
def coletar_objeto_op():
    """Função auxiliar para pegar os dados da tela e criar o objeto unificado"""
    return OrdemProducao(
        data_in=data_entrada.get(),
        data_out=data_entrega.get(),
        cliente=cliente.get(),
        firma=firma.get(),
        op=op.get(),
        referencia=referencia.get(),
        ft=ft.get(),
        desenhista=desenhista.get(),
        status=status.get()
    )
    
def action_save_csv():
    new_op = coletar_objeto_op()
    banco_dados.save_csv(new_op.for_list_csv())
        
def action_save_pdf():
    new_op = coletar_objeto_op()
    banco_dados.save_pdf_fake(new_op.for_dict())
    
def action_imprimir():
    # 1. Coleta os dados da tela
    new_op = coletar_objeto_op()
    
    # 2. Gera o PDF e guarda o nome do arquivo gerado (Ex: 'OP_5.pdf')
    nome_arquivo_gerado = banco_dados.save_pdf_fake(new_op.for_dict())
    
    # 3. Manda o arquivo exato para a impressora do Windows
    banco_dados.imprimir_no_windows(nome_arquivo_gerado)
        
# --- BOTÕES ---
botao_csv = ctk.CTkButton(master=window, text="Salvar em CSV", command=action_save_csv)
botao_csv.pack(pady=10)
    
botao_pdf = ctk.CTkButton(master=window, text="Apenas Salvar PDF", command=action_save_pdf)
botao_pdf.pack(pady=5)

# Botão de impressão agora ativado!
botao_imprimir = ctk.CTkButton(master=window, text="Salvar e Imprimir (Windows)", command=action_imprimir, fg_color="green", hover_color="darkgreen")
botao_imprimir.pack(pady=15)

window.mainloop()