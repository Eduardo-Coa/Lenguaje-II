from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from abc import ABC, abstractmethod
from datetime import date
from enum import Enum


class Periodo(Enum):
    """Periodos históricos del arte."""

    RENACIMIENTO = "Renacimiento (siglos XV-XVI)"
    BARROCO = "Barroco (siglo XVII)"
    ROCOCO = "Rococó (siglo XVIII)"
    NEOCLASICISMO = "Neoclasicismo (siglos XVIII-XIX)"
    ROMANTICISMO = "Romanticismo (siglo XIX)"
    REALISMO = "Realismo (siglo XIX)"
    IMPRESIONISMO = "Impresionismo (finales del siglo XIX)"
    MODERNO_CONTEMPORANEO = "Arte Moderno y Contemporáneo (siglos XX-XXI)"


class EstadoObra(Enum):
    """Estados posibles de una obra de arte."""

    EXPUESTA = "Expuesta"
    DAÑADA = "Dañada"
    EN_RESTAURACION = "En restauración"
    CEDIDA = "Cedida"


class Obra(ABC):
    """Clase abstracta que representa una obra de arte del museo."""

    def __init__(
        self,
        titulo: str,
        autor: str,
        periodo: Periodo,
        fecha_creacion: date,
        fecha_entrada_museo: date,
    ) -> None:
        """Inicializa la obra con sus datos básicos y estado inicial EXPUESTA."""
        if not isinstance(periodo, Periodo):
            raise ValueError(f"El periodo debe ser una instancia de Periodo. Recibido: {periodo}")
        if not isinstance(fecha_creacion, date):
            raise ValueError("fecha_creacion debe ser una instancia de date.")
        if not isinstance(fecha_entrada_museo, date):
            raise ValueError("fecha_entrada_museo debe ser una instancia de date.")
        self._titulo = titulo
        self._autor = autor
        self._periodo = periodo
        self._fecha_creacion = fecha_creacion
        self._fecha_entrada_museo = fecha_entrada_museo
        self._valoracion: float = 0.0
        self._estado: EstadoObra = EstadoObra.EXPUESTA
        self._sala = None
        self._restauraciones: list = []
        self._reportes_danos: list = []
        self._cesiones: list = []
        self._solicitudes_pendientes: list = []

    # --- getters y setters---

    @property
    def titulo(self) -> str:
        """Retorna el título de la obra."""
        return self._titulo

    @property
    def autor(self) -> str:
        """Retorna el autor de la obra."""
        return self._autor

    @property
    def periodo(self) -> Periodo:
        """Retorna el periodo histórico de la obra."""
        return self._periodo

    @property
    def fecha_creacion(self) -> date:
        """Retorna la fecha de creación de la obra."""
        return self._fecha_creacion

    @property
    def fecha_entrada_museo(self) -> date:
        """Retorna la fecha en que la obra ingresó al museo."""
        return self._fecha_entrada_museo

    @property
    def estado(self) -> EstadoObra:
        """Retorna el estado actual de la obra."""
        return self._estado

    @property
    def valoracion(self) -> float:
        """Retorna la valoración económica de la obra en euros."""
        return self._valoracion

    @valoracion.setter
    def valoracion(self, valor: float) -> None:
        """Actualiza la valoración; debe ser un valor no negativo."""
        if valor < 0:
            raise ValueError("La valoración no puede ser negativa.")
        self._valoracion = valor

    @property
    def sala(self):
        """Retorna la sala donde está expuesta la obra."""
        return self._sala

    @sala.setter
    def sala(self, nueva_sala) -> None:
        """Asigna la obra a una sala."""
        self._sala = nueva_sala

    @property
    def restauraciones(self) -> list:
        """Retorna la lista de restauraciones registradas."""
        return self._restauraciones

    @property
    def reportes_danos(self) -> list:
        """Retorna la lista de reportes de daños."""
        return list(self._reportes_danos)

    @property
    def cesiones(self) -> list:
        """Retorna la lista de cesiones registradas."""
        return list(self._cesiones)

    @property
    def solicitudes_pendientes(self) -> list:
        """Retorna las cesiones pendientes en cola."""
        return list(self._solicitudes_pendientes)

    # --------------------Metodos--------------------------------------------------

    def necesita_restauracion(self) -> bool:
        """Devuelve True si han pasado 5 años desde la última restauración o nunca fue restaurada."""
        restauraciones_finalizadas = [
            r for r in self._restauraciones if r["fecha_fin"] is not None
        ]
        if not restauraciones_finalizadas:
            return True
        ultima = max(restauraciones_finalizadas, key=lambda r: r["fecha_fin"])
        return (date.today() - ultima["fecha_fin"]).days >= 365 * 5

    def esta_cedida(self) -> bool:
        """Indica si la obra tiene actualmente una cesión activa."""
        return any(c["fecha_fin"] is None for c in self._cesiones)

    def registrar_cesion(self, museo, importe: float, periodo: tuple) -> None:
        """Registra una nueva cesión o la encola si la obra ya está cedida."""
        cesion = {
            "museo": museo,
            "importe": importe,
            "fecha_inicio": periodo[0],
            "fecha_fin": periodo[1],
        }
        if self.esta_cedida():
            self._solicitudes_pendientes.append(cesion)
        else:
            self._cesiones.append(cesion)
            self._estado = EstadoObra.CEDIDA

    def finalizar_cesion_activa(self) -> None:
        """Finaliza la cesión activa y activa la siguiente solicitud pendiente si existe."""
        cesion_activa = next(
            (c for c in self._cesiones if c["fecha_fin"] is None), None
        )
        if cesion_activa is None:
            raise ValueError(f"La obra '{self._titulo}' no tiene una cesión activa.")
        if self._solicitudes_pendientes:
            siguiente = self._solicitudes_pendientes.pop(0)
            self._cesiones.append(siguiente)
        else:
            self._estado = EstadoObra.EXPUESTA

    # --- Método abstracto ---

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Retorna el tipo de obra (Cuadro, Escultura, Otra)."""

    # --- Representación ---

    def __str__(self) -> str:
        return (
            f"{self.obtener_tipo()} | '{self._titulo}' de {self._autor} "
            f"[{self._periodo.value}] | Estado: {self._estado.value} "
            f"| Creación: {self._fecha_creacion} "
            f"| Entrada museo: {self._fecha_entrada_museo} "
            f"| Valoración: {self._valoracion:.2f} €"
        )
