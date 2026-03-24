from Clases.Producto import Producto

class DetallePedido:
    
    def __init__(
        self,
        producto:Producto,
        cantidad:int
    )-> None:
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser mayor a cero")
        
        self.__producto= producto
        self.__cantidad= cantidad
        self.__precio_unidad=producto.precio

    @property
    def producto(self)-> Producto:
         return self.__producto
    
    @property
    def cantidad(self)->int:
         return self.__cantidad
    
    @property
    def precio_unidad(self)->str:
         return self.__precio_unidad
    
    "Metodos"

    def subtotal(self)-> float:
        return self.__cantidad * self.precio_unidad
    
    def get_producto(self)-> Producto:
        return self.__producto
    
    def __str__(self) -> str:
        return (
            f"DetallePedido(producto={self.__producto.descripcion}, "
            f"cantidad={self.__cantidad}, "
            f"precio_unidad={self.__precio_unidad:.2f}, "
            f"subtotal={self.subtotal():.2f})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()