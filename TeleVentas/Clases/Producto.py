class Producto:

    def __init__(
            self,
            numero_producto: int,
            descripcion: str,
            precio: float,
            cantidad_disponible:int
    )-> None:
        if precio < 0:
            raise ValueError("el precio no debe ser negativo")
        
        if cantidad_disponible < 0:
            raise ValueError("la cantidad disponible no puede ser negativa")
        
        self.__numero_producto= numero_producto
        self.__descripcion= descripcion
        self.__precio= precio
        self.__cantidad_disponible= cantidad_disponible

    @property
    def numero_producto(self)-> int:
        return self.__numero_producto
    
    @property
    def descripcion(self)-> str:
        return self.__descripcion
    
    @property
    def precio(self)-> float:
        return self.__precio
    
    @property
    def cantidad_disponible(self)-> int:
        return self.__cantidad_disponible
    
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = nuevo_precio
 
    @cantidad_disponible.setter
    def cantidad_disponible(self, nueva_cantidad: int) -> None:
        if nueva_cantidad < 0:
            raise ValueError("La cantidad disponible no puede ser negativa")
        self.__cantidad_disponible = nueva_cantidad

    
    def get_info(self) ->dict:
        return{
            "numero_producto": self.__numero_producto,
            "descripcion": self.__descripcion,
            "precio": self.__precio,
            "cantidad_disponible": self.__cantidad_disponible
        }
    
    def actualizar(
            self,
            precio: float=None,
            cantidad: int=None
    )-> None:
        if precio is not None:
            self.precio= precio
        if cantidad is not None:
            self.cantidad_disponible= cantidad

    def __str__(self)-> str:
        return (
            f"Producto(num={self.__numero_producto}, "
            f"descripcion={self.__descripcion}, "
            f"precio={self.__precio}, "
            f"disponible={self.__cantidad_disponible})"
        )
    
    def __repr__(self) -> str:
        return self.__str__()