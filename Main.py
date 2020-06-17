from Organizar_Diretorios.Funcoes_dir.OrganizarArquivos import OrganizarArquivos
import json
import os

from typing import Tuple, Dict, List
from tkinter import filedialog, Tk


def escolher_dir_raiz_destino() -> Tuple[str, str]:
    root: Tk = Tk()
    root.update()
    dir_raiz: str = filedialog.askdirectory(initialdir='C:/', title='Escolha a pasta a ser organizada.') + r'/**'
    dir_destino: str = filedialog.askdirectory(initialdir='C:/', title='Escolha a pasta de destino')
    root.destroy()
    return dir_raiz, dir_destino


def retornar_config() -> Dict[str, List[str]]:
    os.chdir(os.path.dirname(__file__))
    with open('config.json', 'r', encoding='utf-8') as file:
        return json.load(file)


pasta_raiz, pasta_destino = escolher_dir_raiz_destino()
arquivos: OrganizarArquivos = OrganizarArquivos(pasta_raiz, pasta_destino)
config: Dict[str, List[str]] = retornar_config()
arquivos.organizar_arquivos(config, 'Outros')
