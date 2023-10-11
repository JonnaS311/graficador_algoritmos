import folium
from folium import PolyLine

from coordenadas import ciudades, adyacentes
import copy

def crear_mapa(matriz):
    ady = copy.deepcopy(adyacentes)
    # Interactive map
    m = folium.Map(location = ciudades[0], zoom_start = 6)
    # Add a marker to the map
    values = ciudades.keys()
    for ciudad in values:
        folium.Marker(location = ciudades[ciudad]).add_to(m)

    # add a line beetween two cities
    for i in range(len(ady)):
        for j in range(len(ady[i])):
            if ady[i][j] != 0:
                line = PolyLine(locations=[ciudades[i],ciudades[j]], color="black", weight=3)
                line.add_to(m)
                ady[i][j], ady[j][i] = 0,0

    # agragamos rutas criticas
    for i in range (len (matriz)):
        for j in range (len (matriz[i])):
            if matriz[i][j] != 0:
                line = PolyLine (locations=[ciudades[i], ciudades[j]], color="blue", weight=4)
                line.add_to (m)
                matriz[i][j], matriz[j][i] = 0, 0


    m.save("mi_mapa.html")

    return "mi_mapa.html"