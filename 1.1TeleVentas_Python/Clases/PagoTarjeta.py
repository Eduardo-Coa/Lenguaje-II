import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.Pago import Pago


class PagoTarjeta(Pago):
    """
    Representa un pago con tarjeta de crédito en TeleVentas.

    Extiende Pago con los datos específicos de la tarjeta y valida
    que la información sea correcta antes de procesar el cobro.
    """

    def __init__(
        self,
        numero_referencia: int,
        monto: float,
        numero_tarjeta: str,
        titular: str,
        vencimiento: str,
        cvv: str,
    ) -> None:
        """Inicializa el pago con tarjeta con los datos del titular y la tarjeta."""
        super().__init__(numero_referencia, monto)
        self.__numero_tarjeta = numero_tarjeta
        self.__titular        = titular
        self.__vencimiento    = vencimiento
        self.__cvv            = cvv

    @property
    def numero_tarjeta(self) -> str:
        """Retorna el número de tarjeta enmascarado, mostrando solo los últimos 4 dígitos."""
        return f"**** **** **** {self.__numero_tarjeta[-4:]}"

    @property
    def titular(self) -> str:
        """Retorna el nombre del titular de la tarjeta (solo lectura)."""
        return self.__titular

    @property
    def vencimiento(self) -> str:
        """Retorna la fecha de vencimiento de la tarjeta (solo lectura)."""
        return self.__vencimiento

    # --------------------Metodos--------------------------------------------------

    def validar_tarjeta(self) -> bool:
        """Valida que los datos de la tarjeta tengan el formato correcto."""
        numero_valido     = len(self.__numero_tarjeta) == 16 and self.__numero_tarjeta.isdigit()
        cvv_valido        = len(self.__cvv) == 3 and self.__cvv.isdigit()
        vencimiento_valido = len(self.__vencimiento) == 5 and "/" in self.__vencimiento
        titular_valido    = bool(self.__titular.strip())
        return numero_valido and cvv_valido and vencimiento_valido and titular_valido

    def procesar_pago(self) -> bool:
        """Valida la tarjeta y procesa el pago, actualizando el estado según el resultado."""
        if not self.validar_tarjeta():
            self.estado = "rechazado"
            print("Pago rechazado. Datos de la tarjeta inválidos.")
            return False
        self.estado = "aprobado"
        print(f"Pago aprobado. Tarjeta {self.numero_tarjeta} — monto ${self.monto:,.2f}")
        return True

    def __str__(self) -> str:
        """Retorna una representación legible del pago con tarjeta."""
        return (
            f"  PAGO CON TARJETA\n"
            f"  referencia : {self.numero_referencia}\n"
            f"  tarjeta    : {self.numero_tarjeta}\n"
            f"  titular    : {self.__titular}\n"
            f"  vencimiento: {self.__vencimiento}\n"
            f"  monto      : ${self.monto:,.2f}\n"
            f"  estado     : {self.estado}\n"
        )

    def __repr__(self) -> str:
        """Representación oficial del objeto, delega en __str__."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Prueba: PagoTarjeta ===\n")

    print("-- Datos de pago --")
    numero_tarjeta = input("Número de tarjeta (16 dígitos): ").strip()
    titular        = input("Titular            : ").strip()
    vencimiento    = input("Vencimiento (MM/AA): ").strip()
    cvv            = input("CVV (3 dígitos)    : ").strip()

    try:
        monto = float(input("Monto a cobrar     : $").strip().replace(",", ""))
        pago  = PagoTarjeta(1001, monto, numero_tarjeta, titular, vencimiento, cvv)
        print(f"\n{pago}")

        input("Presione ENTER para procesar el pago...")
        resultado = pago.procesar_pago()
        print(f"\n{pago}")
    except ValueError as e:
        print(f"Error: {e}")
