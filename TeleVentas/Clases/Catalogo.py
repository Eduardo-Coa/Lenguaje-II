from __future__ import annotations
from datetime import date
from Clases.Producto import Producto
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Clases.Cliente import Cliente

class Catalogo:
    def __init__(
        self,
        numero_catalogo: int,
        productos: list[Producto] = None
    ) -> None:
        self.__numero_catalogo= numero_catalogo
        self.__fecha= date.today()
        self.__productos= productos if productos else []
        self.__suscriptores= []

    @property
    def numero_catalogo(self) -> int:    
        return self.__numero_catalogo
 
    @property
    def fecha(self) -> date:
        return self.__fecha
 
    @property
    def productos(self) -> list:
        return self.__productos    
    
    def lista_productos(self) -> list:
        return [p.get_info() for p in self.__productos]
 
    def buscar_producto(self, termino: str) -> list:    
        resultados = [
            p for p in self.__productos
            if termino.lower() in p.descripcion.lower()
        ]
        if not resultados:
            print(f"No se encontraron productos con '{termino}'.")
        return resultados
 
    def suscribir(self, cliente:Cliente) -> None:       
        if cliente in self.__suscriptores:
            raise ValueError(
                f"El cliente {cliente.nombre} ya está suscrito."
            )
        self.__suscriptores.append(cliente)
        print(
            f"Cliente {cliente.nombre} suscrito al "
            f"catálogo {self.__numero_catalogo}."
        )
 
    def enviar_catalogo(self, cliente:Cliente) -> None:       
        print(
            f"Catálogo {self.__numero_catalogo} enviado "
            f"a {cliente.correo}."
        )
        for producto in self.__productos:
            info: dict = producto.get_info()
            print(
                f"  - {info['descripcion']} "
                f"| Precio: ${info['precio']:.2f} "
                f"| Stock: {info['cantidad_disponible']}"
            )
 
    def agregar_producto(self, producto: Producto) -> None:        
        if producto in self.__productos:
            raise ValueError(
                f"El producto {producto.descripcion} ya está en el catálogo."
            )
        self.__productos.append(producto)
        print(f"Producto '{producto.descripcion}' agregado al catálogo.")
 
    def __str__(self) -> str:
        return (
            f"Catalogo(num={self.__numero_catalogo}, "
            f"fecha={self.__fecha}, "
            f"productos={len(self.__productos)}, "
            f"suscriptores={len(self.__suscriptores)})"
        )
 
    def __repr__(self) -> str:
        return self.__str__()
 