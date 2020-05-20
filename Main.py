from Organizar_Diretorios.Funcoes_dir.OrganizarArquivos import OrganizarArquivos
import json, os
from tkinter import filedialog
from tkinter import *


def escolher_dir_raiz_destino():
    root = Tk()
    root.update()
    dir_raiz = filedialog.askdirectory(initialdir='C:/', title='Escolha a pasta a ser organizada.') + r'/**'
    dir_destino = filedialog.askdirectory(initialdir='C:/', title='Escolha a pasta de destino')
    root.destroy()
    return dir_raiz, dir_destino


def retornar_config():
    os.chdir(os.path.dirname(__file__))
    with open('config.json', 'r', encoding='utf-8') as file:
        return json.load(file)


pasta_raiz, pasta_destino = escolher_dir_raiz_destino()
arquivos = OrganizarArquivos(pasta_raiz, pasta_destino)
config = retornar_config()
arquivos.organizar_arquivos(config, 'Outros')
