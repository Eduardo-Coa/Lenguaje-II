from Clases.OrdenCompra import OrdenCompra
from Interfaces.ITransportadora import ITransportadora
from Interfaces.IInvetario import IInventario
from Clases.DetallePedido import DetallePedido
from Clases.Producto import Producto


class Pedido:
    PENDIENTE = "pendiente"
    EMPACADO = "empacado"
    TRANSPORTE_ASIGNADO = "transporte_asignado"
    EN_DESPACHO = "en_despacho"

    def __init__(
        self,
        numero_pedido:int,
        orden: OrdenCompra,
        inventario:IInventario= None
    )-> None:
        self.__numero_pedido = numero_pedido
        self.__orden = orden
        self.__estado = Pedido.PENDIENTE
        self.__transportadora = None
        self.__inventario =inventario

    @property
    def numero_pedido(self) -> int:
        return self.__numero_pedido
 
    @property
    def orden(self)-> OrdenCompra:
        return self.__orden
 
    @property
    def estado(self) -> str:
        return self.__estado
 
    @property
    def transportadora(self)-> ITransportadora:
        return self.__transportadora
    
    "Metodos"

    def empacar(self)-> None:
        if self.__estado !=Pedido.PENDIENTE:
            raise ValueError(
                f"El pedido ya fue empacado. Estado: {self.__estado}"
            )
        if self.__orden.estado != "confirmada":
            raise ValueError(
                "Solo se pueden empacar órdenes confirmadas"
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
    
    def asignar_transporte(self, empresa:ITransportadora) -> None:
        if self.__estado != Pedido.EMPACADO:
            raise ValueError(
                "El pedido debe estar empacado antes de asignar transporte"
            )
        if not isinstance(empresa, ITransportadora):
            raise ValueError(
                "La empresa debe implementar ITransportadora"
            )
 
        self.__transportadora = empresa
        self.__estado = Pedido.TRANSPORTE_ASIGNADO
        print(f"Transportadora asignada al pedido {self.__numero_pedido}.")
 
        if empresa.recibir_pedido(self):
            self.__estado = Pedido.EN_DESPACHO
            print(f"Pedido {self.__numero_pedido} en despacho.")

    def __str__(self) -> str:        
        transp = (
            self.__transportadora.get_estado_envio()
            if self.__transportadora
            else "sin asignar"
        )
        return (
            f"Pedido(num={self.__numero_pedido}, "
            f"estado={self.__estado}, "
            f"orden={self.__orden.numero_orden}, "
            f"envio={transp})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()