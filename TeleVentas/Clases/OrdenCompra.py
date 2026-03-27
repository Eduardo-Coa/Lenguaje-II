from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date
from Clases.Pago import Pago
from Clases.DetallePedido import DetallePedido
from Interfaces.IInvetario import IInventario
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Clases.Cliente import Cliente


class EstadoOrden:
    """Constantes que representan los posibles estados de una orden de compra."""
    PENDIENTE   = "pendiente"
    CONFIRMADA  = "confirmada"
    CANCELADA   = "cancelada"
    EN_DESPACHO = "en_despacho"
    ENTREGADA   = "entregada"


class OrdenCompra:
    """
    Representa una orden de compra realizada por un cliente en TeleVentas.

    Agrupa los detalles del pedido, el método de pago y el estado actual,
    e interactúa con el inventario para verificar disponibilidad de productos.
    """

    def __init__(
        self,
        numero_orden: int,
        cliente: Cliente,
        pago: Pago,
        detalles: list[DetallePedido],
        inventario: IInventario = None
    ) -> None:
        """Inicializa la orden validando que tenga al menos un producto."""
        if not detalles:
            raise ValueError("La orden debe tener al menos un producto.")

        self.__numero_orden = numero_orden
        self.__fecha        = date.today()
        self.__estado       = EstadoOrden.PENDIENTE
        self.__cliente      = cliente
        self.__pago         = pago
        self.__detalles     = detalles
        self.__inventario   = inventario

    @property
    def numero_orden(self) -> int:
        """Retorna el número identificador de la orden."""
        return self.__numero_orden

    @property
    def fecha(self) -> date:
        """Retorna la fecha en que se creó la orden."""
        return self.__fecha

    @property
    def estado(self) -> str:
        """Retorna el estado actual de la orden."""
        return self.__estado

    @property
    def cliente(self) -> Cliente:
        """Retorna el cliente que realizó la orden."""
        return self.__cliente

    @property
    def pago(self) -> Pago:
        """Retorna el método de pago asociado a la orden."""
        return self.__pago

    @property
    def detalles(self) -> list[DetallePedido]:
        """Retorna la lista de detalles de productos de la orden."""
        return self.__detalles

    # --------------------Metodos--------------------------------------------------

    def calcular_total(self) -> float:
        """Calcula y retorna el valor total de la orden sumando los subtotales."""
        return sum(detalle.subtotal() for detalle in self.detalles)

    def confirmar(self) -> None:
        """Confirma la orden verificando stock y procesando el pago."""
        if self.__estado != EstadoOrden.PENDIENTE:
            raise ValueError(
                f"Solo se puede confirmar una orden pendiente. "
                f"Estado actual: {self.__estado}"
            )
        if self.__inventario:
            for detalle in self.__detalles:
                if not self.__inventario.verificar_disponibilidad(
                    detalle.producto.numero_producto
                ):
                    raise ValueError(
                        f"Sin stock para: {detalle.producto.descripcion}"
                    )
        if not self.__pago.procesar_pago():
            raise ValueError("El pago no pudo procesarse.")
        self.__estado = EstadoOrden.CONFIRMADA
        print(f"Orden {self.__numero_orden} confirmada con éxito.")

    def cancelar(self) -> None:
        """Cancela la orden si aún no ha sido entregada."""
        if self.__estado == EstadoOrden.ENTREGADA:
            raise ValueError("Ya no se puede cancelar, la orden fue entregada.")
        self.__estado = EstadoOrden.CANCELADA
        print(f"Orden {self.__numero_orden} cancelada.")

    def __str__(self) -> str:
        """Retorna una representación legible de la orden de compra."""
        detalles_str = "".join(
            f"    [{d.producto.numero_producto}] {d.producto.descripcion}"
            f"  x{d.cantidad}  —  ${d.subtotal():,.2f}\n"
            for d in self.__detalles
        )
        return (
            f"  ORDEN # {self.__numero_orden}\n"
            f"  fecha   : {self.__fecha}\n"
            f"  estado  : {self.__estado}\n"
            f"  cliente : {self.__cliente.nombre}\n"
            f"  total   : ${self.calcular_total():,.2f}\n"
            f"  detalle :\n{detalles_str}"
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

    print("=== Prueba: OrdenCompra ===\n")

    # Instancias fijas
    cliente = Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co")
    prod1 = Producto(101, "Ferrari",     90_000.00, 10)
    prod2 = Producto(102, "Lamborghini", 50_000.00, 50)
    prod3 = Producto(103, "Porsche",     80_000.00, 25)
    productos = [prod1, prod2, prod3]

    # Selección interactiva de productos
    print("-- Productos disponibles --")
    for p in productos:
        print(f"  [{p.numero_producto}] {p.descripcion}  —  ${p.precio:,.2f}")

    detalles = []
    while True:
        try:
            cod = int(input("\nCódigo del producto (0 para terminar): "))
        except ValueError:
            print("Código inválido.")
            continue
        if cod == 0:
            break
        prod = next((p for p in productos if p.numero_producto == cod), None)
        if not prod:
            print("Producto no encontrado.")
            continue
        try:
            qty = int(input(f"Cantidad de '{prod.descripcion}': "))
            detalles.append(DetallePedido(prod, qty))
        except ValueError as e:
            print(f"Error: {e}")

    if not detalles:
        print("Sin productos, orden no creada.")
    else:
        print("\n-- Resumen de la orden --")
        for d in detalles:
            print(f"  [{d.producto.numero_producto}] {d.producto.descripcion}  x{d.cantidad}  —  ${d.subtotal():,.2f}")
        print(f"  TOTAL: ${sum(d.subtotal() for d in detalles):,.2f}")

        print("\n-- Datos de pago --")
        numero_tarjeta = input("Número de tarjeta (16 dígitos): ").strip()
        titular        = input("Titular            : ").strip()
        vencimiento    = input("Vencimiento (MM/AA): ").strip()
        cvv            = input("CVV (3 dígitos)    : ").strip()
        try:
            total = sum(d.subtotal() for d in detalles)
            pago  = PagoTarjeta(1001, total, numero_tarjeta, titular, vencimiento, cvv)
            orden = OrdenCompra(1001, cliente, pago, detalles)
            orden.confirmar()
            print(f"\n{orden}")
            print("Orden pagada exitosamente.")

            otra = input("\n¿Desea hacer otra orden? (s/n): ").strip().lower()
            if otra != "s":
                print("Hasta luego.")
        except ValueError as e:
            print(f"Error: {e}")
