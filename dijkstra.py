from grafo_ciudades import adyacentes, lista_ciudades

class algoritmo_dijkstra():
    def __init__(self):
        pass
    def dijkstra(self,matriz_adyacencias, ciudad_origen):
        num_ciudades = len(matriz_adyacencias)

        # Almacenamiento de las distancias minimas
        distancias = [float('inf')] * num_ciudades
        isVisitadas = [False] * num_ciudades
        # Camino de la ciudad inicial a las otras
        caminos = [[] for _ in range(num_ciudades)]
        distancias[ciudad_origen] = 0

        while not all(isVisitadas):
            # Encontrar el vértice no visitado con la distancia mínima
            distancia_min = float('inf')
            ciudad_min = -1

            for ciudad in range(num_ciudades):
                if not isVisitadas[ciudad] and distancias[ciudad] < distancia_min:
                    distancia_min = distancias[ciudad]
                    ciudad_min = ciudad

            # Marcar el vértice como visitado
            isVisitadas[ciudad_min] = True

            # Actualizar las distancias y caminos a los vecinos del vértice actual
            for ciudades_ady in range(num_ciudades):
                if (
                        not isVisitadas[ciudades_ady] and
                        matriz_adyacencias[ciudad_min][ciudades_ady] != 0 and
                        distancias[ciudad_min] + matriz_adyacencias[ciudad_min][ciudades_ady] < distancias[ciudades_ady]
                ):
                    distancias[ciudades_ady] = distancias[ciudad_min] + matriz_adyacencias[ciudad_min][ciudades_ady]
                    # Agregar el valor, sin reemplazar la lista
                    caminos[ciudades_ady] = caminos[ciudad_min] + [lista_ciudades[ciudad_min]]

        return distancias, caminos

    def camino_entre_ciudades(self,ciudad_1,ciudad_2):
        ciudad_origen = ciudad_1
        distancias, caminos = self.dijkstra (adyacentes, ciudad_origen)
        matriz = [[0 for _ in range (len (adyacentes))] for _ in range (len (adyacentes))]
        lista_id = []
        for i in range (len (distancias)):
            caminos[i] = caminos[i] + [lista_ciudades[i]]

        for i in range(len(caminos[ciudad_2])):
            lista_id.append(caminos[ciudad_2][i].id)

        for i in range (len (lista_id) - 1):
            matriz[lista_id[i]][lista_id[i + 1]] = adyacentes[lista_id[i]][lista_id[i + 1]]
            matriz[lista_id[i + 1]][lista_id[i]] = adyacentes[lista_id[i + 1]][lista_id[i]]

        return matriz, distancias[ciudad_2], caminos[ciudad_2]

if __name__ == '__main__':
    dij = algoritmo_dijkstra()
    dij.camino_entre_ciudades(0,9)
    pass

