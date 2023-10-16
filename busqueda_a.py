from grafo_ciudades import adyacentes,lista_ciudades, visitados

class algoritmo_a_star():

    def __init__(self, ciudad_inicial_id):
        self.ciudad_inicial = lista_ciudades[ciudad_inicial_id]
        self.sumatoria_fn = 0
        self.peso = 0
        self.camino = []
        self.camino.append (self.ciudad_inicial.id)
        self.modificable = True

    def __busqueda_A(self,ciudad_Actual, sumatoria):
        if ciudad_Actual != lista_ciudades[9]:  # verificamos que no estamos en cartagena
            pesos = []
            ciudades_adyacentes = {}
            for i in range (len (adyacentes[ciudad_Actual.id])):
                if adyacentes[ciudad_Actual.id][i] != 0:  # calculo de gn y la ciudad de la que es el dato
                    pesos.append (self.__calcular_gn(lista_ciudades[i], ciudad_Actual) + sumatoria)
                    ciudades_adyacentes[lista_ciudades[i].id] = lista_ciudades[i].destino
            pesos = list (map (lambda x, y: x + y, pesos, ciudades_adyacentes.values ()))
            for i in range (len (pesos)):
                if pesos[i] == min (pesos):  # llamamos la función busqueda_A con la ciudad siguiente
                    id = list (ciudades_adyacentes.keys ())[i]
                    sumatoria += self.__calcular_gn (lista_ciudades[id], ciudad_Actual)
                    self.camino.append (id)
                    self.__busqueda_A(lista_ciudades[id], sumatoria)
            else:
                self.__set_peso(sumatoria)

    def __calcular_gn(self,nodo, nodo_ant):
        distancia = adyacentes[lista_ciudades[nodo.id].id][nodo_ant.id]
        visitados[lista_ciudades[nodo.id].id][nodo_ant.id], visitados[nodo_ant.id][lista_ciudades[nodo.id].id] = 1, 1
        return distancia

    def __set_peso(self,value):
        if self.modificable:
            self.peso = value
            self.modificable = False
        else:
            return

    def __convertir_adyacente(self):
        matriz = [[0 for _ in range (len (adyacentes))] for _ in range (len (adyacentes))]
        for i in range (len (self.camino) - 1):
            matriz[self.camino[i]][self.camino[i + 1]] = adyacentes[self.camino[i]][self.camino[i + 1]]
            matriz[self.camino[i + 1]][self.camino[i]] = adyacentes[self.camino[i + 1]][self.camino[i]]

        return matriz
    def generar_recorrido(self):
        self.__busqueda_A(self.ciudad_inicial, self.sumatoria_fn)
        print(self.peso)
        matriz = self.__convertir_adyacente ()
        return self.peso, matriz, self.camino

# Test de prueba
if __name__ == '__main__':
    a = algoritmo_a_star(0)
    print(a.generar_recorrido())
    print(a.camino)
    pass