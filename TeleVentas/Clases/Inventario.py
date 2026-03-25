from Interfaces.IInvetario import IInventario

class Inventario(IInventario):
    def __init__(
        self,
        url_api: str,
        nombre: str        
    ) ->None:
        
        self.__url_api= url_api
        self.__nombre= nombre
        self.__productos= {}

    @property
    def url_api(self) -> str:       
        return self.__url_api

    @property
    def nombre(self) -> str:        
        return self.__nombre
    

    def registrar_producto(self, codigo: int, descripcion: str,precio: float, stock: int) -> None:
        self.__productos[codigo]={
            "codigo": codigo,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock
        }
        print(f"Producto '{descripcion}' registrado en inventario.")

    def consultar_producto(self,codigo:int) -> dict:
        if codigo not in self.__productos:
            raise ValueError(
                f"Producto con código {codigo} no encontrado en inventario."
            )
        return self.__productos[codigo]    
        
    def actualizar_stock(self, codigo:int, qty:int)-> None:
        producto= self.consultar_producto(codigo)
        if producto["stock"] <qty:
            raise ValueError(
                f"Stock insuficiente para producto {codigo}. "
                f"Disponible: {producto['stock']}, solicitado: {qty}"
            )
        self.__productos[codigo]["stock"] -= qty
        print(
            f"Stock actualizado — producto {codigo}: "
            f"{producto['stock'] + qty} → {self.__productos[codigo]['stock']}"
        )   

    def verificar_disponibilidad(self, codigo: int) -> bool:
        try:
            producto = self.consultar_producto(codigo)
            return producto["stock"] > 0
        except ValueError:
            return False
 
    def __str__(self) -> str:
        return (
            f"Inventario(nombre={self.__nombre}, "
            f"url={self.__url_api}, "
            f"productos={len(self.__productos)})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()