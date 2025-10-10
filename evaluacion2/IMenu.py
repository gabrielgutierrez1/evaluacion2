# IMenu.py
from typing import Protocol, List, Optional
from Ingrediente import Ingrediente
from Stock import Stock

class IMenu(Protocol):
    
    def esta_disponible(self, stock: Stock) -> bool:
        for req in self.ingredientes:
            ok = False
            for ing in stock.lista_ingredientes:
                if ing.nombre == req.nombre and (req.unidad is None or ing.unidad == req.unidad):
                    if int(ing.cantidad) >= int(req.cantidad):
                        ok = True
                        break
            if not ok:
                return False
        return True

    pass