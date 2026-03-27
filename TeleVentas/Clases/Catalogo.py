from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date
from Clases.Producto import Producto
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Clases.Cliente import Cliente


class Catalogo:
    """
    Representa el catálogo de productos disponibles en TeleVentas.

    Permite listar, buscar y enviar productos, así como gestionar
    las suscripciones de los clientes para recibir el catálogo por correo.
    """

    def __init__(
        self,
        numero_catalogo: int,
        productos: list[Producto] = None
    ) -> None:
        """Inicializa el catálogo con un número identificador y una lista opcional de productos."""
        self.__numero_catalogo = numero_catalogo
        self.__fecha = date.today()
        self.__productos = productos if productos else []
        self.__suscriptores = []

    @property
    def numero_catalogo(self) -> int:
        """Retorna el número identificador del catálogo."""
        return self.__numero_catalogo

    @property
    def fecha(self) -> date:
        """Retorna la fecha de creación del catálogo."""
        return self.__fecha

    @property
    def productos(self) -> list:
        """Retorna la lista de productos del catálogo."""
        return self.__productos

# --------------------Metodos--------------------------------------------------

    def lista_productos(self) -> list:
        """Retorna la información de todos los productos del catálogo."""
        return [p.get_info() for p in self.__productos]

    def buscar_producto(self, termino: str) -> list:
        """Busca productos cuya descripción contenga el término ingresado."""
        resultados = [
            p for p in self.__productos
            if termino.lower() in p.descripcion.lower()
        ]
        if not resultados:
            print(f"No se encontraron productos con '{termino}'.")
        return resultados

    def suscribir(self, cliente: Cliente) -> None:
        """Suscribe a un cliente al catálogo para recibir envíos periódicos."""
        if cliente in self.__suscriptores:
            raise ValueError(
                f"El cliente {cliente.nombre} ya está suscrito."
            )
        self.__suscriptores.append(cliente)
        print(
            f" El cliente {cliente.nombre} ha sido suscrito al "
            f"catálogo {self.__numero_catalogo}."
        )

    def enviar_catalogo(self, cliente: Cliente) -> None:
        """Envía el catálogo completo al correo del cliente."""
        print(
            f" Catálogo {self.__numero_catalogo} enviado "
            f"a {cliente.correo}."
        )
        
    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo producto al catálogo si no existe previamente."""
        if producto in self.__productos:
            raise ValueError(
                f"El producto {producto.descripcion} ya está en el catálogo."
            )
        self.__productos.append(producto)
        print(f"Producto '{producto.descripcion}' agregado al catálogo.")

    def __str__(self) -> str:
        """Retorna una representación legible del catálogo."""
        return (
            f"  CATALOGO # {self.__numero_catalogo}\n"
            f"  fecha       : {self.__fecha}\n"
            f"  productos   : {len(self.__productos)}\n"
            f"  suscriptores: {len(self.__suscriptores)}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    from Clases.Cliente import Cliente

    print("=== Prueba: Catalogo ===\n")

    # Instancias fijas
    prod1 = Producto(101, "Ferrari",     90_000.00, 10)
    prod2 = Producto(102, "Lamborghini", 50_000.00, 50)
    prod3 = Producto(103, "Porsche",     80_000.00, 25)
    catalogo = Catalogo(1, [prod1, prod2, prod3])
    cliente = Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co")

    print(catalogo)

    while True:
        print("--------------------------------")
        print("  1. Listar productos")
        print("  2. Buscar producto")
        print("  3. Suscribirse al catálogo")
        print("  0. Salir")
        opcion = input("\nOpción: ").strip()

        if opcion == "1":
            for p in catalogo.lista_productos():
                print(f"  [{p['numero_producto']}] {p['descripcion']}  —  ${p['precio']:,.2f}  (stock: {p['cantidad_disponible']})")

        elif opcion == "2":
            termino = input("Término de búsqueda: ").strip()
            resultados = catalogo.buscar_producto(termino)
            if resultados:
                print("-- Resultados --")
                for p in resultados:
                    print(f"  [{p.numero_producto}] {p.descripcion}  —  ${p.precio:,.2f}  (stock: {p.cantidad_disponible})")

        elif opcion == "3":
            try:
                catalogo.suscribir(cliente)
                catalogo.enviar_catalogo(cliente)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
