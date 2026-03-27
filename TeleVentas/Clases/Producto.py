import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Producto:
    """
    Representa un producto disponible en el catálogo de TeleVentas.

    Almacena el código, descripción, precio y cantidad disponible.
    """

    def __init__(
        self,
        numero_producto: int,
        descripcion: str,
        precio: float,
        cantidad_disponible: int
    ) -> None:
        """Inicializa un producto validando que el precio y stock no sean negativos."""
        if precio < 0:
            raise ValueError("El precio no debe ser negativo.")
        if cantidad_disponible < 0:
            raise ValueError("La cantidad disponible no puede ser negativa.")

        self.__numero_producto = numero_producto
        self.__descripcion = descripcion
        self.__precio = precio
        self.__cantidad_disponible = cantidad_disponible

    @property
    def numero_producto(self) -> int:
        """Retorna el código identificador del producto."""
        return self.__numero_producto

    @property
    def descripcion(self) -> str:
        """Retorna la descripción del producto."""
        return self.__descripcion

    @property
    def precio(self) -> float:
        """Retorna el precio del producto."""
        return self.__precio

    @property
    def cantidad_disponible(self) -> int:
        """Retorna la cantidad disponible en stock."""
        return self.__cantidad_disponible

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        """Actualiza el precio del producto validando que no sea negativo."""
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = nuevo_precio

    @cantidad_disponible.setter
    def cantidad_disponible(self, nueva_cantidad: int) -> None:
        """Actualiza el stock del producto validando que no sea negativo."""
        if nueva_cantidad < 0:
            raise ValueError("La cantidad disponible no puede ser negativa.")
        self.__cantidad_disponible = nueva_cantidad

    # --------------------Metodos--------------------------------------------------

    def get_info(self) -> dict:
        """Retorna un diccionario con la información completa del producto."""
        return {
            "numero_producto": self.__numero_producto,
            "descripcion": self.__descripcion,
            "precio": self.__precio,
            "cantidad_disponible": self.__cantidad_disponible
        }

    def actualizar(self, precio: float = None, cantidad: int = None) -> None:
        """Actualiza el precio y/o la cantidad disponible del producto."""
        if precio is not None:
            self.precio = precio
        if cantidad is not None:
            self.cantidad_disponible = cantidad

    def __str__(self) -> str:
        """Retorna una representación legible del producto."""
        return (
            f"  PRODUCTO # {self.__numero_producto}\n"
            f"  descripcion: {self.__descripcion}\n"
            f"  precio     : ${self.__precio:,.2f}\n"
            f"  stock      : {self.__cantidad_disponible}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Prueba: Producto ===\n")

    # Instancias fijas
    prod1 = Producto(101, "Ferrari",     90_000.00, 10)
    prod2 = Producto(102, "Lamborghini", 50_000.00, 50)
    prod3 = Producto(103, "Porsche",     80_000.00, 25)

    print(prod1)
    print(prod2)
    print(prod3)

    # Parte interactiva: actualizar precio o stock de un producto
    print("-- Actualizar producto --")
    print("  [101] Ferrari  [102] Lamborghini  [103] Porsche")
    try:
        cod = int(input("Código del producto a actualizar: ").strip())
        producto = next((p for p in [prod1, prod2, prod3] if p.numero_producto == cod), None)
        if not producto:
            print("Producto no encontrado.")
        else:
            nuevo_precio = input(f"Nuevo precio (ENTER para mantener ${producto.precio:,.2f}): ").strip()
            nuevo_stock  = input(f"Nuevo stock  (ENTER para mantener {producto.cantidad_disponible}): ").strip()
            producto.actualizar(
                precio   = float(nuevo_precio.replace("$", "").replace(",", "")) if nuevo_precio else None,
                cantidad = int(nuevo_stock) if nuevo_stock else None
            )
            print(f"\nProducto actualizado:\n{producto}")
    except ValueError as e:
        print(f"Error: {e}")
