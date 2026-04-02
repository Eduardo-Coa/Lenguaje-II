from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date

from Clases.Obra import EstadoObra
from Clases.Usuario import Usuario


class AgenteRestaurador(Usuario):
    """Usuario encargado de gestionar las restauraciones de las obras."""

    # --------------------Metodos--------------------------------------------------

    def get_rol(self) -> str:
        """Retorna el rol del usuario."""
        return "Agente Restaurador"

    def iniciar_restauracion(self, obra) -> None:
        """Inicia una restauración sobre una obra y cambia su estado a EN_RESTAURACION."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para iniciar restauraciones.")
        restauracion = {
            "fecha_inicio": date.today(),
            "fecha_fin": None,
        }
        obra.restauraciones.append(restauracion)
        obra._estado = EstadoObra.EN_RESTAURACION

    def finalizar_restauracion(self, obra) -> None:
        """Finaliza la restauración activa de una obra y registra la fecha de fin."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para finalizar restauraciones.")
        restauracion_activa = next(
            (r for r in obra.restauraciones if r["fecha_fin"] is None), None
        )
        if restauracion_activa is None:
            raise ValueError(f"La obra '{obra.titulo}' no tiene una restauración activa.")
        restauracion_activa["fecha_fin"] = date.today()
        obra._estado = EstadoObra.EXPUESTA

    def consultar_restauraciones(self, obra) -> list:
        """Retorna el historial de restauraciones de una obra, ordenado por antigüedad."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para consultar restauraciones.")
        return sorted(obra.restauraciones, key=lambda r: r["fecha_inicio"])

    def verificar_obras_pendientes(self, obras: list) -> list:
        """Retorna las obras que necesitan restauración según el criterio de 5 años."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para verificar obras pendientes.")
        return [obra for obra in obras if obra.necesita_restauracion()]


# ---------------------------------------------------------------------------
# Prueba interactiva
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import io
    from datetime import date

    from Clases.Cuadro import Cuadro, EstiloCuadro, TecnicaCuadro
    from Clases.Obra import Periodo

    # Silenciar creación de objetos
    _stdout = sys.stdout
    sys.stdout = io.StringIO()

    restaurador = AgenteRestaurador("restaurador01", "rest456")

    cuadro = Cuadro(
        "La Gioconda", "Leonardo da Vinci", Periodo.RENACIMIENTO,
        date(1503, 1, 1), date(1797, 8, 1),
        EstiloCuadro.RENACIMIENTO, TecnicaCuadro.OLEO,
    )

    sys.stdout = _stdout

    print("=== Prueba de AgenteRestaurador ===")
    print(f"Restaurador: {restaurador.nombre_usuario} | Rol: {restaurador.get_rol()}")

    restaurador.autenticar("rest456")
    print(f"Autenticado: {restaurador.autenticado}")
    print(f"\nObra: {cuadro.titulo} | Estado: {cuadro.estado.value}")
    print(f"¿Necesita restauración? {cuadro.necesita_restauracion()}")

    input("\nPresiona ENTER para iniciar restauración...")
    restaurador.iniciar_restauracion(cuadro)
    print(f"Estado: {cuadro.estado.value}")

    input("\nPresiona ENTER para finalizar restauración...")
    restaurador.finalizar_restauracion(cuadro)
    print(f"Estado: {cuadro.estado.value}")

    historial = restaurador.consultar_restauraciones(cuadro)
    print(f"\nHistorial de restauraciones: {historial}")
