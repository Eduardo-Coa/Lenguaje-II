from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.Usuario import Usuario


class Visitante(Usuario):
    """Usuario público que puede consultar obras por sala desde el vestíbulo."""

    # --------------------Metodos--------------------------------------------------

    def get_rol(self) -> str:
        """Retorna el rol del usuario."""
        return "Visitante"

    def consultar_obras_por_sala(self, sala) -> list:
        """Retorna las obras asignadas a una sala, ordenadas por título."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para consultar obras.")
        return sorted(sala.obras, key=lambda obra: obra.titulo)


# ---------------------------------------------------------------------------
# Prueba 
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import io
    from datetime import date

    from Clases.Cuadro import Cuadro, EstiloCuadro, TecnicaCuadro
    from Clases.Obra import Periodo
    from Clases.Sala import Sala

    # Silenciar creación de objetos
    _stdout = sys.stdout
    sys.stdout = io.StringIO()

    visitante = Visitante("eduardo_coa", "pass123")
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
    sala.agregar_obra(cuadro1)
    sala.agregar_obra(cuadro2)

    sys.stdout = _stdout

    print("=== Prueba de Visitante ===")
    print(f"Visitante: {visitante.nombre_usuario} | Rol: {visitante.get_rol()}")

    visitante.autenticar("pass123")
    print(f"Autenticado: {visitante.autenticado}")

    print(f"\nObras en '{sala.nombre}' (ordenadas por título):")
    for obra in visitante.consultar_obras_por_sala(sala):
        print(f"  - {obra.titulo} ({obra.autor})")

    input("\nPresiona ENTER para cerrar sesión...")
    visitante.cerrar_sesion()
    print(f"Sesión cerrada. ")
