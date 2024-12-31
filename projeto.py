# Janela para selecionar a past do nosso computador 
import os
from tkinter.filedialog import askdirectory
import shutil

pasta_selecionada = askdirectory()
print(pasta_selecionada)

lista_arquivos = os.listdir(pasta_selecionada)
print(lista_arquivos)

# Fazer o backup dos arquivos que estão nessa pasta
nome_pasta_backup = "Backup"
nome_completo_pasta_backup = f"{pasta_selecionada}/{nome_pasta_backup}"
if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)
    
for arquivo in lista_arquivos:
    print(arquivo)
    nome_completo = f"{pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{arquivo}"
    if "." in arquivo:
        shutil.copy2(nome_completo, nome_final_arquivo)
    elif "Backup" != arquivo:
        shutil.copytree(nome_completo, nome_final_arquivo)
