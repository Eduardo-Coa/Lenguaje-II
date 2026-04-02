import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.Usuario import Usuario
from Clases.Queja import Queja


class GerenteRelaciones(Usuario):
    """
    Representa al gerente de relaciones del sistema TeleVentas.

    Extiende Usuario y es responsable de recibir y gestionar
    las quejas remitidas por los clientes.
    """

    def __init__(
        self,
        user_id: str,
        contrasena: str,
        nombre: str
    ) -> None:
        """Inicializa el gerente con sus credenciales y una lista vacía de quejas."""
        super().__init__(user_id, nombre, contrasena)
        # Lista que acumula las quejas recibidas durante la sesión
        self.__quejas = []

    @property
    def quejas(self) -> list:
        """Retorna la lista de quejas recibidas por el gerente."""
        return self.__quejas
    
    
    # --------------------Metodos--------------------------------------------------

    def recibir_queja(self, queja: Queja) -> None:
        """Recibe una queja ya remitida y la agrega a la lista del gerente."""
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
        """Retorna una representación legible del gerente."""
        return (
            f"  GERENTE DE RELACIONES\n"
            f"  id     : {self.user_id}\n"
            f"  nombre : {self.nombre}\n"
            f"  quejas : {len(self.__quejas)}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    from Clases.Cliente import Cliente
    from Clases.Queja import Queja

    print("=== Prueba: GerenteRelaciones ===\n")

    # Instancias fijas
    gerente = GerenteRelaciones("ger01", "ger123", "Diunis Pérez")
    cliente = Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co")

    # Queja fija ya creada y remitida, lista para ser recibida
    queja = Queja(1, "Demora en la entrega del pedido", cliente)
    queja.remitir_gerente()

    print(f"{gerente}")

    # Parte interactiva: el gerente recibe la queja
    print("-- Recibir queja --")
    input("Presione ENTER para que el gerente reciba la queja...")
    try:
        gerente.recibir_queja(queja)
        print(f"\n{queja}")
        print(f"Quejas recibidas por el gerente: {len(gerente.quejas)}")
    except ValueError as e:
        print(f"Error: {e}")
