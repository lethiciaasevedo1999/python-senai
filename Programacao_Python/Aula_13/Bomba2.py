#Desafio da bomba d'agua 2 

import time 

class Bomba_02:
    def __init__(self):
        self.status = False
        
    def ligar(self, tempo: int):
        '''Liga a bomba por um determinado tempo (em segundos).'''
        if self.status:
            print("A bomba já está ligada")
            return
        
        self.status = True
        print("Bomba ligada.")
        for segundos_restantes in range (tempo, 0, -1):
            print(f"Segundos restantes: {segundos_restantes}")
            time.sleep(1)
        self.desligar()
        
    def desligar(self):
        """Desligar a bomba."""
        if not self.status:
            print("A bomba já está desligada.")
            return
        
        self.status = False
        print("Bomba desligada.")
        
# Classe usa Bomba 

class UsaBomba:
    @staticmethod
    def main():
        #Instancia uma bomba
        bomba1 = Bomba_02()
        
        #Liga a bomba por 5 segundos
        bomba1.ligar(5)
        
# Executa o programa 
if __name__ == "__main__":
    UsaBomba.main()