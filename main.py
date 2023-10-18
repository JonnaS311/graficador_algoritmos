import os

import flet as ft
from flet_core import theme

import dijkstra
import mapas
import prim
from bellmanFord import Algoritmo
from grafo_ciudades import adyacentes, lista_ciudades
import busqueda_a as ba


def main(page: ft.Page):
    page.theme_mode = "LIGHT"
    ciudades =  ft.Dropdown(options=[ft.dropdown.Option(str(x)) for x in range(len(adyacentes))] )
    ciudades_aux = ft.Dropdown (options=[ft.dropdown.Option (str (x)) for x in range (len (adyacentes))])
    page.theme = theme.Theme(color_scheme_seed="#148F77")
    page.title = "Algorithms"

    def generar_A(e):
        if ciudades.value is not None:
            peso,matriz,camino = ba.algoritmo_a_star(int(ciudades.value)).generar_recorrido()
            text_info = '\n'
            for i in camino:
                text_info +=  '✔️' + lista_ciudades[i].nombre +'\n'
            informacion_a.value= f"El costo para llegar al destino es de: {peso}. \nDebe pasar por las ciudadades: {text_info}"
            page.update()
            archivo_html =  mapas.crear_mapa(matriz)
            os.system (f"start {archivo_html}")

    def generar_prim(e):
        if ciudades.value is not None:
            camino, matriz = prim.algoritmo_prim(int (ciudades.value)).arbol_de_expancion()
            text_info = '\n'
            for i in camino:
                text_info += "✔️" + lista_ciudades[i[0]].nombre + " -> " + lista_ciudades[i[1]].nombre + "\n"
            informacion_p.value = f"El árbol de expación miníno se encuentra pasando por las aristas: {text_info}"
            page.update ()
            archivo_html = mapas.crear_mapa (matriz)
            os.system (f"start {archivo_html}")

    def generar_dij(e):
        if ciudades.value is not None and ciudades_aux.value is not None:
            matriz,distancia,caminos = dijkstra.algoritmo_dijkstra().camino_entre_ciudades(int (ciudades.value),int (ciudades_aux.value))
            text_info = "\n"
            for i in caminos:
                text_info += "✔️" + i.nombre + "\n"
            informacion_d.value = f"la distancia miníma es de: {distancia}. \nY las ciudades por donde pasa son:{text_info}"
            page.update ()
            archivo_html = mapas.crear_mapa (matriz)
            os.system (f"start {archivo_html}")

    def generar_B(e):
        if ciudades.value is not None:
            distancias,matriz = Algoritmo().generar_matriz(int(ciudades.value))
            text_info = '\n'
            for i in range(len(distancias)):
                text_info +=  '✔️' + lista_ciudades[i].nombre + "->" + str(distancias[i]) +'\n'
            informacion_b.value= f"El costo para llegar al destino es de:\n {text_info}"
            page.update()
            archivo_html =  mapas.crear_mapa(matriz)
            os.system (f"start {archivo_html}")

    datos = [ft.DataRow(cells=[ft.DataCell (ft.Text (str(x))),ft.DataCell (ft.Text (lista_ciudades[x]))])
             for x in range(len(adyacentes))]


    Tabla = ft.Column (

        controls=[
            ft.DataTable (
                columns=[
                    ft.DataColumn (ft.Text ("Id")),
                    ft.DataColumn (ft.Text ("Ciudad")),
                ],
                rows=datos,
                column_spacing=50
            )

        ],
        scroll=ft.ScrollMode.ALWAYS,
        auto_scroll=False
    )

    informacion_a = ft.TextField(disabled=False, label='Información del Camino',read_only=True, value=" ",
                               multiline=True,width=400, text_style=ft.TextStyle(font_family='Consolas'),text_size=14)
    informacion_p = ft.TextField(disabled=False, label='Información del Camino',read_only=True, value=" ",
                               multiline=True,width=400, text_style=ft.TextStyle(font_family='Consolas'),text_size=14)
    informacion_d = ft.TextField(disabled=False, label='Información del Camino',read_only=True, value=" ",
                               multiline=True,width=400, text_style=ft.TextStyle(font_family='Consolas'),text_size=14)
    informacion_b = ft.TextField(disabled=False, label='Información del Camino',read_only=True, value=" ",
                               multiline=True,width=400, text_style=ft.TextStyle(font_family='Consolas'),text_size=14)

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,

        tabs=[
            ft.Tab(
                text="Algoritmo A-star",
                icon=ft.icons.SETTINGS,
                content=ft.Container(ft.Row(

                    controls=[
                        ft.Column(
                            alignment= ft.MainAxisAlignment.CENTER,
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Todos los caminos llevan a Cartagena...", size=14,italic=True),
                                ft.Text("Ciudad de partida", size=18),
                                ciudades,
                                ft.FilledButton("Generar", on_click=generar_A)
                            ]
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container (
                                    expand=False,
                                    content=ft.Text('La siguiente tabla muestra información sobre los ID de cada ciudad y un tablero con el camino optimo.'
                                                    ,style=ft.TextThemeStyle.BODY_LARGE, max_lines=4,width=300,
                                                    height=70,text_align=ft.TextAlign.CENTER,),
                                    margin= ft.margin.symmetric(20,0)
                                ),
                                ft.Container(
                                    expand=3,
                                    content=Tabla,
                                    margin=10
                                ),
                                ft.Container(
                                    expand=2,
                                    margin=ft.margin.symmetric(10,0),
                                    content= informacion_a
                                )
                            ],
                        )
                    ],
                    vertical_alignment= ft.CrossAxisAlignment.CENTER,
                    alignment= ft.MainAxisAlignment.SPACE_AROUND
                )),
            ),
            ft.Tab(
                text= "Algoritmo Prim",
                icon=ft.icons.SETTINGS,
                content= ft.Container(ft.Row(

                    controls=[
                        ft.Column(
                            alignment= ft.MainAxisAlignment.CENTER,
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Ciudad de partida para generar el árbol", size=18),
                                ciudades,
                                ft.FilledButton("Generar", on_click=generar_prim)
                            ]
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container (
                                    expand=False,
                                    content=ft.Text('La siguiente tabla muestra información sobre los ID de cada ciudad y un tablero con el camino optimo.'
                                                    ,style=ft.TextThemeStyle.BODY_LARGE, max_lines=4,width=300,
                                                    height=70,text_align=ft.TextAlign.CENTER,),
                                    margin= ft.margin.symmetric(20,0)
                                ),
                                ft.Container(
                                    expand=3,
                                    content=Tabla,
                                    margin=10
                                ),
                                ft.Container(
                                    expand=2,
                                    margin=ft.margin.symmetric(10,0),
                                    content= informacion_p
                                )
                            ],
                        )
                    ],
                    vertical_alignment= ft.CrossAxisAlignment.CENTER,
                    alignment= ft.MainAxisAlignment.SPACE_AROUND
                )),
            ),
            ft.Tab(
                text="Algoritmo Dijsktra",
                icon=ft.icons.SETTINGS,
                content=ft.Container(ft.Row(

                    controls=[
                        ft.Column(
                            alignment= ft.MainAxisAlignment.CENTER,
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Ciudades de partida y llegada", size=18),
                                ft.Text("ciudad de partida",size=14,italic=True),
                                ciudades,
                                ft.Text ("ciudad de llegada", size=14, italic=True),
                                ciudades_aux,
                                ft.FilledButton("Generar", on_click=generar_dij)
                            ]
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container (
                                    expand=False,
                                    content=ft.Text('La siguiente tabla muestra información sobre los ID de cada ciudad y un tablero con el camino optimo.'
                                                    ,style=ft.TextThemeStyle.BODY_LARGE, max_lines=4,width=300,
                                                    height=70,text_align=ft.TextAlign.CENTER,),
                                    margin= ft.margin.symmetric(20,0)
                                ),
                                ft.Container(
                                    expand=3,
                                    content=Tabla,
                                    margin=10
                                ),
                                ft.Container(
                                    expand=2,
                                    margin=ft.margin.symmetric(10,0),
                                    content= informacion_d
                                )
                            ],
                        )
                    ],
                    vertical_alignment= ft.CrossAxisAlignment.CENTER,
                    alignment= ft.MainAxisAlignment.SPACE_AROUND
                )),
            ),
            ft.Tab(
                text="Algoritmo Bellman Ford",
                icon=ft.icons.SETTINGS,
                content=ft.Container(ft.Row(

                    controls=[
                        ft.Column(
                            alignment= ft.MainAxisAlignment.CENTER,
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Ciudad de partida", size=18),
                                ciudades,
                                ft.FilledButton("Generar", on_click=generar_B)
                            ]
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container (
                                    expand=False,
                                    content=ft.Text('La siguiente tabla muestra información sobre los ID de cada ciudad y un tablero con el camino optimo.'
                                                    ,style=ft.TextThemeStyle.BODY_LARGE, max_lines=4,width=300,
                                                    height=70,text_align=ft.TextAlign.CENTER,),
                                    margin= ft.margin.symmetric(20,0)
                                ),
                                ft.Container(
                                    expand=3,
                                    content=Tabla,
                                    margin=10
                                ),
                                ft.Container(
                                    expand=2,
                                    margin=ft.margin.symmetric(10,0),
                                    content= informacion_b
                                )
                            ],
                        )
                    ],
                    vertical_alignment= ft.CrossAxisAlignment.CENTER,
                    alignment= ft.MainAxisAlignment.SPACE_AROUND
                )),
            ),
        ],
        expand=1,
    )

    autores = ft.Row(
        controls=[
            ft.Text("Hecho por: Jonnathan Sotelo - Handersson Felipe Pacheco - Holman Alejandro Alarcón - Juan David Pulido",size=12),
            ft.IconButton (icon=ft.icons.HUB, tooltip="GitHub repository",)]
    )
    page.add(tabs,autores)
    page.update()

ft.app(target=main)