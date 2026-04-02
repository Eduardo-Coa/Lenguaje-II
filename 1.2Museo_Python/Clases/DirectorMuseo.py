from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Clases.Usuario import Usuario


class DirectorMuseo(Usuario):
    """Usuario con máximos privilegios: gestiona salas, cesiones y museos colaboradores."""

    def __init__(self, nombre_usuario: str, contrasena: str) -> None:
        """Inicializa el director con listas vacías de salas y museos colaboradores."""
        super().__init__(nombre_usuario, contrasena)
        self._museos_colaboradores: list = []
        self._salas: list = []

    # --- getters ---

    @property
    def museos_colaboradores(self) -> list:
        """Retorna la lista de museos colaboradores registrados."""
        return list(self._museos_colaboradores)

    @property
    def salas(self) -> list:
        """Retorna la lista de salas del museo."""
        return list(self._salas)

    # --------------------Metodos--------------------------------------------------

    def get_rol(self) -> str:
        """Retorna el rol del usuario."""
        return "Director del Museo"

    def agregar_sala(self, sala) -> None:
        """Añade una sala al museo."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para agregar salas.")
        if sala not in self._salas:
            self._salas.append(sala)

    def eliminar_sala(self, sala) -> None:
        """Elimina una sala del museo."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para eliminar salas.")
        if sala not in self._salas:
            raise ValueError(f"La sala '{sala.nombre}' no existe en el museo.")
        self._salas.remove(sala)

    def agregar_museo_colaborador(self, museo) -> None:
        """Añade un museo al listado de colaboradores con los que se puede ceder obras."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para agregar museos colaboradores.")
        if museo not in self._museos_colaboradores:
            self._museos_colaboradores.append(museo)

    def ceder_obra(self, obra, museo, importe: float, periodo: tuple) -> None:
        """Cede una obra a un museo colaborador registrando importe y periodo."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para ceder obras.")
        if museo not in self._museos_colaboradores:
            raise ValueError(f"El museo '{museo.nombre}' no está en la lista de colaboradores.")
        if importe < 0:
            raise ValueError("El importe de la cesión no puede ser negativo.")
        obra.registrar_cesion(museo, importe, periodo)

    def consultar_valoracion_total(self, catalogo) -> float:
        """Retorna la suma de las valoraciones de todas las obras del catálogo."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para consultar la valoración total.")
        return sum(obra.valoracion for obra in catalogo.obras)


# ---------------------------------------------------------------------------
# Prueba interactiva
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import io
    from datetime import date

    from Clases.Catalogo import Catalogo
    from Clases.Cuadro import Cuadro, EstiloCuadro, TecnicaCuadro
    from Clases.MuseoColaborador import MuseoColaborador
    from Clases.Obra import Periodo
    from Clases.Sala import Sala

    # Silenciar creación de objetos
    _stdout = sys.stdout
    sys.stdout = io.StringIO()

    director = DirectorMuseo("director01", "director789")
    sala_imp = Sala("Sala Impresionista")
    museo_collab = MuseoColaborador("Musée d'Orsay", "Francia")
    catalogo = Catalogo()

    cuadro = Cuadro(
        "La noche estrellada", "Van Gogh", Periodo.IMPRESIONISMO,
        date(1889, 6, 1), date(1941, 1, 1),
        EstiloCuadro.POSTIMPRESIONISMO, TecnicaCuadro.OLEO,
    )
    cuadro.valoracion = 50_000_000.0
    catalogo.agregar_obra(cuadro)

    sys.stdout = _stdout

    print("=== Prueba de DirectorMuseo ===")
    print(f"Director: {director.nombre_usuario} | Rol: {director.get_rol()}")

    director.autenticar("director789")
    print(f"Autenticado: {director.autenticado}")

    # Agregar sala y museo colaborador
    director.agregar_sala(sala_imp)
    director.agregar_museo_colaborador(museo_collab)
    print(f"\nSalas: {[s.nombre for s in director.salas]}")
    print(f"Museos colaboradores: {[str(m) for m in director.museos_colaboradores]}")

    # Consultar valoración total
    total = director.consultar_valoracion_total(catalogo)
    print(f"\nValoración total del catálogo: {total:,.2f} €")

    # Ceder obra
    input("\nPresiona ENTER para ceder la obra al museo colaborador...")
    director.ceder_obra(
        cuadro, museo_collab, 100_000.0,
        (date(2026, 4, 1), None),
    )
    print(f"Estado de la obra: {cuadro.estado.value}")
    print(f"Cesión activa: {cuadro.esta_cedida()}")
