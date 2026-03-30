import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Interfaces.ITransportadora import ITransportadora
from Clases.Pedido import Pedido


class Transportadora(ITransportadora):
    """
    Representa una empresa de transporte en TeleVentas.

    Implementa ITransportadora y gestiona la recepción, traslado
    y confirmación de entrega de los pedidos despachados.
    """

    SIN_PEDIDO = "sin_pedido"
    RECIBIDO   = "recibido"
    EN_CAMINO  = "en_camino"
    ENTREGADO  = "entregado"

    def __init__(
        self,
        id: int,
        nombre: str
    ) -> None:
        """Inicializa la transportadora sin pedido asignado."""
        self.__id     = id
        self.__nombre = nombre
        self.__estado = Transportadora.SIN_PEDIDO
        self.__pedido = None

    @property
    def id(self) -> int:
        """Retorna el identificador de la transportadora."""
        return self.__id

    @property
    def nombre(self) -> str:
        """Retorna el nombre de la transportadora."""
        return self.__nombre

    # --------------------Metodos--------------------------------------------------

    def recibir_pedido(self, pedido: Pedido) -> bool:
        """Recibe un pedido y lo pone en camino. Retorna False si ya tiene uno asignado."""
        if self.__estado != Transportadora.SIN_PEDIDO:
            print(f"Transportadora {self.__nombre} ya tiene un pedido asignado.")
            return False
        self.__pedido = pedido
        self.__estado = Transportadora.RECIBIDO
        print(f"Transportadora {self.__nombre} recibió el pedido {pedido.numero_pedido}.")
        self.__estado = Transportadora.EN_CAMINO
        print(f"Pedido en camino con {self.__nombre}.")
        return True

    def confirmar_entrega(self) -> bool:
        """Confirma la entrega del pedido en camino. Lanza error si no hay pedido activo."""
        if self.__estado != Transportadora.EN_CAMINO:
            raise ValueError(
                f"No hay pedido en camino. Estado actual: {self.__estado}"
            )
        self.__estado = Transportadora.ENTREGADO
        print(
            f"Transportadora {self.__nombre} confirmó la entrega "
            f"del pedido {self.__pedido.numero_pedido}."
        )
        return True

    def get_estado_envio(self) -> str:
        """Retorna el estado actual del envío."""
        return self.__estado

    def __str__(self) -> str:
        """Retorna una representación legible de la transportadora."""
        return (
            f"  TRANSPORTADORA # {self.__id}\n"
            f"  nombre : {self.__nombre}\n"
            f"  estado : {self.__estado}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    from Clases.Cliente import Cliente
    from Clases.Producto import Producto
    from Clases.DetallePedido import DetallePedido
    from Clases.PagoTarjeta import PagoTarjeta
    from Clases.OrdenCompra import OrdenCompra

    print("=== Prueba: Transportadora ===\n")

    # Instancias fijas
    transportadora = Transportadora(1, "TransRápido S.A.")
    cliente        = Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co")
    prod1          = Producto(101, "Ferrari",     90_000.00, 10)
    prod2          = Producto(102, "Lamborghini", 50_000.00, 50)
    detalles       = [DetallePedido(prod1, 1), DetallePedido(prod2, 1)]
    pago           = PagoTarjeta(1001, sum(d.subtotal() for d in detalles),
                                 "1234567890123456", "Eduardo Coa", "12/26", "123")

    # Confirmar orden y empacar pedido en silencio
    import io
    orden  = OrdenCompra(1001, cliente, pago, detalles)
    pedido = Pedido(5001, orden)
    sys.stdout = io.StringIO()
    orden.confirmar()
    pedido.empacar()
    sys.stdout = sys.__stdout__

    print(transportadora)

    # Parte interactiva
    input("Presione ENTER para que la transportadora reciba el pedido...")
    transportadora.recibir_pedido(pedido)
    print(f"\n{transportadora}")

    input("Presione ENTER para confirmar la entrega...")
    try:
        transportadora.confirmar_entrega()
        print(f"\n{transportadora}")
    except ValueError as e:
        print(f"Error: {e}")
