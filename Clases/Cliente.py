from Clases.OrdenCompra import OrdenCompra
from Clases.Usuario import Usuario 
from Clases.Catalogo import Catalogo

class Cliente(Usuario):

    def __init__(
        self,
        user_id: str,
        nombre:str,
        contrasena:str,
        direccion: str,
        correo: str,
       
     )-> None:
        super().__init__(user_id,nombre,contrasena)
        self.__direccion= direccion
        self.__correo = correo

    @property
    def direccion(self)->str:
         return self.__direccion
    
    @property
    def correo(self)->str:
         return self.__correo

    def consultar_catalogo(self, catalogo:Catalogo)-> list:
         return catalogo.lista_productos()
    
    def suscribir_catalogo(self, catalogo:Catalogo)-> None:
         catalogo.suscribir(self)
         print(f"cliente{self.nombre} suscrito al catálogo.")

    def crear_orden(self, numero_orden: int, detalles: list, pago):
         orden=OrdenCompra(numero_orden, self, pago, detalles)
         print(f"Orden creada para cliente {self.nombre}.")
         return orden
    
    def cancelar_orden(self, orden:OrdenCompra) -> None:       
         orden.cancelar()
         print(f"Orden cancelada para cliente {self.nombre}. ")

    def presentar_queja(self, numero_queja: int, motivo: str):
         from Clases.Queja import Queja
         queja=Queja(numero_queja, motivo, self)
         print (f"Queja registrada para el cliente {self.nombre}.")
         return queja
    
    def __str__(self)->str:
         return (
            f"Cliente(id={self.user_id}, nombre={self.nombre}, "
            f"email={self.__correo}, direccion={self.__direccion})")
    
    def __repr__(self) -> str:
         return self.__str__()