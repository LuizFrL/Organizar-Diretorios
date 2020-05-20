import os


class ArquivoInf(object):
    def __init__(self, diretorio):
        self.diretorio = diretorio
        self.__status_arquivos = os.stat(self.diretorio)
        self.tamanho = self.__status_arquivos.st_size
        self.data_de_modificacao = self.__status_arquivos.st_ctime
        self.data_acesso_recente = self.__status_arquivos.st_atime
        self.nome_arquivo = os.path.basename(self.diretorio)
        self.extensao = self.extensao_arquivo()

    def extensao_arquivo(self):
        dir_inverso = self.diretorio[::-1]
        return dir_inverso[:str(dir_inverso).find('.') + 1][::-1].lower()

