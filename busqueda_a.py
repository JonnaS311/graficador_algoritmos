from grafo_ciudades import adyacentes,lista_ciudades, visitados

ciudad_inicial = lista_ciudades[0]
sumatoria_fn = 0
camino = []
camino.append(ciudad_inicial.id)
def busqueda_A(ciudad_Actual, sumatoria):
    if ciudad_Actual != lista_ciudades[9]:   # verificamos que no estamos en cartagena
        pesos = []
        ciudades_adyacentes = {}
        for i in range(len(adyacentes[ciudad_Actual.id])):
            if adyacentes[ciudad_Actual.id][i] != 0: #calculo de gn y la ciudad de la que es el dato
                pesos.append(calcular_gn(lista_ciudades[i],ciudad_Actual)+sumatoria)
                ciudades_adyacentes[lista_ciudades[i].id] = lista_ciudades[i].destino
        pesos = list(map(lambda x,y: x+y,pesos,ciudades_adyacentes.values()))
        for i in range(len(pesos)):
            if pesos[i] == min(pesos): #llamamos la función busqueda_A con la ciudad siguiente
                id = list(ciudades_adyacentes.keys())[i]
                sumatoria += calcular_gn(lista_ciudades[id],ciudad_Actual)
                camino.append(id)
                busqueda_A(lista_ciudades[id],sumatoria)
        else:
            return  sumatoria

def calcular_gn(nodo,nodo_ant):
    distancia = adyacentes[lista_ciudades[nodo.id].id][nodo_ant.id]
    visitados[lista_ciudades[nodo.id].id][nodo_ant.id], visitados[nodo_ant.id][lista_ciudades[nodo.id].id] = 1,1
    return distancia

def convertir_adyacente():
    matriz = [[0 for _ in range(len(adyacentes))] for _ in range(len(adyacentes))]
    for i in range(len(camino)-1):
        matriz[camino[i]][camino[i+1]] = adyacentes[camino[i]][camino[i+1]]
        matriz[camino[i+1]][camino[i]] = adyacentes[camino[i+1]][camino[i]]

    return matriz

def retornar_adyacente(ciudad_inicial_id):
    camino.clear()
    ciudad_inicial = lista_ciudades[ciudad_inicial_id]
    camino.append(ciudad_inicial_id)
    sumatoria_fn = 0
    peso = busqueda_A(ciudad_inicial,sumatoria_fn)
    matriz = convertir_adyacente()
    print(camino)
    return peso,matriz

convertir_adyacente()