import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.OrdenCompra import OrdenCompra
from Clases.Usuario import Usuario
from Clases.Catalogo import Catalogo


class Cliente(Usuario):
    """
    Representa a un cliente del sistema TeleVentas.

    Extiende Usuario con dirección y correo, y permite consultar el catálogo,
    crear y cancelar órdenes de compra, y presentar quejas.
    """

    def __init__(
        self,
        user_id: str,
        nombre: str,
        contrasena: str,
        direccion: str,
        correo: str,
    ) -> None:
        """Inicializa un cliente con sus datos personales y credenciales."""
        super().__init__(user_id, nombre, contrasena)
        self.__direccion = direccion
        self.__correo = correo

    @property
    def direccion(self) -> str:
        """Retorna la dirección de entrega del cliente."""
        return self.__direccion

    @property
    def correo(self) -> str:
        """Retorna el correo electrónico del cliente."""
        return self.__correo

    @direccion.setter
    def direccion(self, nueva_direccion: str) -> None:
        """Actualiza la dirección de entrega del cliente validando que no esté vacía."""
        if not nueva_direccion or not nueva_direccion.strip():
            raise ValueError("La dirección no puede estar vacía.")
        self.__direccion = nueva_direccion

    @correo.setter
    def correo(self, nuevo_correo: str) -> None:
        """Actualiza el correo electrónico del cliente validando que no esté vacío."""
        if not nuevo_correo or not nuevo_correo.strip():
            raise ValueError("El correo no puede estar vacío.")
        self.__correo = nuevo_correo
    
    # --------------------Metodos--------------------------------------------------

    def consultar_catalogo(self, catalogo: Catalogo) -> list:
        """Retorna la lista de productos disponibles en el catálogo."""
        return catalogo.lista_productos()

    def suscribir_catalogo(self, catalogo: Catalogo) -> None:
        """Suscribe al cliente para recibir el catálogo por correo."""
        catalogo.suscribir(self)
        print(f"Cliente {self.nombre} suscrito al catálogo.")

    def crear_orden(self, numero_orden: int, detalles: list, pago) -> OrdenCompra:
        """Crea y retorna una nueva orden de compra con los detalles y metodo de pago ."""
        orden = OrdenCompra(numero_orden, self, pago, detalles)
        print(f"Orden creada para cliente {self.nombre}.")
        return orden

    def cancelar_orden(self, orden: OrdenCompra) -> None:
        """Cancela una orden de compra existente del cliente."""
        orden.cancelar()
        print(f"Orden cancelada para cliente {self.nombre}.")

    def presentar_queja(self, numero_queja: int, motivo: str):
        """Registra y retorna una queja del cliente indicando el motivo."""
        from Clases.Queja import Queja
        queja = Queja(numero_queja, motivo, self)
        print(f"Queja registrada, Cliente: {self.nombre}.")
        return queja

    def __str__(self) -> str:
        """Retorna una representación legible del cliente."""
        return (
            f"  CLIENTE ID : {self.user_id}\n"
            f"  Nombre     : {self.nombre}\n"
            f"  email      : {self.__correo}\n"
            f"  Direccion  : {self.__direccion}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()

# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------ 
if __name__ == "__main__":
    
    from Clases.Producto import Producto
    from Clases.DetallePedido import DetallePedido
    from Clases.PagoTarjeta import PagoTarjeta

    print("=== Prueba: clase Cliente ===\n")

    # Datos del cliente
    print("-- Registro de cliente --")
    cliente = Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co")
    print(f"{cliente}\n")

    # Productos disponibles para la prueba
    productos = [
        Producto(101, "Ferrari",  90_000.00, 10),
        Producto(102, "Lamborghini",   50_000.00, 50),
        Producto(103, "Porsche", 80_000.00, 25),
    ]

    # --- Crear orden ---
    print("-- Crear orden de compra --")
    for p in productos:
        print(f"  [{p.numero_producto}] {p.descripcion}  —  ${p.precio:,.2f}")

    detalles = []
    while True:
        try:
            cod = int(input("\nCódigo del producto (0 para terminar): "))
        except ValueError:
            print("Código inválido.")
            continue
        if cod == 0:
            break
        prod = next((p for p in productos if p.numero_producto == cod), None)
        if not prod:
            print("Producto no encontrado.")
            continue
        try:
            qty = int(input(f"Cantidad de '{prod.descripcion}': "))
            detalles.append(DetallePedido(prod, qty))
        except ValueError as e:
            print(f"Error: {e}")

    
    # --- Presentar queja ---
    print("\n-- Presentar queja --")
    motivo = input("Ingrese el motivo de su queja: ").strip()
    if motivo:
        try:
            queja = cliente.presentar_queja(1, motivo)
            queja.remitir_gerente()
            print(f"\n{queja}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Motivo vacío, queja no registrada.")
