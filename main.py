import os

import flet as ft
from flet_core import theme

import mapas
from grafo_ciudades import adyacentes, lista_ciudades
import busqueda_a as ba


def main(page: ft.Page):
    page.theme_mode = "LIGHT"
    ciudades =  ft.Dropdown(options=[ft.dropdown.Option(str(x)) for x in range(len(adyacentes))] )
    page.theme = theme.Theme(color_scheme_seed="#148F77")
    page.title = "Algorithms"

    def generar_A(e):
        if ciudades.value is not None:
            peso,matriz = ba.retornar_adyacente(int(ciudades.value))
            archivo_html =  mapas.crear_mapa(matriz)
            os.system (f"start {archivo_html}")
        pass

    datos = [ft.DataRow(cells=[ft.DataCell (ft.Text (str(x))),ft.DataCell (ft.Text (lista_ciudades[x]))])
             for x in range(len(adyacentes))]

    Tabla = ft.DataTable (
        columns=[
            ft.DataColumn (ft.Text ("Id")),
            ft.DataColumn (ft.Text ("Ciudad")),
        ],
        rows= datos,
        column_spacing= 50
    )

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
                                Tabla,

                            ],
                            scroll=ft.ScrollMode.ALWAYS
                        ),
                    ],
                    vertical_alignment= ft.CrossAxisAlignment.CENTER,
                    alignment= ft.MainAxisAlignment.SPACE_AROUND
                )),
            ),
            ft.Tab(
                text= "Algoritmo Dijsktra",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Algoritmo Prim",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="Algoritmo Bellman Ford",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 4"),
            ),
        ],
        expand=1,
    )
    page.add(tabs,ft.Text("Hecho por: Jonnathan Sotelo Rodríguez - Handersson Felipe Pacheco Espitia"))
    page.update()

ft.app(target=main)