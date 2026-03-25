from Clases.Usuario import Usuario 
from Clases.Queja import Queja

class GerenteRelaciones(Usuario):

    def __init__(
        self,
        user_id: str,
        contrasena: str,
        nombre: str            
    )-> None:
        super().__init__(user_id,nombre,contrasena)
        self.__quejas = []


    "Metodos"

    def recibir_queja(self, queja:Queja)-> None:
        if queja.estado != Queja.EN_REVISION:
            raise ValueError(
                f"La queja no ha sido remitida aún. "
                f"Estado actual: {queja.estado}"
            )
        self.__quejas.append(queja)
        print(
            f"Gerente {self.nombre} recibió la queja {queja.numero_queja}. "
            f"Cliente: {queja.cliente.nombre}. "
            f"Motivo: {queja.motivo}"
        )
            
    def __str__(self) -> str:
        return (
            f"GerenteRelaciones(id={self.user_id}, "
            f"nombre={self.nombre}, "
            f"quejas_recibidas={len(self.__quejas)})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()