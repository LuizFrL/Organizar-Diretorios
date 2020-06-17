"""
Organizador de diretórios
"""
import os

from glob import glob
from Organizar_Diretorios.Funcoes_dir.InformacoersArquivos import ArquivoInf
from typing import List, Union


class ArquivosDir(object):
    def __init__(self, diretorio_raiz: str) -> None:
        self.diretorio_raiz: str = diretorio_raiz
        self.__arquivos: List[str] = self.set_arquivos()

    def set_arquivos(self, recursive: bool = True) -> List[str]:
        self.__arquivos: List[str] = glob(self.diretorio_raiz, recursive=recursive)
        return self.__arquivos

    def set_diretorio_raiz(self, novo_diretorio: str) -> None:
        self.__init__(novo_diretorio)

    def get_arquivos_pasta(self) -> List[str]:
        return self.__arquivos

    def arquivos(self) -> List[str]:
        arquivos: List[str] = []
        for diretorio in self.__arquivos:
            if not os.path.isdir(diretorio):
                arquivos.append(diretorio)
        return arquivos

    def extensoes_diretorio(self) -> List[str]:
        extensoes: List[str] = []
        for arquivo in self.arquivos():
            extensoes.append(ArquivoInf(arquivo).extensao_arquivo())
        return self.__remove_repetidos(extensoes)

    @staticmethod
    def __remove_repetidos(lista: Union[List[str], List[int]]) -> Union[List[str], List[int]]:
        l: Union[List[str], List[int]] = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l
