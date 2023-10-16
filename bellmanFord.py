from grafo_ciudades import adyacentes
class Algoritmo:
    def __init__(self):
        self.num_vertices = len(adyacentes)
        self.distancia = [float('inf')] * self.num_vertices
        self.predecesor = [None] * self.num_vertices
        self.matriz_adyacencia = adyacentes

    def bellman_ford(self, ciudad_origen):
        self.distancia[ciudad_origen] = 0

        for _ in range(self.num_vertices - 1):
            for u in range(self.num_vertices):
                for v in range(self.num_vertices):
                    if self.matriz_adyacencia[u][v] != 0 and self.distancia[v] > self.distancia[u] + \
                            self.matriz_adyacencia[u][v]:
                        self.distancia[v] = self.distancia[u] + self.matriz_adyacencia[u][v]
                        self.predecesor[v] = u

        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.matriz_adyacencia[u][v] != 0 and self.distancia[v] > self.distancia[u] + \
                        self.matriz_adyacencia[u][v]:
                    #print("Hay ciclo negativo")
                    return False

        return True

    def generar_matriz(self,ciudad_origen:int):
        self.bellman_ford(ciudad_origen)
        matriz = [[0 for _ in range (len (self.matriz_adyacencia))] for _ in range (len (self.matriz_adyacencia))]
        for i in range(len(self.predecesor)):
            if self.predecesor[i] is not None:
                matriz[i][self.predecesor[i]] = self.matriz_adyacencia[i][self.predecesor[i]]
                matriz[self.predecesor[i]][i] = self.matriz_adyacencia[self.predecesor[i]][i]
        print(matriz)

        return self.distancia,matriz