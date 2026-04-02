import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from abc import ABC, abstractmethod
from datetime import date


class Pago(ABC):
    """
    Clase abstracta que representa un método de pago en TeleVentas.

    Define la estructura común para todos los tipos de pago del sistema.
    Cada subclase debe implementar procesar_pago() con su lógica específica.
    """

    def __init__(
        self,
        numero_referencia: int,
        monto: float
    ) -> None:
        """Inicializa el pago validando que el monto sea mayor a cero."""
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")

        self.__numero_referencia = numero_referencia
        self.__monto             = monto
        self.__estado            = "pendiente"
        self.__fecha             = date.today()

    @property
    def numero_referencia(self) -> int:
        """Retorna el número de referencia del pago (solo lectura)."""
        return self.__numero_referencia

    @property
    def monto(self) -> float:
        """Retorna el monto del pago (solo lectura)."""
        return self.__monto

    @property
    def estado(self) -> str:
        """Retorna el estado actual del pago (solo lectura)."""
        return self.__estado

    @property
    def fecha(self) -> date:
        """Retorna la fecha en que se registró el pago (solo lectura)."""
        return self.__fecha

    @estado.setter
    def estado(self, nuevo_estado: str) -> None:
        """Actualiza el estado del pago validando que sea un valor permitido."""
        estados_validos = ["pendiente", "aprobado", "rechazado"]
        if nuevo_estado not in estados_validos:
            raise ValueError(f"Estado inválido. Escoja uno de: {estados_validos}")
        self.__estado = nuevo_estado

    @abstractmethod
    def procesar_pago(self) -> bool:
        """Procesa el pago según el método específico. Debe implementarse en cada subclase."""
        pass

    def __str__(self) -> str:
        """Retorna una representación legible del pago."""
        return (
            f"  PAGO\n"
            f"  referencia : {self.__numero_referencia}\n"
            f"  monto      : ${self.__monto:,.2f}\n"
            f"  estado     : {self.__estado}\n"
            f"  fecha      : {self.__fecha}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()
