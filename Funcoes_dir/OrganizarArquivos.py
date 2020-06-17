import os
import shutil

from typing import Dict, List, Set
from Organizar_Diretorios.Funcoes_dir.Diretorio import ArquivosDir
from Organizar_Diretorios.Funcoes_dir.InformacoersArquivos import ArquivoInf


class OrganizarArquivos(ArquivosDir):
    def __init__(self, diretorio_raiz, diretorio_destino):
        ArquivosDir.__init__(self, diretorio_raiz)
        self.diretorio_destino = diretorio_destino

    def __organizar_lista_arquivos(self, config: Dict[str, List[str]] = None,
                                   pasta_nao_regis: str = '') -> Dict[str, List[str]]:
        if config is None:
            config: Dict[str, List[str]] = {
                        'Imagens': ['.jpeg', '.png', '.jpg', '.gif', '.bmp'],
                        'Videos': ['.mp4', '.mkv', '.amv'],
                        'Documentos': ['.docx', '.pdf', '.xlsx', '.csv', '.xltx', '.xls', '.txt'],
                  }

        lista_arquivos: Dict[str, List[str]] = {}

        for key in config.keys():
            lista_arquivos[key] = []

        arquivos_lidos: List[str] = []
        todos_arquivos: Set[str] = set(self.arquivos())

        for arquivo in todos_arquivos:
            arq: ArquivoInf = ArquivoInf(arquivo)
            for pasta, extensoes in config.items():
                for extensao in extensoes:
                    if extensao.lower().find(arq.extensao_arquivo()) != -1:
                        lista_arquivos[pasta].append(arquivo)
                        arquivos_lidos.append(arquivo)

        if pasta_nao_regis:
            if lista_arquivos.get(pasta_nao_regis):
                pasta_nao_regis += '(1) - Cópia'
            arquivos_nao_registrados: Set[str] = todos_arquivos.difference(set(arquivos_lidos))
            lista_arquivos[pasta_nao_regis] = list(arquivos_nao_registrados)
        return lista_arquivos

    def organizar_arquivos(self, config: Dict[str, List[str]] = None,
                           pasta_nao_regis: str = '', conservar_pastas: bool = True) -> None:

        arquivos_organizados: Dict[str, List[str]] = self.__organizar_lista_arquivos(
            config,
            pasta_nao_regis
        )

        for pasta, arquivos in arquivos_organizados.items():
            nova_pasta: str = self.diretorio_destino + r'\{}'.format(pasta)
            for arquivo in arquivos:
                arquivo_nome: str = os.path.basename(arquivo)
                if conservar_pastas:
                    arquivo_nome: str = arquivo.replace(self.diretorio_raiz[0:-3:], '')[1::]
                novo_arquivo: str = nova_pasta + r'\{}'.format(arquivo_nome)
                novo_dir: str = os.path.dirname(novo_arquivo)
                if not os.path.exists(novo_dir):
                    os.makedirs(novo_dir)
                shutil.move(arquivo, novo_arquivo)
                print(f"""Arquivo: {os.path.basename(arquivo)}
De: {arquivo}
Para: {novo_arquivo}
""")
