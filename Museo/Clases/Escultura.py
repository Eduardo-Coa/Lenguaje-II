from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date
from enum import Enum

from Clases.Obra import Obra, Periodo


class MaterialEscultura(Enum):
    """Materiales utilizados en la elaboración de esculturas."""

    MARMOL = "Mármol"
    GRANITO = "Granito"
    BRONCE = "Bronce"
    ORO = "Oro"
    CONCRETO = "Concreto"
    MADERA = "Madera"


class Escultura(Obra):
    """Obra de arte tridimensional elaborada con un material específico."""

    def __init__(
        self,
        titulo: str,
        autor: str,
        periodo: Periodo,
        fecha_creacion: date,
        fecha_entrada_museo: date,
        material: MaterialEscultura,
    ) -> None:
        """Inicializa la escultura validando que el material sea una instancia de MaterialEscultura."""
        super().__init__(titulo, autor, periodo, fecha_creacion, fecha_entrada_museo)
        if not isinstance(material, MaterialEscultura):
            raise ValueError(
                f"El material debe ser una instancia de MaterialEscultura. Recibido: {material}"
            )
        self._material = material

    # --- getters-----------------------------

    @property
    def material(self) -> MaterialEscultura:
        """Retorna el material de la escultura."""
        return self._material

# --------------------Metodos--------------------------------------------------

    def obtener_tipo(self) -> str:
        """Retorna el tipo de obra."""
        return "Escultura"



    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Material: {self._material.value}"


# ---------------------------------------------------------------------------
# Prueba 
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    from datetime import date

    print("=== Prueba de Escultura ===")

    # Escultura de ejemplo
    escultura = Escultura(
        titulo="El pensador",
        autor="Auguste Rodin",
        periodo=Periodo.IMPRESIONISMO,
        fecha_creacion=date(1904, 1, 1),
        fecha_entrada_museo=date(2015, 3, 15),
        material=MaterialEscultura.BRONCE,
    )

    print(escultura)
    print(f"\nTipo     : {escultura.obtener_tipo()}")
    print(f"Material : {escultura.material.value}")

    nueva_val = input("\nIngresa una nueva valoración (€): ")
    escultura.valoracion = float(nueva_val)
    print(f"Valoración actualizada: {escultura.valoracion:.2f} €")
