from Interfaces.ITransportadora import ITransportadora
from Clases.Pedido import Pedido

class Transportadora(ITransportadora):
    SIN_PEDIDO= "sin_pedido"
    RECIBIDO= "recibido"
    EN_CAMINO= "en_camino"
    ENTREGADO= "entregado"

    def __init__(
        self,
        id: int,
        nombre: str
    )->None:
        
        self.__id= id
        self.__nombre= nombre
        self.__estado= Transportadora.SIN_PEDIDO
        self.__pedido= None

    @property
    def id(self)-> int:
        return self.__id
    
    @property
    def nombre(self)-> str:
        return self.__nombre
    
    "Metodos"

    def recibir_pedido(self, pedido:Pedido)-> bool:
        if self.__estado != Transportadora.SIN_PEDIDO:
            print(
                f"Transportadora {self.__nombre} ya tiene un pedido asignado."
            )
            return False
        
        self.__pedido= pedido
        self.__estado= Transportadora.RECIBIDO
        print(
            f"Transportadora {self.__nombre} recibió el pedido "
            f"{pedido.numero_pedido}."
        )
        self.__estado= Transportadora.EN_CAMINO
        print(f"Pedido en camino con {self.__nombre}.")
        return True
    
    def confirmar_entrega(self)-> bool:
        if self.__estado != Transportadora.EN_CAMINO:
            raise ValueError(
                f"No hay pedido en camino. Estado actual: {self.__estado}"
            )
        self.__estado= Transportadora.ENTREGADO
        print(
            f"Transportadora {self.__nombre} confirmó la entrega "
            f"del pedido {self.__pedido.numero_pedido}."
        )
        return True
    
    def get_estado_envio(self)->str:
        return self.__estado
    
    def __str__(self) -> str:
        return (
            f"Transportadora(id={self.__id}, "
            f"nombre={self.__nombre}, "
            f"estado={self.__estado})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()