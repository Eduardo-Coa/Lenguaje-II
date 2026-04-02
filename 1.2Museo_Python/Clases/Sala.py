from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Sala:
    """Sala del museo que agrupa obras de arte para su exposición."""

    def __init__(self, nombre: str) -> None:
        """Inicializa la sala con un nombre y sin obras asignadas."""
        self._nombre = nombre
        self._obras: list = []

    # --- getters ---

    @property
    def nombre(self) -> str:
        """Retorna el nombre de la sala."""
        return self._nombre

    @property
    def obras(self) -> list:
        """Retorna una copia de la lista de obras en la sala."""
        return list(self._obras)

    # --------------------Metodos--------------------------------------------------

    def agregar_obra(self, obra) -> None:
        """Añade una obra a la sala si no estaba asignada."""
        if obra in self._obras:
            raise ValueError(f"La obra '{obra.titulo}' ya está en la sala '{self._nombre}'.")
        self._obras.append(obra)

    def eliminar_obra(self, obra) -> None:
        """Retira una obra de la sala."""
        if obra not in self._obras:
            raise ValueError(f"La obra '{obra.titulo}' no está en la sala '{self._nombre}'.")
        self._obras.remove(obra)

    # --- Representación ---

    def __str__(self) -> str:
        if not self._obras:
            return f"Sala '{self._nombre}' — sin obras asignadas."
        lineas = [f"Sala '{self._nombre}' ({len(self._obras)} obras):"]
        for obra in self._obras:
            lineas.append(f"  - {obra.titulo} ({obra.autor})")
        return "\n".join(lineas)


# ---------------------------------------------------------------------------
# Prueba 
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import io
    from datetime import date

    from Clases.Cuadro import Cuadro, EstiloCuadro, TecnicaCuadro
    from Clases.Obra import Periodo

    # Silenciar salida de creación
    _stdout = sys.stdout
    sys.stdout = io.StringIO()

    sala = Sala("Sala Impresionista")
    cuadro1 = Cuadro(
        "La noche estrellada", "Van Gogh", Periodo.IMPRESIONISMO,
        date(1889, 6, 1), date(1941, 1, 1),
        EstiloCuadro.POSTIMPRESIONISMO, TecnicaCuadro.OLEO,
    )
    cuadro2 = Cuadro(
        "Almuerzo sobre la hierba", "Manet", Periodo.IMPRESIONISMO,
        date(1863, 1, 1), date(1907, 4, 10),
        EstiloCuadro.IMPRESIONISMO, TecnicaCuadro.OLEO,
    )

    sys.stdout = _stdout

    print("=== Prueba de Sala ===")
    print(sala)

    input("\nPresiona ENTER para agregar dos cuadros...")
    sala.agregar_obra(cuadro1)
    sala.agregar_obra(cuadro2)
    print(sala)

    input("\nPresiona ENTER para eliminar el primer cuadro...")
    sala.eliminar_obra(cuadro1)
    print(sala)
