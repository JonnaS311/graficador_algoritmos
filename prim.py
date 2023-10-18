from grafo_ciudades import *
from ciudades_nodo import Ciudad

class algoritmo_prim():

    def __init__(self, nodo_incial_id):
        self.solucion = []
        self.nodo_incial = lista_ciudades[nodo_incial_id]

    def prim(self,nodo_inicial:Ciudad):
        # creamos un conjunto en donde guardamos los nodos conectados
        nodos = set()
        nodos.add(nodo_inicial)
        # inicializamos una matriz con el tamaño del grafo
        matriz_arbol = [[0 for _ in range(len(adyacentes[0]))] for _ in range(len(adyacentes))]
        posicion = tuple()
        camino = []

        # pintamos la horizontal y vertical para el nodo actual
        for i in range (len (adyacentes)):
            matriz_arbol[nodo_inicial.id][i] += 1
            matriz_arbol[i][nodo_inicial.id] += 1

        while len(nodos) != len(lista_ciudades):
            # obtenemos la arista de menor peso
            menor_peso = 0xfff
            for k in nodos:
                for i in range(len(adyacentes)):
                    if (adyacentes[k.id][i] > 0 and adyacentes[k.id][i] < menor_peso) \
                            and (matriz_arbol[k.id][i] < 2 or matriz_arbol[i][k.id] < 2 ) :
                        posicion = (k.id,i)
                        menor_peso = adyacentes[k.id][i]
            # añadimos la arista
            camino.append ((posicion[0], posicion[1]))
            is_almacenado = lista_ciudades[posicion[0]] in nodos
            if not is_almacenado:
                for i in range (len (adyacentes)):
                    matriz_arbol[posicion[0]][i] += 1
                    matriz_arbol[i][posicion[0]] += 1
            else:
                for i in range (len (adyacentes)):
                    matriz_arbol[posicion[1]][i] += 1
                    matriz_arbol[i][posicion[1]] += 1
            # añadimos el nodo nuevo
            nodos.add (lista_ciudades[posicion[0]])
            nodos.add (lista_ciudades[posicion[1]])

        return camino

    def __crear_adyacentes(self,solucion):
        matriz = [[0 for _ in range(len (adyacentes))] for _ in range(len (adyacentes))]
        for i in solucion:
            matriz[i[0]][i[1]] = adyacentes[i[0]][i[1]]
            matriz[i[1]][i[0]] = adyacentes[i[1]][i[0]]
        return matriz

    def arbol_de_expancion(self):
        self.solucion = self.prim(lista_ciudades[0])
        matriz = self.__crear_adyacentes (self.solucion)
        return self.solucion, matriz

if __name__ == '__main__':
    prim = algoritmo_prim(0)
    print(prim.arbol_de_expancion())
    pass

