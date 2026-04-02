from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from abc import ABC, abstractmethod


class Usuario(ABC):
    """Clase abstracta que representa un usuario del sistema de museo."""

    def __init__(self, nombre_usuario: str, contrasena: str) -> None:
        """Inicializa el usuario con credenciales y sesión cerrada."""
        self._nombre_usuario = nombre_usuario
        self._contrasena = contrasena
        self._autenticado = False

    # --- getters ---

    @property
    def nombre_usuario(self) -> str:
        """Retorna el nombre de usuario."""
        return self._nombre_usuario

    @property
    def autenticado(self) -> bool:
        """Retorna True si el usuario tiene sesión activa."""
        return self._autenticado

    @property
    def contrasena(self) -> str:
        """Retorna la contraseña del usuario."""
        return self._contrasena

    @contrasena.setter
    def contrasena(self, nueva: str) -> None:
        """Actualiza la contraseña si no está vacía."""
        if not nueva:
            raise ValueError("La contraseña no puede estar vacía.")
        self._contrasena = nueva

    # --------------------Metodos--------------------------------------------------

    def autenticar(self, contrasena: str) -> bool:
        """Verifica la contraseña y marca al usuario como autenticado."""
        self._autenticado = self._contrasena == contrasena
        return self._autenticado

    def cerrar_sesion(self) -> None:
        """Cierra la sesión del usuario."""
        self._autenticado = False

 

    @abstractmethod
    def get_rol(self) -> str:
        """Retorna el rol del usuario en el sistema."""


# ---------------------------------------------------------------------------
# Prueba 
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    # Implementación mínima para probar la clase abstracta
    class UsuarioTest(Usuario):
        def get_rol(self) -> str:
            return "Director Museo"

    print("=== Prueba de Usuario ===")
    nombre = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    u = UsuarioTest(nombre, contrasena)
    print(f"\nUsuario creado: {u.nombre_usuario} | Rol: {u.get_rol()}")

    intento = input("\nIngresa la contraseña para autenticar: ")
    if u.autenticar(intento):
        print(f"Autenticado: {u.autenticado}")
    else:
        print("Contraseña incorrecta.")

    input("\nPresiona ENTER para cerrar sesión...")
    u.cerrar_sesion()
    print(f"Sesión cerrada.")
