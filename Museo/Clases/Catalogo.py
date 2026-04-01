from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.Obra import EstadoObra, Periodo


class Catalogo:
    """Gestiona el conjunto de obras de arte registradas en el museo."""

    def __init__(self) -> None:
        """Inicializa el catálogo con una lista de obras vacía."""
        self._obras: list = []

    # --- getters ---

    @property
    def obras(self) -> list:
        """Retorna una copia de la lista de obras registradas."""
        return list(self._obras)

# --------------------Metodos--------------------------------------------------

    def agregar_obra(self, obra) -> None:
        """Añade una obra al catálogo si no estaba registrada."""
        if obra in self._obras:
            raise ValueError(f"La obra '{obra.titulo}' ya está registrada en el catálogo.")
        self._obras.append(obra)

    def eliminar_obra(self, obra) -> None:
        """Elimina una obra del catálogo."""
        if obra not in self._obras:
            raise ValueError(f"La obra '{obra.titulo}' no está en el catálogo.")
        self._obras.remove(obra)

# --- Consultas -------------------------------------------------------------

    def buscar_por_autor(self, autor: str) -> list:
        """Retorna las obras de un autor dado (búsqueda insensible a mayúsculas)."""
        autor_lower = autor.lower()
        return [o for o in self._obras if o.autor.lower() == autor_lower]

    def buscar_por_periodo(self, periodo: Periodo) -> list:
        """Retorna las obras correspondientes a un periodo artístico."""
        return [o for o in self._obras if o.periodo == periodo]

    def buscar_por_estado(self, estado: EstadoObra) -> list:
        """Retorna las obras que se encuentran en un estado determinado."""
        return [o for o in self._obras if o.estado == estado]

    def buscar_por_sala(self, sala) -> list:
        """Retorna las obras asignadas a una sala, ordenadas por título."""
        return sorted(
            [o for o in self._obras if o.sala == sala],
            key=lambda o: o.titulo,
        )

    def buscar_por_tipo(self, tipo: str) -> list:
        """Retorna las obras de un tipo concreto: 'Cuadro', 'Escultura' u 'Otra'."""
        return [o for o in self._obras if o.obtener_tipo() == tipo]



    def __str__(self) -> str:
        if not self._obras:
            return "El catálogo está vacío."
        lineas = [f"Catálogo ({len(self._obras)} obras):"]
        for obra in self._obras:
            lineas.append(f"  - {obra}")
        return "\n".join(lineas)


# ---------------------------------------------------------------------------
# Prueba
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import io
    from datetime import date

    from Clases.Cuadro import Cuadro, EstiloCuadro, TecnicaCuadro
    from Clases.Escultura import Escultura, MaterialEscultura
    from Clases.Obra import Periodo

    # Silenciar creación de objetos
    _stdout = sys.stdout
    sys.stdout = io.StringIO()

    catalogo = Catalogo()

    cuadro1 = Cuadro(
        "La noche estrellada", "Van Gogh", Periodo.IMPRESIONISMO,
        date(1889, 6, 1), date(1941, 1, 1),
        EstiloCuadro.POSTIMPRESIONISMO, TecnicaCuadro.OLEO,
    )
    cuadro2 = Cuadro(
        "Las Meninas", "Diego Velázquez", Periodo.BARROCO,
        date(1656, 1, 1), date(1819, 11, 19),
        EstiloCuadro.BARROCO, TecnicaCuadro.OLEO,
    )
    escultura = Escultura(
        "El pensador", "Auguste Rodin", Periodo.IMPRESIONISMO,
        date(1904, 1, 1), date(1950, 3, 15),
        MaterialEscultura.BRONCE,
    )

    catalogo.agregar_obra(cuadro1)
    catalogo.agregar_obra(cuadro2)
    catalogo.agregar_obra(escultura)

    sys.stdout = _stdout

    print("=== Prueba de Catálogo ===")
    print(catalogo)

    print("\n--- Menú de búsqueda ---")
    print("1. Buscar por autor")
    print("2. Buscar por periodo")
    print("3. Buscar por tipo")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        autor = input("Autor: ")
        resultados = catalogo.buscar_por_autor(autor)
    elif opcion == "2":
        print("Periodos disponibles:")
        for p in Periodo:
            print(f"  {p.name}: {p.value}")
        nombre_periodo = input("Nombre del periodo (ej. BARROCO): ").upper()
        resultados = catalogo.buscar_por_periodo(Periodo[nombre_periodo])
    elif opcion == "3":
        tipo = input("Tipo (Cuadro / Escultura / Otra): ")
        resultados = catalogo.buscar_por_tipo(tipo)
    else:
        resultados = []
        print("Opción no válida.")

    if resultados:
        print(f"\nResultados ({len(resultados)}):")
        for r in resultados:
            print(f"  - {r}")
    elif opcion in ("1", "2", "3"):
        print("No se encontraron obras.")
