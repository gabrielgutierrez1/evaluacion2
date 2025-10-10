# menu_catalog.py
from typing import List
from ElementoMenu import CrearMenu
from Ingrediente import Ingrediente
from IMenu import IMenu

def get_default_menus() -> List[IMenu]:
    return [
        CrearMenu(
            "Completo",
            [
                Ingrediente("Vienesa","unid", 1),
                Ingrediente("Pan de completo","unid", 1),
                Ingrediente("Palta","kg",0.5),
                Ingrediente("Tomate","kg",0.2),
            ],
            precio=1800,
            icono_path="IMG/icono_hotdog_sin_texto_64x64.png",
            
        ),
        CrearMenu(
            "Bepis",
            [
                Ingrediente("Bepis","unid",1)
            ],
            precio=1200,
            icono_path="IMG/icono_cola_64x64.png"
        ),
        CrearMenu(
            "Chorrillana",
            [
                Ingrediente("Papas","kg",0.2),
                Ingrediente("Carne de vacuno","kg",0.1),
                Ingrediente("Huevo","unid",2),
                Ingrediente("Cebolla","kg",0.05),
            ],
            precio=6500,
            icono_path="IMG/icono_chorrillana_64x64.png"
        ),
        CrearMenu(
            "Papas fritas",
            [
                Ingrediente("Papas", "unid", 5),
            ],
            precio=500,
            icono_path="IMG/icono_papas_fritas_64x64.png",
        ),


        CrearMenu(
            "Hamburguesa",
            [
                Ingrediente("Pan de hamburguesa", "unid", 1),
                Ingrediente("Lámina de queso", "unid", 1),
                Ingrediente("Churrasco de carne", "unid", 1),
            ],
            precio=3500,
            icono_path="IMG/icono_hamburguesa_negra_64x64.png",
        ),

        CrearMenu(
            "Panqueques",
            [
                Ingrediente("Panqueques", "unid", 2),
                Ingrediente("Manjar", "porción", 1),
                Ingrediente("Azúcar flor", "porción", 1),
            ],
            precio=2000,
            icono_path="IMG/icono_panqueques_64x64.png",
        ),

        CrearMenu(
            "Pollo frito",
            [
                Ingrediente("Presa de pollo", "unid", 1),
                Ingrediente("Porción de harina", "porción", 1),
                Ingrediente("Porción de aceite", "porción", 1),
            ],
            precio=2800,
            icono_path="IMG/icono_pollofrito_64x64.png",
        ),

        CrearMenu(
            "Ensalada mixta",
            [
                Ingrediente("Lechuga", "unid", 1),
                Ingrediente("Tomate", "unid", 1),
                Ingrediente("Zanahoria rallada", "unid", 1),
            ],
            precio=1500,
            icono_path="IMG/icono_ensaladamixta_64x64.png",
        ),
    ]
