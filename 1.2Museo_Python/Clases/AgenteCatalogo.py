from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date

from Clases.Obra import EstadoObra
from Clases.Usuario import Usuario


class AgenteCatalogo(Usuario):
    """Usuario encargado de gestionar el catálogo de obras y las salas."""

    # --------------------Metodos--------------------------------------------------

    def get_rol(self) -> str:
        """Retorna el rol del usuario."""
        return "Agente de Catálogo"

    def registrar_obra(self, catalogo, obra) -> None:
        """Añade una obra al catálogo del museo."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para registrar obras.")
        catalogo.agregar_obra(obra)

    def dar_baja_obra(self, catalogo, obra) -> None:
        """Elimina una obra del catálogo del museo."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para dar de baja obras.")
        catalogo.eliminar_obra(obra)

    def asignar_sala(self, obra, sala) -> None:
        """Asigna una obra a una sala determinada."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para asignar salas.")
        obra.sala = sala
        sala.agregar_obra(obra)

    def reportar_danio(self, obra, descripcion: str) -> None:
        """Registra un reporte de daño sobre una obra y cambia su estado a DAÑADA."""
        if not self._autenticado:
            raise PermissionError("Debe autenticarse para reportar daños.")
        reporte = {
            "fecha": date.today(),
            "descripcion": descripcion,
            "reportado_por": self._nombre_usuario,
        }
        obra._reportes_danos.append(reporte)
        obra._estado = EstadoObra.DAÑADA


# ---------------------------------------------------------------------------
# Prueba interactiva
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

    agente = AgenteCatalogo("agente01", "admin123")
    sala = Sala("Sala Barroca")

    cuadro = Cuadro(
        "Las Meninas", "Diego Velázquez", Periodo.BARROCO,
        date(1656, 1, 1), date(1819, 11, 19),
        EstiloCuadro.BARROCO, TecnicaCuadro.OLEO,
    )

    sys.stdout = _stdout

    print("=== Prueba de AgenteCatalogo ===")
    print(f"Agente: {agente.nombre_usuario} | Rol: {agente.get_rol()}")

    agente.autenticar("admin123")
    print(f"Autenticado: {agente.autenticado}")

    # Asignar sala
    agente.asignar_sala(cuadro, sala)
    print(f"\nObra asignada a: {cuadro.sala.nombre}")
    print(sala)

    # Valorar obra
    valor_str = input("\nIngresa una valoración para la obra (€): ")
    agente.valorar_obra(cuadro, float(valor_str))
    print(f"Valoración registrada: {cuadro.valoracion:.2f} €")

    # Reportar daño
    input("\nPresiona ENTER para reportar un daño en la obra...")
    descripcion = input("Descripción del daño: ")
    agente.reportar_danio(cuadro, descripcion)
    print(f"Estado de la obra: {cuadro.estado.value}")
    print(f"Reporte: {cuadro.reportes_danos[-1]}")
