from abc import ABC, abstractmethod


class IInventario(ABC):
    """
    Interfaz que debe implementar el sistema de inventario externo de TeleVentas.

    Permite consultar productos, actualizar el stock al empacar pedidos
    y verificar disponibilidad antes de confirmar una orden de compra.
    """

    @abstractmethod
    def consultar_producto(self, codigo: int) -> dict:
        """Retorna la información de un producto dado su código."""
        pass

    @abstractmethod
    def actualizar_stock(self, codigo: int, qty: int) -> None:
        """Descuenta la cantidad indicada del stock del producto."""
        pass

    @abstractmethod
    def verificar_disponibilidad(self, codigo: int) -> bool:
        """Retorna True si el producto existe y tiene stock disponible."""
        pass
