"""
Organizador de diretórios
"""
import os
from glob import glob
from Organizar_Diretorios.Funcoes_dir.InformacoersArquivos import ArquivoInf


class ArquivosDir(object):
    def __init__(self, diretorio_raiz):
        self.diretorio_raiz = diretorio_raiz
        self.__arquivos = self.set_arquivos()

    def set_arquivos(self, recursive=True):
        self.__arquivos = glob(self.diretorio_raiz, recursive=recursive)
        return self.__arquivos

    def set_diretorio_raiz(self, novo_diretorio):
        self.__init__(novo_diretorio)

    def get_arquivos_pasta(self):
        return self.__arquivos

    def arquivos(self):
        arquivos = []
        for diretorio in self.__arquivos:
            if not os.path.isdir(diretorio):
                arquivos.append(diretorio)
        return arquivos

    def extensoes_diretorio(self):
        extensoes = []
        for arquivo in self.arquivos():
            extensoes.append(ArquivoInf(arquivo).extensao_arquivo())
        return self.__remove_repetidos(extensoes)

    @staticmethod
    def __remove_repetidos(lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l
