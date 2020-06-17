import os


class ArquivoInf(object):
    def __init__(self, diretorio: str):
        self.diretorio: str = diretorio
        self.__status_arquivos: os.stat = os.stat(self.diretorio)
        self.tamanho: int = self.__status_arquivos.st_size
        self.data_de_modificacao: float = self.__status_arquivos.st_ctime
        self.data_acesso_recente: float = self.__status_arquivos.st_atime
        self.nome_arquivo: str = os.path.basename(self.diretorio)
        self.extensao: str = self.extensao_arquivo()

    def extensao_arquivo(self) -> str:
        dir_inverso:str = self.diretorio[::-1]
        return dir_inverso[:str(dir_inverso).find('.') + 1][::-1].lower()

