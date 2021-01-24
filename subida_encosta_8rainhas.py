import copy
import random

class rainha:

    # insere peça em uma determinada posição
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # verifica se uma posição é atacável
    def can_attack(self, x, y):
        rx = abs(self.x - x)
        ry = abs(self.y - y)
        # mesma linha ou coluna
        if not (rx and ry):
            return True
        if rx == ry:
            return True  # diagonal
        return False


# classe com informações do tabuleiro
class tabuleiro:

    # configurações iniciais
    def __init__(self):
        self.rainhas = []
        for i in range(8):
            self.rainhas.append(rainha(random.randint(0, 7), i))

    # menor quantidade de possibilidades
    def heuristica(self):
        custo = 0

        for i in range(8):
            for j in range(i, 8):
                if (i != j) and self.rainhas[i].can_attack(self.rainhas[j].x,
                                                           self.rainhas[j].y):
                    custo += 1

        return custo

    def move_rainha(self, x, y):
            self.rainhas[y].x = x

    def rand_tab(self):
        self.rainhas.clear()
        for i in range(8):
            self.rainhas.append(rainha(random.randint(0, 7), i))

count = 0
quantNo = 0

# expande melhor estado
def expande(estado):
    est = estado.pop(0)
    for y in range(8):
        for x in range(8):
            t = copy.deepcopy(est)
            if t.rainhas[y].x != x:
                t.move_rainha(x, y)
                estado.append(t)

    estado = sorted(estado, key=lambda x: x.heuristica())
    global quantNo
    quantNo += (len(estado) - 1)
    estadoaux = []
    estadoaux.append(estado.pop(0))
    global count
    if (est.heuristica() >= estadoaux[0].heuristica()) and count < 5:
        if est.heuristica() == estadoaux[0].heuristica():
            count += 1

        return estadoaux
    else:
        estadoaux[0].rand_tab()
        print_result(estadoaux[0].rainhas)
        count = 0
        return estadoaux

# exibe matriz final
def print_result(queens):
    m = [[0 for i in range(8)] for j in range(8)]
    for q in queens:
        m[q.y][q.x] = 1
    for i in m :
        print(i)

# estado inicial (tabuleiro vazio)
estado = [tabuleiro()]
print_result(estado[0].rainhas)
# enquanto não finalizar:
while(estado[0].heuristica() != 0):

    print(estado[0].heuristica())

    estado = expande(estado)
    if len(estado) == 0:
        print("solucao nao encontrada")

print("resultado final")
print_result(estado[0].rainhas)
print("quantidade de nos expandidos: ", quantNo)
