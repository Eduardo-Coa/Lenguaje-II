from abc import ABC, abstractmethod


class ITransportadora(ABC):
    """
    Interfaz que deben implementar todas las empresas de transporte en TeleVentas.

    Garantiza que cualquier transportadora pueda recibir pedidos,
    confirmar entregas y reportar el estado del envío.
    """

    @abstractmethod
    def recibir_pedido(self, pedido) -> bool:
        """Recibe un pedido para su despacho. Retorna True si fue aceptado."""
        pass

    @abstractmethod
    def confirmar_entrega(self) -> bool:
        """Confirma que el pedido fue entregado al cliente. Retorna True si fue exitoso."""
        pass

    @abstractmethod
    def get_estado_envio(self) -> str:
        """Retorna el estado actual del envío."""
        pass
