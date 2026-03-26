from abc import ABC, abstractmethod


class Usuario(ABC):
    """Clase abstracta que representa los usuarios del sistema, a partir de esta clase creamos los usuarios."""

    def __init__(
        self,
        nombre_usuario: str,
        contrasena: str
        ) -> None:
        
        self._nombre_usuario = nombre_usuario
        self._contrasena = contrasena
        self._autenticado = False

    @property
    def nombre_usuario(self) -> str:
        return self._nombre_usuario

    @property
    def autenticado(self) -> bool:
        return self._autenticado

    def autenticar(self, contrasena: str) -> bool:
        """Verifica la contraseña y marca al usuario como autenticado."""
        self._autenticado = self._contrasena == contrasena
        return self._autenticado

    def cerrar_sesion(self) -> None:
        self._autenticado = False

    @abstractmethod
    def get_rol(self) -> str:
        """Retorna el rol del usuario en el sistema."""
