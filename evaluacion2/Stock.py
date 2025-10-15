from Ingrediente import Ingrediente
import os
import csv



class Stock:
    CSV_FILENAME = os.path.join(os.path.dirname(__file__), "ingredientes_menu.csv")

    def __init__(self):
        self.lista_ingredientes = []

        self.cargar_desde_csv()


    def agregar_ingrediente(self, ingrediente: Ingrediente):
        # Normalizar nombre
        try:
            nombre_nuevo = ingrediente.nombre.strip().lower()
        except Exception:
            nombre_nuevo = str(ingrediente.nombre).strip().lower()

        # Intentar parsear la cantidad y validar que no sea negativa
        try:
            cantidad_nueva = float(ingrediente.cantidad)
        except Exception:
            return False, f"La cantidad para '{ingrediente.nombre}' no es válida."

        if cantidad_nueva < 0:
            return False, "No se permiten cantidades negativas."

        # Buscar si ya existe el ingrediente y sumar
        for ing in self.lista_ingredientes:
            try:
                if str(ing.nombre).strip().lower() == nombre_nuevo:
                    try:
                        ing.cantidad = float(ing.cantidad) + cantidad_nueva
                    except Exception:
                        # si falla convertir la cantidad previa, reemplazarla
                        try:
                            ing.cantidad = cantidad_nueva
                        except Exception:
                            pass
                    self.actualizar_csv()
                    return True, None
            except Exception:
                continue

        # Si no existía, normalizar nombre y agregar
        try:
            ingrediente.nombre = ingrediente.nombre.strip().capitalize()
        except Exception:
            pass
        ingrediente.cantidad = cantidad_nueva
        self.lista_ingredientes.append(ingrediente)
        self.actualizar_csv()
        return True, None

    def eliminar_ingrediente(self, nombre_ingrediente: str):
        antes = len(self.lista_ingredientes)
        self.lista_ingredientes = [i for i in self.lista_ingredientes if i.nombre != nombre_ingrediente]
        if len(self.lista_ingredientes) < antes:
            self.actualizar_csv()
            return True, None
        return False, "Ingrediente no encontrado."

    def verificar_stock(self):
        return self.lista_ingredientes

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        for ing in self.lista_ingredientes:
            if ing.nombre == nombre_ingrediente:
                # validar nueva cantidad
                try:
                    nueva_cant = float(nueva_cantidad)
                except Exception:
                    return False, f"La cantidad ingresada para '{nombre_ingrediente}' no es válida."

                if nueva_cant < 0:
                    return False, "No se permiten cantidades negativas."

                ing.cantidad = nueva_cant
                self.actualizar_csv()
                return True, None
            return False, "Ingrediente no encontrado."

    def obtener_elementos_menu(self):
        return self.lista_ingredientes

    def cargar_desde_csv(self):
        self.lista_ingredientes = []
        if not os.path.exists(self.CSV_FILENAME):
            return
        
        try:
            with open(self.CSV_FILENAME, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    nombre = row.get('nombre') or row.get('Name') or row.get('Nombre') or row.get('nombre_ingrediente')
                    unidad = row.get('unidad') or row.get('Unidad') or ''
                    cantidad = row.get('cantidad') or row.get('Cantidad') or 0
                    if nombre:
                        try:
                            ing = Ingrediente(nombre=str(nombre), unidad=str(unidad) if unidad else None, cantidad=float(cantidad))
                        except Exception:
                            
                            try:
                                ing = Ingrediente(nombre=str(nombre), unidad=str(unidad) if unidad else None, cantidad=float(cantidad))
                            except Exception:
                                ing = Ingrediente(nombre=str(nombre), unidad=str(unidad) if unidad else None, cantidad=0)
                        self.lista_ingredientes.append(ing)
        except Exception:   
            pass

    def actualizar_csv(self):
        try:
            with open(self.CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['nombre', 'unidad', 'cantidad']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for ing in self.lista_ingredientes:
                    cantidad_para_csv = ing.cantidad_str() if hasattr(ing, 'cantidad_str') else ing.cantidad
                    writer.writerow({'nombre': ing.nombre, 'unidad': ing.unidad if ing.unidad else '', 'cantidad': cantidad_para_csv})
        except Exception:
            pass
