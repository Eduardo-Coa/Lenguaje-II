import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date
from Clases.Cliente import Cliente


class Queja:
    """
    Representa una queja presentada por un cliente en el sistema TeleVentas.

    Registra el motivo, la fecha y el estado del reclamo, y permite
    remitirla al gerente de relaciones para su atención.
    """

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
        """Inicializa una queja validando que el motivo no esté vacío."""
        if not motivo or not motivo.strip():
            raise ValueError("El motivo de la queja no puede estar vacío.")

        self.__numero_queja = numero_queja
        self.__fecha = date.today()
        self.__motivo = motivo.strip()
        self.__estado = Queja.REGISTRADA
        self.__cliente = cliente

    @property
    def numero_queja(self) -> int:
        """Retorna el número identificador de la queja."""
        return self.__numero_queja

    @property
    def fecha(self) -> date:
        """Retorna la fecha en que se registró la queja."""
        return self.__fecha

    @property
    def motivo(self) -> str:
        """Retorna el motivo de la queja ."""
        return self.__motivo

    @property
    def estado(self) -> str:
        """Retorna el estado actual de la queja."""
        return self.__estado

    @property
    def cliente(self) -> Cliente:
        """Retorna el cliente que presentó la queja."""
        return self.__cliente

    # --------------------Metodos--------------------------------------------------

    def registrar_queja(self) -> None:
        """Confirma el registro de la queja si aún no ha sido procesada."""
        if self.__estado != Queja.REGISTRADA:
            raise ValueError(
                f"La queja ya fue procesada. Estado: {self.__estado}"
            )
        print(
            f"Queja # {self.__numero_queja} registrada. \n"            
        )

    def remitir_gerente(self) -> None:
        """Cambia el estado de la queja a EN_REVISION y la remite al gerente."""
        if self.__estado != Queja.REGISTRADA:
            raise ValueError(
                f"La queja ya fue procesada. Estado: {self.__estado}"
            )
        self.__estado = Queja.EN_REVISION
        print(
            f"Queja #{self.__numero_queja} remitida al gerente.\n"
            f"  Cliente: {self.__cliente.nombre}.\n"
        )

    def __str__(self) -> str:
        """Retorna una representación legible de la queja."""
        return (
            f"QUEJA # {self.__numero_queja}\n"
            f"  fecha  : {self.__fecha}\n"
            f"  motivo : {self.__motivo}\n"
            f"  estado : {self.__estado}\n"
            f"  cliente: {self.__cliente.nombre}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    from Clases.Cliente import Cliente

    print("=== Prueba: Queja ===\n")

    # Instancias fijas
    cliente = Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co")

    # Parte interactiva: ingresar motivo de la queja
    motivo = input("Ingrese el motivo de la queja: ").strip()
    if motivo:
        try:
            queja = Queja(1, motivo, cliente)
            queja.registrar_queja()
            print(f"\n{queja}")

            input("Presione ENTER para remitir la queja al gerente...")
            queja.remitir_gerente()
            print(f"\n{queja}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Motivo vacío, queja no registrada.")
