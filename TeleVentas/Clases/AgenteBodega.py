import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.OrdenCompra import OrdenCompra, EstadoOrden
from Clases.Pedido import Pedido
from Clases.Usuario import Usuario
from Interfaces.ITransportadora import ITransportadora


class AgenteBodega(Usuario):
    """
    Representa al agente de bodega del sistema TeleVentas.

    Extiende Usuario y es responsable de consultar órdenes confirmadas,
    empacar pedidos y asignar una transportadora para su envío.
    """

    def __init__(
        self,
        user_id: str,
        contrasena: str,
        numero_bodega: int,
        nombre: str
    ) -> None:
        """Inicializa el agente con sus credenciales y número de bodega."""
        super().__init__(user_id, nombre, contrasena)
        self.__numero_bodega = numero_bodega

    @property
    def numero_bodega(self) -> int:
        """Retorna el número de bodega asignada al agente."""
        return self.__numero_bodega
    
    # --------------------Metodos-----------------------------------------------------

    def consultar_orden(self, orden: OrdenCompra) -> None:
        """Muestra el detalle de productos y total de una orden confirmada."""
        if orden.estado != EstadoOrden.CONFIRMADA:
            raise ValueError(
                f"Solo se pueden consultar órdenes confirmadas. "
                f"Estado actual: {orden.estado}"
            )
        for detalle in orden.detalles:
            print(
                f"  - {detalle.producto.descripcion} "
                f"| Cantidad: {detalle.cantidad} "
                f"| Subtotal: ${detalle.subtotal():.2f}"
            )
        print(f"  Total: ${orden.calcular_total():.2f}")

    def asignar_transporte(self, pedido: Pedido, empresa: ITransportadora) -> None:
        """Asigna una transportadora al pedido empacado y lo despacha."""
        print(
            f"Agente {self.nombre} asignando transporte "
            f"al pedido {pedido.numero_pedido}."
        )
        pedido.asignar_transporte(empresa)

    def __str__(self) -> str:
        """Retorna una representación legible del agente de bodega."""
        return (
            f"  AGENTE DE BODEGA\n"
            f"  id     : {self.user_id}\n"
            f"  nombre : {self.nombre}\n"
            f"  bodega : {self.__numero_bodega}\n"
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

    print("=== Prueba interactiva: clase AgenteBodega ===\n")

    # Instancias fijas
    agente = AgenteBodega("age01", "agent123", 5, "Pedro Martínez")
    cliente = Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co")
    transportadora = Transportadora(1, "TransRápido S.A.")

    print(f"{agente}")

    # Orden confirmada lista para que el agente la gestione
    prod1 = Producto(101, "Ferrari",      90_000.00, 10)
    prod2 = Producto(102, "Lamborghini",  50_000.00, 50)
    prod3 = Producto(103, "Porsche",      80_000.00, 25)
    detalles = [DetallePedido(prod1, 1), DetallePedido(prod2, 1)]
    pago = PagoTarjeta(1001, sum(d.subtotal() for d in detalles),
                       "1234567890123456", "Eduardo Coa", "12/26", "123")
    orden = OrdenCompra(1001, cliente, pago, detalles)
    # Silenciar salida de confirmación — es solo preparación para la prueba
    import io
    sys.stdout = io.StringIO()
    orden.confirmar()
    sys.stdout = sys.__stdout__

    # Parte interactiva: consultar orden y empacar pedido
    print("\n-- Consultar orden --")
    input("Presione ENTER para consultar la orden confirmada...")
    agente.consultar_orden(orden)

    print("\n-- Empacar y asignar transporte --")
    input("Presione ENTER para empacar el pedido y asignar transporte...")
    try:
        pedido = Pedido(5001, orden)
        pedido.empacar()
        agente.asignar_transporte(pedido, transportadora)
        print(f"\n{pedido}")
    except ValueError as e:
        print(f"Error: {e}")
