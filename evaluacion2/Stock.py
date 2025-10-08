from Ingrediente import Ingrediente
import os
import csv

class Stock:
    CSV_FILENAME = os.path.join(os.path.dirname(__file__), "ingredientes_menu.csv")

    def __init__(self):
        self.lista_ingredientes = []
        # intentar cargar ingredientes desde CSV al iniciar
        self.cargar_desde_csv()

    # agregar ingrediente a la lista y al csv
    def agregar_ingrediente(self, ingrediente: Ingrediente):
        for ing in self.lista_ingredientes:
            if ing.nombre.capitalize()  == ingrediente.nombre.capitalize():
                ing.cantidad += ingrediente.cantidad
                return True
        ingrediente.nombre= ingrediente.nombre.capitalize()
        self.lista_ingredientes.append(ingrediente)
        self.actualizar_csv()
        return True

    def eliminar_ingrediente(self, nombre_ingrediente: str):
        antes = len(self.lista_ingredientes)
        self.lista_ingredientes = [i for i in self.lista_ingredientes if i.nombre != nombre_ingrediente]
        if len(self.lista_ingredientes) < antes:
            self.actualizar_csv()
            return True
        return False

    def verificar_stock(self):
        # podría implementarse según reglas de negocio
        return self.lista_ingredientes

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        for ing in self.lista_ingredientes:
            if ing.nombre == nombre_ingrediente:
                ing.cantidad = float(nueva_cantidad)
                self.actualizar_csv()
                return True
        return False

    def obtener_elementos_menu(self):
        return self.lista_ingredientes

    def cargar_desde_csv(self):
        # Lee el CSV si existe y carga en lista_ingredientes
        if not os.path.exists(self.CSV_FILENAME):
            return
        try:
            with open(self.CSV_FILENAME, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    nombre = row.get('nombre') or row.get('Nombre') or row.get('nombre_ingrediente')
                    unidad = row.get('unidad') or row.get('Unidad') or ''
                    cantidad = row.get('cantidad') or row.get('Cantidad') or 0
                    if nombre:
                        try:
                            ing = Ingrediente(nombre=str(nombre), unidad=str(unidad) if unidad else None, cantidad=float(cantidad))
                        except Exception:
                            # en caso de formatos raros, intentar como string
                            ing = Ingrediente(nombre=str(nombre), unidad=str(unidad) if unidad else None, cantidad=0)
                        self.lista_ingredientes.append(ing)
        except Exception:
            # si falla la lectura, no rompemos la aplicación; simplemente no cargamos
            pass

    def actualizar_csv(self):
        # Escribe todos los ingredientes al CSV (sobrescribe)
        try:
            with open(self.CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['nombre', 'unidad', 'cantidad']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for ing in self.lista_ingredientes:
                    writer.writerow({'nombre': ing.nombre, 'unidad': ing.unidad if ing.unidad else '', 'cantidad': ing.cantidad})
        except Exception:
            # fallar silenciosamente (podemos mejorar mostrando mensajes desde GUI)
            pass

