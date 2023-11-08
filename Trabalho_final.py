
 
from _typeshed import Self
from msilib.schema import SelfReg


class Agente_Aspirador_Po:

    def __init__ (self):

        self.energia_aspirador = 100
        self.capacidade_bolsa = 10
        self.localizacao = 'A'
        self.sujeira = { 

            'A' : True, 'B': False, 'C': True, 'D':False, 'E':False, 'F':True, 'G': True, 'H': False, 'I':True, 'J': False, 'K': True, 'L':False, 'M':True, 'N':False, 'O':True, 'P':False

}


    def MOVER (self, direcao ):

        direcoes1 = { 'Norte': -4, 'Sul':4, 'Leste':1, 'Oeste': -1 }

        new_localizacao = ord(self.localizacao) + direcoes1[direcao]

        if 'A' <= chr(new_localizacao) <= 'P':
            self.localizacao = chr(new_localizacao)
            self.energia_aspirador -=1

            print(f" Movimentado para {self.localizacao }" )

    
    def ASPIRAR_SUJEIRAS (self):

        if Self.sujeira[self.localizacao]:

            self.sujeira[self.localizacao] = False
            self.capacidade_bolsa -=1
            self.energia_aspirador -= 1
            
            print(f"Aspirou a sujeira em  {Self.localizacao}" )


    def OBJ_ALCANCADO(sef):

        return not any(sef.sujeira.values()) and sef.capacidade_bolsa == 10

    def TOMAR_ACAO(self):

        if self.energia_aspirador <= 0:
            print(f"Energia esgotada, o aspirador de pó não pode mais continuar!!! ")

            return
               




