from __future__ import annotations
from datetime import date
from Clases.Pago import Pago
from Clases.DetallePedido import DetallePedido
from Interfaces.IInvetario import IInventario
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Clases.Cliente import Cliente


class EstadoOrden:
    PENDIENTE = "pendiente"
    CONFIRMADA ="confirmada"
    CANCELADA = "cancelada"
    EN_DESPACHO = "en_despacho"
    ENTREGADA = "entregada"

class OrdenCompra:
    def __init__(
        self,
        numero_orden: int,
        cliente : Cliente,
        pago: Pago,
        detalles: list[DetallePedido],
        inventario: IInventario = None
    )-> None:
        if not detalles:
            raise ValueError("la orden debe tener al menos un producto")
        
        self.__numero_orden= numero_orden
        self.__fecha= date.today()
        self.__estado= EstadoOrden.PENDIENTE
        self.__cliente= cliente
        self.__pago= pago
        self.__detalles= detalles
        self.__inventario= inventario

    @property
    def numero_orden(self)-> int:
        return self.__numero_orden

    @property
    def fecha(self)-> date:
        return self.__fecha
    
    @property
    def estado(self)-> str:
        return self.__estado
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def pago(self):
        return self.__pago
    
    @property
    def detalles(self)-> list[DetallePedido]:
        return self.__detalles
    
    
    """ Metodos """    

    def calcular_total(self)-> float:
        return sum(detalle.subtotal() for detalle in self.detalles)
    
    def confirmar(self)->None:
        if self.__estado != EstadoOrden.PENDIENTE:
            raise ValueError(
                f"solo se puede confirmar una orden pendiente"
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
            raise ValueError ("el pago no pudo procesarse")
        self.__estado = EstadoOrden.CONFIRMADA
        print(f"Orden {self.__numero_orden} confirmada con exito.")

    def cancelar(self)->None:
        if self.__estado == EstadoOrden.ENTREGADA:
            raise ValueError("Ya no se puede cancelar, la orden fue entregada")
        self.__estado = EstadoOrden.CANCELADA
        print(f"Orden {self.__numero_orden} cancelada")  

    def __str__(self) -> str:
        return (
            f"OrdenCompra(num={self.__numero_orden}, "
            f"fecha={self.__fecha}, "
            f"estado={self.__estado}, "
            f"cliente={self.__cliente.nombre}, "
            f"total={self.calcular_total():.2f})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()