
import tkinter as tk
from tkinter import messagebox


# Clase Nodo
class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None


# Clase Lista Circular Simple
class ListaCircular:
    def __init__(self):
        self.ultimo = None

    # Agregar producto
    def agregar(self, producto):
        nuevo = Nodo(producto)

        # Si la lista está vacía
        if self.ultimo is None:
            self.ultimo = nuevo
            nuevo.siguiente = nuevo

        else:
            nuevo.siguiente = self.ultimo.siguiente
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    # Mostrar productos
    def obtener_productos(self):
        productos = []

        if self.ultimo is None:
            return productos

        actual = self.ultimo.siguiente

        while True:
            productos.append(actual.producto)
            actual = actual.siguiente

            if actual == self.ultimo.siguiente:
                break

        return productos

    # Eliminar producto
    def eliminar(self, posicion):
        if self.ultimo is None:
            return False

        actual = self.ultimo.siguiente
        anterior = self.ultimo
        contador = 0

        while True:

            if contador == posicion:

                # Si solamente hay un elemento
                if actual == self.ultimo and actual == self.ultimo.siguiente:
                    self.ultimo = None

                else:
                    anterior.siguiente = actual.siguiente

                    if actual == self.ultimo:
                        self.ultimo = anterior

                return True

            anterior = actual
            actual = actual.siguiente
            contador += 1

            if actual == self.ultimo.siguiente:
                break

        return False


# Crear lista circular
lista_compras = ListaCircular()


# ---------------- FUNCIONES DE LA INTERFAZ ----------------

def mostrar():
    lista.delete(0, tk.END)

    productos = lista_compras.obtener_productos()

    for producto in productos:
        lista.insert(tk.END, producto)

    contador.config(
        text=f"Cantidad de productos: {len(productos)}"
    )


def agregar():
    producto = caja.get().strip()

    if producto == "":
        messagebox.showwarning(
            "Aviso",
            "Escriba un producto."
        )
        return

    lista_compras.agregar(producto)

    caja.delete(0, tk.END)

    mostrar()

    caja.focus()


def borrar():
    seleccionado = lista.curselection()

    if not seleccionado:
        messagebox.showwarning(
            "Aviso",
            "Seleccione un producto."
        )
        return

    posicion = seleccionado[0]

    lista_compras.eliminar(posicion)

    mostrar()


# ---------------- VENTANA ----------------

ventana = tk.Tk()

ventana.title("Lista de Compras - Lista Circular")
ventana.geometry("450x450")
ventana.resizable(False, False)


titulo = tk.Label(
    ventana,
    text="LISTA DE COMPRAS",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=15)


caja = tk.Entry(
    ventana,
    width=35,
    font=("Arial", 12)
)

caja.pack(pady=5)


boton_agregar = tk.Button(
    ventana,
    text="Agregar producto",
    command=agregar,
    width=25
)

boton_agregar.pack(pady=10)


lista = tk.Listbox(
    ventana,
    width=40,
    height=12,
    font=("Arial", 11)
)

lista.pack(pady=10)


boton_borrar = tk.Button(
    ventana,
    text="Borrar producto",
    command=borrar,
    width=25
)

boton_borrar.pack(pady=5)


contador = tk.Label(
    ventana,
    text="Cantidad de productos: 0",
    font=("Arial", 10)
)

contador.pack(pady=10)


caja.focus()

ventana.mainloop()