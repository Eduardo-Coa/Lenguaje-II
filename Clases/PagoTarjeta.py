from Clases.Pago import Pago 

class PagoTarjeta(Pago):

    def __init__(
        self,
        numero_referencia : int,
        monto : float,
        numero_tarjeta: str,
        titular : str,
        vencimiento : str, 
        cvv : str,

    )-> None:
        super().__init__(numero_referencia, monto)
        self.__numero_tarjeta =numero_tarjeta
        self.__titular = titular
        self.__vencimiento = vencimiento
        self.__cvv = cvv

    
    @property
    def numero_tarjeta(self)-> str:
        return f"**** **** **** {self.__numero_tarjeta[-4:]} "
    
    @property
    def titular(self)-> str:
        return self.__titular
    
    @property
    def vencimiento(self)->str:
        return self.__vencimiento
    
    "metodos"
    
    def validar_tarjeta(self)->bool:
        numero_valido = len(self.__numero_tarjeta) == 16 and self.__numero_tarjeta.isdigit()
        cvv_valido = len(self.__cvv) == 3 and self.__cvv.isdigit()
        vencimiento_valido = len(self.__vencimiento) == 5 and "/" in self.__vencimiento
        titular_valido = bool(self.__titular.strip())

        return numero_valido and cvv_valido and vencimiento_valido and titular_valido
    
    def procesar_pago(self)->bool:
        if not self.validar_tarjeta():
            self.estado ="rechazado"
            print(f"Pago Rechazado, datos de la tarjeta inválidos")
            return False
        
        self.estado = "aprobado"
        print(f"Pago Aprobado, Tarjeta {self.__numero_tarjeta},monto ${self.monto:.2f} ")
        return True
    
    def __str__(self) -> str:
        return (
            f"PagoTarjeta(ref={self.numero_referencia}, "
            f"tarjeta={self.numero_tarjeta}, "
            f"titular={self.__titular}, "
            f"monto={self.monto:.2f}), "
            f"estado={self.estado}"
        )
 
    def __repr__(self) -> str:
        return self.__str__()