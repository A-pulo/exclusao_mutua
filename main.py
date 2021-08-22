import time
from random import randint
import asyncio
import threading

# Classe processo

class Processo:
    def __init__(self, id):
        self.__id = id
        self.__ts = time.perf_counter()
        self.__tag = f'Processo {id}:'
        threading.Thread(target=self.run_p).start()

    def run_p(self):
        print(f'{self.__tag} Inicializado!')
        while (True):
            time.sleep(randint(2,5))
            print(f'{self.__tag} ativo á {self.get_uptime()} segundos')

    def get_uptime(self):
        return round(time.perf_counter() - self.__ts)


def gera_processo():
    while(True):
        ran_id = randint(0, 2048)
        processos[ran_id] = Processo(ran_id)
        time.sleep(40)


#Execução principal
processos = dict()
threading.Thread(target=gera_processo).start()
print('sim')

