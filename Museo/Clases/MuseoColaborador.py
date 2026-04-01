from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class MuseoColaborador:
    """Museo colaborador con el que se pueden gestionar cesiones de obras."""

    def __init__(self, nombre: str, pais: str) -> None:
        """Inicializa el museo colaborador con su nombre y país."""
        self._nombre = nombre
        self._pais = pais

    # --- Propiedades ---

    @property
    def nombre(self) -> str:
        """Retorna el nombre del museo colaborador."""
        return self._nombre

    @property
    def pais(self) -> str:
        """Retorna el país del museo colaborador."""
        return self._pais



    def __str__(self) -> str:
        return f"Museo '{self._nombre}' ({self._pais})"


# ---------------------------------------------------------------------------
# Prueba
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Prueba de MuseoColaborador ===")

    nombre = input("Nombre del museo colaborador: ")
    pais = input("País: ")

    museo = MuseoColaborador(nombre, pais)
    print(f"\n{museo}")
