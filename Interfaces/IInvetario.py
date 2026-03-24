from abc import ABC, abstractmethod

class IInventario(ABC):

    @abstractmethod
    def consultar_producto(self, codigo:int)->dict:
        pass

    @abstractmethod
    def actualizar_stock(self, codigo:int, qty:int)->None:
        pass

    @abstractmethod
    def verificar_disponibilidad(self, codigo:int)->bool:
        pass
    