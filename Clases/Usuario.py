class Usuario:
    def __init__(
        self,
        user_id: str,
        nombre: str,
        contrasena: str,
    ) -> None:
        self.__nombre = nombre
        self.__user_id = user_id
        self.__contrasena = contrasena
        
    @property
    def nombre(self)->str:
         return self.__nombre

    @property
    def user_id(self) -> str:
        return self.__user_id
        
    @property
    def contrasena(self)->str:
         return self.__contrasena
        
    def validar_credenciales(self, user_id: str, contrasena: str)->bool:
        return self.__user_id == user_id and self.__contrasena == contrasena
        
    def __str__(self) -> str:
         return f"Usuario(id={self.__user_id}, contrasena={self.__contrasena})"
        
    def __repr__(self) -> str:
         return self.__str__()