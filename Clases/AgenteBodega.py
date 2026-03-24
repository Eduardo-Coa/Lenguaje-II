from Clases.OrdenCompra import OrdenCompra
from Clases.Pedido import Pedido
from Clases.Usuario import Usuario
from Interfaces.ITransportadora import ITransportadora


class AgenteBodega(Usuario):
    def __init__(
        self,
        user_id: str,
        contrasena: str,
        numero_bodega: int,
        nombre: str
        
        )->None:        
        super().__init__(user_id,nombre,contrasena)
        self.__numero_bodega = numero_bodega
        self.__nombre = nombre.strip()

    @property
    def numero_bodega(self) ->int:
        return self.__numero_bodega
    
    @property
    def nombre(self)-> str:
        return self.__nombre
    
    "Metodos"

    def consultar_orden(self, orden: OrdenCompra)->None:
        if orden.estado !="confirmada":
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
    
    def asignar_transporte(
        self,
        pedido: Pedido,
        empresa: ITransportadora
    )-> None:
        print(
            f"Agente {self.__nombre} asignando transporte "
            f"al pedido {pedido.numero_pedido}."
        )
        pedido.asignar_transporte(empresa)
    
    def __str__(self) -> str:
        return (
            f"AgenteBodega(num={self.__numero_bodega}, "
            f"nombre={self.__nombre})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()