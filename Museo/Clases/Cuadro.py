from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date
from enum import Enum

from Clases.Obra import Obra, Periodo


class EstiloCuadro(Enum):
    """Estilos artísticos reconocidos en pintura."""

    RENACIMIENTO = "Renacimiento (s. XV-XVI)"
    BARROCO = "Barroco (1600-1750)"
    ROCOCO = "Rococó (1720-1780)"
    NEOCLASICISMO = "Neoclasicismo (1750-1820)"
    ROMANTICISMO = "Romanticismo (1790-1880)"
    REALISMO = "Realismo (1840-1870)"
    IMPRESIONISMO = "Impresionismo (1872-1882)"
    POSTIMPRESIONISMO = "Postimpresionismo (1880-1910)"
    ART_NOUVEAU = "Art Nouveau (1890-1905)"
    FAUVISMO = "Fauvismo (1905-1908)"
    EXPRESIONISMO = "Expresionismo (1905-1933)"
    CUBISMO = "Cubismo (1907-1917)"
    FUTURISMO = "Futurismo (1909-1920)"
    DADAISMO = "Dadaísmo (1916-1923)"
    SURREALISMO = "Surrealismo (años 20-30)"
    EXPRESIONISMO_ABSTRACTO = "Expresionismo Abstracto (1940s-50s)"
    POP_ART = "Pop Art (1950s-60s)"
    MINIMALISMO = "Minimalismo (1960s)"
    HIPERREALISMO = "Hiperrealismo (1970s-presente)"
    ARTE_CONCEPTUAL = "Arte Conceptual (1960s-presente)"


class TecnicaCuadro(Enum):
    """Técnicas pictóricas utilizadas en cuadros."""

    FRESCO = "Pintura al Fresco"
    TEMPERA = "Temple o Témpera"
    OLEO = "Pintura al Óleo"
    ENCAUSTICA = "Encáustica"
    ACUARELA = "Acuarela"
    ACRILICO = "Acrílico"


class Cuadro(Obra):
    """Obra de arte pictórica con estilo y técnica definidos."""

    def __init__(
        self,
        titulo: str,
        autor: str,
        periodo: Periodo,
        fecha_creacion: date,
        fecha_entrada_museo: date,
        estilo: EstiloCuadro,
        tecnica: TecnicaCuadro,
    ) -> None:
        """Inicializa el cuadro validando que estilo y técnica sean instancias correctas."""
        super().__init__(titulo, autor, periodo, fecha_creacion, fecha_entrada_museo)
        if not isinstance(estilo, EstiloCuadro):
            raise ValueError(f"El estilo debe ser una instancia de EstiloCuadro. Recibido: {estilo}")
        if not isinstance(tecnica, TecnicaCuadro):
            raise ValueError(f"La técnica debe ser una instancia de TecnicaCuadro. Recibido: {tecnica}")
        self._estilo = estilo
        self._tecnica = tecnica

    # --- Propiedades ---

    @property
    def estilo(self) -> EstiloCuadro:
        """Retorna el estilo artístico del cuadro."""
        return self._estilo

    @property
    def tecnica(self) -> TecnicaCuadro:
        """Retorna la técnica pictórica del cuadro."""
        return self._tecnica

    # --------------------Metodos--------------------------------------------------

    def obtener_tipo(self) -> str:
        """Retorna el tipo de obra."""
        return "Cuadro"

    # --- Representación ---

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Estilo: {self._estilo.value} | Técnica: {self._tecnica.value}"


# ---------------------------------------------------------------------------
# Prueba interactiva
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    from datetime import date

    print("=== Prueba de Cuadro ===")

    # Cuadro de ejemplo
    cuadro = Cuadro(
        titulo="La noche estrellada",
        autor="Vincent van Gogh",
        periodo=Periodo.IMPRESIONISMO,
        fecha_creacion=date(1889, 6, 1),
        fecha_entrada_museo=date(1941, 1, 1),
        estilo=EstiloCuadro.POSTIMPRESIONISMO,
        tecnica=TecnicaCuadro.OLEO,
    )

    print(cuadro)
    print(f"\nTipo     : {cuadro.obtener_tipo()}")
    print(f"Estilo   : {cuadro.estilo.value}")
    print(f"Técnica  : {cuadro.tecnica.value}")

    nueva_val = input("\nIngresa una nueva valoración (€): ")
    cuadro.valoracion = float(nueva_val)
    print(f"Valoración actualizada: {cuadro.valoracion:.2f} €")
