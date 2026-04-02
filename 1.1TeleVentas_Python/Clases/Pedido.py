from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.OrdenCompra import OrdenCompra, EstadoOrden
from Interfaces.ITransportadora import ITransportadora
from Interfaces.IInvetario import IInventario


class Pedido:
    """
    Representa el pedido físico armado por el Agente de Bodega en TeleVentas.

    A partir de una orden confirmada, gestiona el empaque de los productos
    y la asignación de una transportadora para su despacho.
    """

    PENDIENTE           = "pendiente"
    EMPACADO            = "empacado"
    TRANSPORTE_ASIGNADO = "transporte_asignado"
    EN_DESPACHO         = "en_despacho"

    def __init__(
        self,
        numero_pedido: int,
        orden: OrdenCompra,
        inventario: IInventario = None
    ) -> None:
        """Inicializa el pedido en estado PENDIENTE a partir de una orden de compra."""
        self.__numero_pedido  = numero_pedido
        self.__orden          = orden
        self.__estado         = Pedido.PENDIENTE
        self.__transportadora = None
        self.__inventario     = inventario

    @property
    def numero_pedido(self) -> int:
        """Retorna el número identificador del pedido."""
        return self.__numero_pedido

    @property
    def orden(self) -> OrdenCompra:
        """Retorna la orden de compra asociada al pedido."""
        return self.__orden

    @property
    def estado(self) -> str:
        """Retorna el estado actual del pedido."""
        return self.__estado

    @property
    def transportadora(self) -> ITransportadora:
        """Retorna la transportadora asignada al pedido."""
        return self.__transportadora

    # --------------------Metodos--------------------------------------------------

    def empacar(self) -> None:
        """Empaca el pedido y actualiza el stock si hay inventario disponible."""
        if self.__estado != Pedido.PENDIENTE:
            raise ValueError(
                f"El pedido ya fue empacado. Estado: {self.__estado}"
            )
        if self.__orden.estado != EstadoOrden.CONFIRMADA:
            raise ValueError(
                "Solo se pueden empacar órdenes confirmadas."
            )
        if self.__inventario:
            for detalle in self.__orden.detalles:
                self.__inventario.actualizar_stock(
                    detalle.producto.numero_producto,
                    detalle.cantidad
                )
        self.__estado = Pedido.EMPACADO
        print(
            f"Pedido {self.__numero_pedido} empacado. "
            f"Productos: {len(self.__orden.detalles)}"
        )

    def asignar_transporte(self, empresa: ITransportadora) -> None:
        """Asigna una transportadora al pedido empacado y lo pone en despacho."""
        if self.__estado != Pedido.EMPACADO:
            raise ValueError(
                "El pedido debe estar empacado antes de asignar transporte."
            )
        self.__transportadora = empresa
        self.__estado = Pedido.TRANSPORTE_ASIGNADO
        print(f"Transportadora asignada al pedido {self.__numero_pedido}.")

        if empresa.recibir_pedido(self):
            self.__estado = Pedido.EN_DESPACHO
            print(f"Pedido {self.__numero_pedido} en despacho.")

    def __str__(self) -> str:
        """Retorna una representación legible del pedido."""
        transp = (
            self.__transportadora.get_estado_envio()
            if self.__transportadora
            else "sin asignar"
        )
        return (
            f"  PEDIDO # {self.__numero_pedido}\n"
            f"  estado : {self.__estado}\n"
            f"  orden  : {self.__orden.numero_orden}\n"
            f"  envio  : {transp}\n"
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
    from Clases.Transportadora import Transportadora

    print("=== Prueba: Pedido ===\n")

    # Instancias fijas
    cliente       = Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co")
    transportadora = Transportadora(1, "TransRápido S.A.")
    prod1  = Producto(101, "Ferrari",     90_000.00, 10)
    prod2  = Producto(102, "Lamborghini", 50_000.00, 50)
    detalles = [DetallePedido(prod1, 1), DetallePedido(prod2, 2)]
    pago   = PagoTarjeta(1001, sum(d.subtotal() for d in detalles),
                         "1234567890123456", "Eduardo Coa", "12/26", "123")

    # Confirmar orden en silencio — solo preparación
    import io
    orden = OrdenCompra(1001, cliente, pago, detalles)
    sys.stdout = io.StringIO()
    orden.confirmar()
    sys.stdout = sys.__stdout__

    pedido = Pedido(5001, orden)
    print(f"{pedido}")

    # Parte interactiva: empacar y asignar transporte
    input("Presione ENTER para empacar el pedido...")
    try:
        pedido.empacar()
        print(f"\n{pedido}")

        input("Presione ENTER para asignar transporte...")
        pedido.asignar_transporte(transportadora)
        print(f"\n{pedido}")
    except ValueError as e:
        print(f"Error: {e}")

