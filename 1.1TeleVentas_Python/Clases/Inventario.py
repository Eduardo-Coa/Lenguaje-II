import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Interfaces.IInvetario import IInventario


class Inventario(IInventario):
    """
    Representa el sistema de inventario externo de TeleVentas.

    Implementa IInventario y permite consultar productos, verificar
    disponibilidad y actualizar el stock al momento de empacar pedidos.
    """

    def __init__(
        self,
        url_api: str,
        nombre: str
    ) -> None:
        """Inicializa el inventario con su URL de API y nombre identificador."""
        self.__url_api   = url_api
        self.__nombre    = nombre
        # Diccionario interno que simula la base de datos del inventario
        self.__productos = {}

    @property
    def url_api(self) -> str:
        """Retorna la URL de la API del inventario (solo lectura)."""
        return self.__url_api

    @property
    def nombre(self) -> str:
        """Retorna el nombre del inventario (solo lectura)."""
        return self.__nombre

    # --------------------Metodos--------------------------------------------------

    def registrar_producto(self, codigo: int, descripcion: str, precio: float, stock: int) -> None:
        """Registra un nuevo producto en el inventario con su stock inicial."""
        self.__productos[codigo] = {
            "codigo":      codigo,
            "descripcion": descripcion,
            "precio":      precio,
            "stock":       stock
        }
        print(f"Producto '{descripcion}' registrado en inventario.")

    def consultar_producto(self, codigo: int) -> dict:
        """Retorna la información de un producto por su código. Lanza error si no existe."""
        if codigo not in self.__productos:
            raise ValueError(
                f"Producto con código {codigo} no encontrado en inventario."
            )
        return self.__productos[codigo]

    def actualizar_stock(self, codigo: int, qty: int) -> None:
        """Descuenta la cantidad indicada del stock del producto."""
        producto = self.consultar_producto(codigo)
        if producto["stock"] < qty:
            raise ValueError(
                f"Stock insuficiente para producto {codigo}. "
                f"Disponible: {producto['stock']}, solicitado: {qty}"
            )
        self.__productos[codigo]["stock"] -= qty
        print(
            f"Stock actualizado — producto {codigo}: "
            f"{producto['stock'] + qty} → {self.__productos[codigo]['stock']}"
        )

    def verificar_disponibilidad(self, codigo: int) -> bool:
        """Retorna True si el producto existe y tiene stock mayor a cero."""
        try:
            producto = self.consultar_producto(codigo)
            return producto["stock"] > 0
        except ValueError:
            return False

    def __str__(self) -> str:
        """Retorna una representación legible del inventario."""
        return (
            f"  INVENTARIO\n"
            f"  nombre   : {self.__nombre}\n"
            f"  url      : {self.__url_api}\n"
            f"  productos: {len(self.__productos)}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Prueba: Inventario ===\n")

    # Instancia fija
    inventario = Inventario("http://api.televentas.com/inventario", "Inventario Central")
    inventario.registrar_producto(101, "Ferrari",     90_000.00, 10)
    inventario.registrar_producto(102, "Lamborghini", 50_000.00, 50)
    inventario.registrar_producto(103, "Porsche",     80_000.00, 25)

    print(f"\n{inventario}")

    while True:
        print("  1. Consultar producto")
        print("  2. Verificar disponibilidad")
        print("  3. Actualizar stock")
        print("  0. Salir")
        opcion = input("\nOpción: ").strip()

        if opcion == "1":
            try:
                cod = int(input("Código del producto: ").strip())
                p   = inventario.consultar_producto(cod)
                print(f"  [{p['codigo']}] {p['descripcion']}  —  ${p['precio']:,.2f}  (stock: {p['stock']})")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            try:
                cod  = int(input("Código del producto: ").strip())
                disp = inventario.verificar_disponibilidad(cod)
                print(f"  Disponible: {'Sí' if disp else 'No'}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            try:
                cod = int(input("Código del producto: ").strip())
                qty = int(input("Cantidad a descontar: ").strip())
                inventario.actualizar_stock(cod, qty)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
