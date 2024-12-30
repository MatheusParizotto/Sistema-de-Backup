# Janela para selecionar a past do nosso computador 
import os
from tkinter.filedialog import askdirectory

pasta_selecionada = askdirectory()
print(pasta_selecionada)

lista_arquivos = os.listdir(pasta_selecionada)
print(lista_arquivos)

# Fazer o backup dos arquivos que estão nessa pasta

for arquivo in lista_arquivos:
    nome_completo = f"{pasta_selecionada}/{arquivo}"
    print(nome_completo)
