from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date

from Clases.Obra import Obra, Periodo


class Otra(Obra):
    """Obra de arte que no encaja en las categorías de Cuadro ni Escultura."""

    def __init__(
        self,
        titulo: str,
        autor: str,
        periodo: Periodo,
        fecha_creacion: date,
        fecha_entrada_museo: date,
        tipo_descripcion: str,
    ) -> None:
        """Inicializa la obra con una descripción libre de su tipo."""
        super().__init__(titulo, autor, periodo, fecha_creacion, fecha_entrada_museo)
        self._tipo_descripcion = tipo_descripcion

    # --- getters ---

    @property
    def tipo_descripcion(self) -> str:
        """Retorna la descripción del tipo de obra."""
        return self._tipo_descripcion

    # --------------------Metodos--------------------------------------------------

    def obtener_tipo(self) -> str:
        """Retorna el tipo de obra."""
        return "Otra"

    # --- Representación ---

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Tipo: {self._tipo_descripcion}"


# ---------------------------------------------------------------------------
# Prueba interactiva
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    from datetime import date

    print("=== Prueba de Otra ===")

    # Obra de ejemplo
    obra = Otra(
        titulo="Instalación de luz",
        autor="James Turrell",
        periodo=Periodo.MODERNO_CONTEMPORANEO,
        fecha_creacion=date(1992, 5, 20),
        fecha_entrada_museo=date(2005, 11, 1),
        tipo_descripcion="Instalación lumínica",
    )

    print(obra)
    print(f"\nTipo            : {obra.obtener_tipo()}")
    print(f"Tipo descripción: {obra.tipo_descripcion}")

    nueva_val = input("\nIngresa una nueva valoración (€): ")
    obra.valoracion = float(nueva_val)
    print(f"Valoración actualizada: {obra.valoracion:.2f} €")
