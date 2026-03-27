from datetime import date
from Clases.Cliente import Cliente
 
 
class Queja:
 
    # Estados válidos
    REGISTRADA  = "registrada"
    EN_REVISION = "en_revision"
    RESUELTA    = "resuelta"
    CERRADA     = "cerrada"
 
    def __init__(
        self,
        numero_queja: int,
        motivo: str,
        cliente: Cliente
    ) -> None:
        if not motivo or not motivo.strip():
            raise ValueError("El motivo de la queja no puede estar vacío")
 
        self.__numero_queja = numero_queja
        self.__fecha= date.today()
        self.__motivo= motivo.strip()
        self.__estado= Queja.REGISTRADA
        self.__cliente= cliente
 
    
 
    @property
    def numero_queja(self) -> int:
        return self.__numero_queja
 
    @property
    def fecha(self) -> date:
        return self.__fecha
 
    @property
    def motivo(self) -> str:
        return self.__motivo
 
    @property
    def estado(self) -> str:
        return self.__estado
 
    @property
    def cliente(self) -> Cliente:
        return self.__cliente
 
    "Métodos"
 
    def registrar_queja(self) -> None:
       
        if self.__estado != Queja.REGISTRADA:
            raise ValueError(
                f"La queja ya fue procesada. Estado: {self.__estado}"
            )
        print(
            f"Queja {self.__numero_queja} registrada. "
            f"Cliente: {self.__cliente.nombre}. "
            f"Motivo: {self.__motivo}"
        )
 
    def remitir_gerente(self) -> None:
        if self.__estado != Queja.REGISTRADA:
            raise ValueError(
                f"La queja ya fue procesada. Estado: {self.__estado}"
            )
        self.__estado = Queja.EN_REVISION
        print(
            f"Queja {self.__numero_queja} remitida al gerente. "
            f"Cliente: {self.__cliente.nombre}. "
            f"Motivo: {self.__motivo}"
        )
 
    def __str__(self) -> str:
        return (
            f"QUEJA # {self.__numero_queja} \n"
            f"  fecha  : {self.__fecha}\n"
            f"  motivo : {self.__motivo}\n"
            f"  estado : {self.__estado}\n"
            f"  cliente: {self.__cliente.nombre}\n"
            
        )
 
    def __repr__(self) -> str:
        return self.__str__()