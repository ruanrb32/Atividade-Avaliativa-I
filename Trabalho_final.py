
 
from _typeshed import Self
from msilib.schema import SelfReg



class AGENTE_ASPIRADOR_DE_PO:

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


    def VOLTAR_PARA_CASA(self):
        
        self.localizacao = 'A'
        self.capacidade_bolsa = 10
        self.energia_aspirador -=1
        
        print(" Retornou para cara e esvaziou a sujeira da bolsa")        


    
    def OBJ_ALCANCADO(sef):

        return not any(sef.sujeira.values()) and sef.capacidade_bolsa == 10




    def TOMAR_ACAO(self):

        if self.energia_aspirador <= 0:

            print(f"Energia esgotada, o aspirador de pó não pode mais continuar!!! ")

            return
        
        if self.sujeira[self.localizacao]:
            self.ASPIRAR_SUJEIRAS()

        else:

            direcoes_disponiveis = []

            if self.localizacao != 'A':
                direcoes_disponiveis.append('NORTE')

            if self.localizacao !=  'P':
                    direcoes_disponiveis.append('SUL')

            if self.localizacao != 'D' and self.localizacao != 'H' and self.localizacao != 'L':
                        direcoes_disponiveis.append('LESTE')
                        
            if self.localizacao !='A' and self.localizacao != 'E' and self.localizacao != 'I':   
                            direcoes_disponiveis.append('OESTE')

            if direcoes_disponiveis:
                                direcao=direcoes_disponiveis[0]
                                self.MOVER(direcao)

            else: 
                  self.VOLTAR_PARA_CASA()

        if self.OBJ_ALCANCADO():

            print("Objetivo alcançado com sucesso, o ambiente está limpo e o agente retornou para casa!!!")               