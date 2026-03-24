from abc import ABC, abstractmethod
from datetime import date

class Pago(ABC):

    def __init__(
        self,
        numero_referencia: int,
        monto:float
    )->None:
        if monto <=0:
            raise ValueError ("El monto debe ser mayor a cero")
        
        self.__numero_referencia =numero_referencia
        self.__monto = monto
        self.__estado = "pendiente"
        self.__fecha =date.today()

    @property
    def numero_referencia(self)->int:
        return self.__numero_referencia
    
    @property
    def monto(self)->float:
        return self.__monto
    
    @property
    def estado(self)->str:
        return self.__estado
    
    @property
    def fecha(self)->date:
        return self.__fecha
    
    @estado.setter
    def estado(self, nuevo_estado: str)->None:
        estados_validos =["pendiente", "aprobado", "rechazado"]
        if nuevo_estado not in estados_validos:
            raise ValueError(f"Estado invalido, escoja uno de {estados_validos}: ")
        self.__estado = nuevo_estado

    @abstractmethod
    def procesar_pago(self)-> bool:
        pass

    def __str__(self) -> str:
        return (
            f"Pago(ref={self.__numero_referencia}, "
            f"monto={self.__monto:.2f}, "
            f"estado={self.__estado}, "
            f"fecha={self.__fecha})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()