from abc import ABC, abstractmethod
class ITransportadora(ABC):
    
    @abstractmethod
    def recibir_pedido(self,pedido) ->bool:
        pass

    @abstractmethod
    def confirmar_entrega(self)->bool:
        pass

    @abstractmethod
    def get_estado_envio(self)->str:
        pass