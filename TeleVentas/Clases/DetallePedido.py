import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.Producto import Producto


class DetallePedido:
    """
    Representa una línea dentro de una orden de compra en TeleVentas.

    Asocia un producto con la cantidad solicitada y captura el precio
    unitario al momento de crear el detalle.
    """

    def __init__(
        self,
        producto: Producto,
        cantidad: int
    ) -> None:
        """Inicializa el detalle validando que la cantidad sea mayor a cero."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        self.__producto     = producto
        self.__cantidad     = cantidad
        # Se captura el precio al momento de crear el detalle para evitar variaciones futuras
        self.__precio_unidad = producto.precio

    @property
    def producto(self) -> Producto:
        """Retorna el producto asociado a este detalle."""
        return self.__producto

    @property
    def cantidad(self) -> int:
        """Retorna la cantidad solicitada del producto."""
        return self.__cantidad

    @property
    def precio_unidad(self) -> float:
        """Retorna el precio unitario capturado al momento de la orden."""
        return self.__precio_unidad

    # --------------------Metodos--------------------------------------------------

    def subtotal(self) -> float:
        """Calcula y retorna el subtotal multiplicando cantidad por precio unitario."""
        return self.__cantidad * self.__precio_unidad

    def get_producto(self) -> Producto:
        """Retorna el producto asociado a este detalle."""
        return self.__producto

    def __str__(self) -> str:
        """Retorna una representación legible del detalle del pedido."""
        return (
            f"  DETALLE\n"
            f"  producto    : {self.__producto.descripcion}\n"
            f"  cantidad    : {self.__cantidad}\n"
            f"  precio unit : ${self.__precio_unidad:,.2f}\n"
            f"  subtotal    : ${self.subtotal():,.2f}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Prueba: DetallePedido ===\n")

    # Productos disponibles
    productos = [
        Producto(101, "Ferrari",     90_000.00, 10),
        Producto(102, "Lamborghini", 50_000.00, 50),
        Producto(103, "Porsche",     80_000.00, 25),
    ]

    print("-- Productos disponibles --")
    for p in productos:
        print(f"  [{p.numero_producto}] {p.descripcion}  —  ${p.precio:,.2f}")

    try:
        cod = int(input("\nCódigo del producto: ").strip())
        prod = next((p for p in productos if p.numero_producto == cod), None)
        if not prod:
            print("Producto no encontrado.")
        else:
            qty = int(input(f"Cantidad de '{prod.descripcion}': ").strip())
            detalle = DetallePedido(prod, qty)
            print(f"\n{detalle}")
    except ValueError as e:
        print(f"Error: {e}")
