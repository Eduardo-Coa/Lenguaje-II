import io
import sys
from datetime import date

from Clases.AgenteCatalogo import AgenteCatalogo
from Clases.AgenteRestaurador import AgenteRestaurador
from Clases.Catalogo import Catalogo
from Clases.Cuadro import Cuadro, EstiloCuadro, TecnicaCuadro
from Clases.DirectorMuseo import DirectorMuseo
from Clases.Escultura import Escultura, MaterialEscultura
from Clases.MuseoColaborador import MuseoColaborador
from Clases.Obra import EstadoObra, Periodo
from Clases.Otra import Otra
from Clases.Sala import Sala
from Clases.Visitante import Visitante

# ── Salas ──────────────────────────────────────────────────────────────────────
sala_renacimiento  = Sala("Sala Renacimiento")
sala_barroca       = Sala("Sala Barroca")
sala_impresionista = Sala("Sala Impresionista")
salas: list = [sala_renacimiento, sala_barroca, sala_impresionista]

# ── Obras preestablecidas ──────────────────────────────────────────────────────
_stdout = sys.stdout; sys.stdout = io.StringIO()

_gioconda   = Cuadro("La Gioconda",          "Leonardo da Vinci",  Periodo.RENACIMIENTO,
                     date(1503, 1,  1),  date(1797,  8,  1),  EstiloCuadro.RENACIMIENTO,     TecnicaCuadro.OLEO)
_meninas    = Cuadro("Las Meninas",           "Diego Velázquez",    Periodo.BARROCO,
                     date(1656, 1,  1),  date(1819, 11, 19),  EstiloCuadro.BARROCO,          TecnicaCuadro.OLEO)
_noche      = Cuadro("La noche estrellada",   "Vincent van Gogh",   Periodo.IMPRESIONISMO,
                     date(1889, 6,  1),  date(1941,  1,  1),  EstiloCuadro.POSTIMPRESIONISMO, TecnicaCuadro.OLEO)
_pensador   = Escultura("El pensador",        "Auguste Rodin",      Periodo.IMPRESIONISMO,
                        date(1904, 1,  1),  date(1950,  3, 15),  MaterialEscultura.BRONCE)

sys.stdout = _stdout

_gioconda.valoracion = 800_000_000.0
_meninas.valoracion  = 250_000_000.0
_noche.valoracion    =  50_000_000.0
_pensador.valoracion =  35_000_000.0

# ── Historial de restauraciones preestablecido ────────────────────────────────
_gioconda._restauraciones = [
    {"fecha_inicio": date(1956,  6,  1), "fecha_fin": date(1956,  9, 15)},
    {"fecha_inicio": date(2004,  3, 10), "fecha_fin": date(2004,  7, 20)},
]
_meninas._restauraciones = [
    {"fecha_inicio": date(1984,  1, 15), "fecha_fin": date(1984,  4, 30)},
]
_noche._restauraciones = [
    {"fecha_inicio": date(2002,  5,  1), "fecha_fin": date(2002,  8, 10)},
    {"fecha_inicio": date(2018, 11,  5), "fecha_fin": date(2019,  2, 28)},
]
_pensador._restauraciones = [
    {"fecha_inicio": date(1995,  7, 20), "fecha_fin": date(1995, 10,  5)},
]

# ── Catálogo ───────────────────────────────────────────────────────────────────
catalogo = Catalogo()
for _obra in [_gioconda, _meninas, _noche, _pensador]:
    catalogo.agregar_obra(_obra)

# ── Asignación a salas ─────────────────────────────────────────────────────────
sala_renacimiento.agregar_obra(_gioconda);   _gioconda._sala = sala_renacimiento
sala_barroca.agregar_obra(_meninas);         _meninas._sala  = sala_barroca
sala_impresionista.agregar_obra(_noche);     _noche._sala    = sala_impresionista
sala_impresionista.agregar_obra(_pensador);  _pensador._sala = sala_impresionista

# ── Museo colaborador ──────────────────────────────────────────────────────────
museo_orsay = MuseoColaborador("Musée d'Orsay", "Francia")

# ── Usuarios ───────────────────────────────────────────────────────────────────
_director   = DirectorMuseo("director01",    "director789")
_agente_cat = AgenteCatalogo("agente_cat01", "admin123")
_agente_res = AgenteRestaurador("restaurador01", "rest456")
_visitante  = Visitante("visitante01",       "vis123")

_stdout = sys.stdout; sys.stdout = io.StringIO()
_director.autenticar("director789")
_director.agregar_sala(sala_renacimiento)
_director.agregar_sala(sala_barroca)
_director.agregar_sala(sala_impresionista)
_director.agregar_museo_colaborador(museo_orsay)
_director.cerrar_sesion()
sys.stdout = _stdout

usuarios: list = [_visitante, _agente_cat, _agente_res, _director]


# ── Utilidades ─────────────────────────────────────────────────────────────────
def separador(titulo: str = "") -> None:
    print("\n" + "=" * 60)
    if titulo:
        print(f"  {titulo}")
        print("=" * 60)


def login():
    separador("MUSEO — Inicio de sesión")
    uid = input("  Usuario    : ").strip()
    pwd = input("  Contraseña : ").strip()
    for u in usuarios:
        if u.nombre_usuario == uid:
            if u.autenticar(pwd):
                print(f"\n  Bienvenido/a, {u.nombre_usuario}  [{u.get_rol()}].")
                return u
            else:
                print("  Contraseña incorrecta.")
                return None
    print("  Usuario no encontrado.")
    return None


def listar_obras() -> None:
    """Muestra todas las obras con su índice para selección."""
    for i, o in enumerate(catalogo.obras, 1):
        print(f"  [{i}] {o.obtener_tipo():<10} '{o.titulo}'  —  {o.autor}"
              f"  |  Estado: {o.estado.value}")


def seleccionar_obra(titulo_accion: str = "seleccionar"):
    """Pide al usuario un índice y retorna la obra correspondiente."""
    listar_obras()
    try:
        idx = int(input(f"\n  Número de obra a {titulo_accion} (0 para cancelar): "))
        if idx == 0:
            return None
        obras = catalogo.obras
        if idx < 1 or idx > len(obras):
            print("  Número fuera de rango.")
            return None
        return obras[idx - 1]
    except ValueError:
        print("  Entrada inválida.")
        return None


def seleccionar_sala(titulo_accion: str = "seleccionar") -> Sala | None:
    """Pide al usuario un índice y retorna la sala correspondiente."""
    for i, s in enumerate(salas, 1):
        print(f"  [{i}] {s.nombre}")
    try:
        idx = int(input(f"\n  Número de sala a {titulo_accion} (0 para cancelar): "))
        if idx == 0:
            return None
        if idx < 1 or idx > len(salas):
            print("  Número fuera de rango.")
            return None
        return salas[idx - 1]
    except ValueError:
        print("  Entrada inválida.")
        return None


def pedir_fecha(etiqueta: str) -> date | None:
    """Pide una fecha en formato YYYY-MM-DD."""
    raw = input(f"  {etiqueta} (YYYY-MM-DD): ").strip()
    try:
        return date.fromisoformat(raw)
    except ValueError:
        print("  Formato de fecha inválido.")
        return None


def elegir_enum(enum_cls, etiqueta: str):
    """Muestra los valores de un Enum y devuelve el elegido."""
    miembros = list(enum_cls)
    for i, m in enumerate(miembros, 1):
        print(f"  [{i}] {m.value}")
    try:
        idx = int(input(f"  {etiqueta}: "))
        if 1 <= idx <= len(miembros):
            return miembros[idx - 1]
        print("  Opción fuera de rango.")
        return None
    except ValueError:
        print("  Entrada inválida.")
        return None


# ── Menú Visitante ─────────────────────────────────────────────────────────────
def menu_visitante(visitante: Visitante) -> None:
    while True:
        separador(f"MENÚ VISITANTE — {visitante.nombre_usuario}")
        print("  1. Ver salas del museo")
        print("  2. Consultar obras por sala")
        print("  3. Buscar en catálogo")
        print("  0. Cerrar sesión")
        opcion = input("\n  Opción: ").strip()

        if opcion == "1":
            separador("SALAS DEL MUSEO")
            for s in salas:
                print(f"\n{s}")

        elif opcion == "2":
            separador("CONSULTAR OBRAS POR SALA")
            sala = seleccionar_sala("consultar")
            if sala:
                obras = visitante.consultar_obras_por_sala(sala)
                if obras:
                    separador(f"OBRAS EN {sala.nombre.upper()}")
                    for o in obras:
                        print(f"  - '{o.titulo}'  ({o.autor})  |  {o.estado.value}")
                else:
                    print("  Esta sala no tiene obras asignadas.")

        elif opcion == "3":
            separador("BUSCAR EN CATÁLOGO")
            print("  1. Por autor")
            print("  2. Por período")
            print("  3. Por tipo")
            print("  4. Por estado")
            sub = input("\n  Opción: ").strip()

            if sub == "1":
                autor = input("  Autor: ").strip()
                resultados = catalogo.buscar_por_autor(autor)
            elif sub == "2":
                periodo = elegir_enum(Periodo, "Período")
                resultados = catalogo.buscar_por_periodo(periodo) if periodo else []
            elif sub == "3":
                tipo = input("  Tipo (Cuadro / Escultura / Otra): ").strip()
                resultados = catalogo.buscar_por_tipo(tipo)
            elif sub == "4":
                estado = elegir_enum(EstadoObra, "Estado")
                resultados = catalogo.buscar_por_estado(estado) if estado else []
            else:
                print("  Opción inválida.")
                continue

            if resultados:
                print(f"\n  Resultados ({len(resultados)}):")
                for r in resultados:
                    print(f"  - {r}")
            else:
                print("  No se encontraron obras.")

        elif opcion == "0":
            visitante.cerrar_sesion()
            print("  Sesión cerrada.")
            break
        else:
            print("  Opción inválida.")


# ── Menú Agente de Catálogo ────────────────────────────────────────────────────
def menu_agente_catalogo(agente: AgenteCatalogo) -> None:
    while True:
        separador(f"MENÚ AGENTE CATÁLOGO — {agente.nombre_usuario}")
        print("  1. Ver catálogo completo")
        print("  2. Registrar nueva obra")
        print("  3. Asignar obra a sala")
        print("  4. Reportar daño en obra")
        print("  5. Dar baja obra")
        print("  0. Cerrar sesión")
        opcion = input("\n  Opción: ").strip()

        if opcion == "1":
            separador("CATÁLOGO COMPLETO")
            print(catalogo)

        elif opcion == "2":
            separador("REGISTRAR NUEVA OBRA")
            print("  Tipo de obra:")
            print("  [1] Cuadro")
            print("  [2] Escultura")
            print("  [3] Otra")
            tipo_op = input("\n  Opción: ").strip()
            if tipo_op not in ("1", "2", "3"):
                print("  Tipo inválido.")
                continue

            titulo = input("  Título       : ").strip()
            autor  = input("  Autor        : ").strip()
            if not titulo or not autor:
                print("  Título y autor son obligatorios.")
                continue

            print("\n  Período histórico:")
            periodo = elegir_enum(Periodo, "Período")
            if not periodo:
                continue

            fecha_creacion = pedir_fecha("Fecha de creación")
            if not fecha_creacion:
                continue
            fecha_entrada = pedir_fecha("Fecha entrada al museo")
            if not fecha_entrada:
                continue

            try:
                if tipo_op == "1":
                    print("\n  Estilo artístico:")
                    estilo = elegir_enum(EstiloCuadro, "Estilo")
                    if not estilo:
                        continue
                    print("\n  Técnica:")
                    tecnica = elegir_enum(TecnicaCuadro, "Técnica")
                    if not tecnica:
                        continue
                    obra = Cuadro(titulo, autor, periodo, fecha_creacion, fecha_entrada, estilo, tecnica)
                elif tipo_op == "2":
                    print("\n  Material:")
                    material = elegir_enum(MaterialEscultura, "Material")
                    if not material:
                        continue
                    obra = Escultura(titulo, autor, periodo, fecha_creacion, fecha_entrada, material)
                else:
                    tipo_desc = input("  Descripción del tipo: ").strip()
                    obra = Otra(titulo, autor, periodo, fecha_creacion, fecha_entrada, tipo_desc)

                agente.registrar_obra(catalogo, obra)
                try:
                    valor = float(input("  Valoración (€): ").strip())
                    obra.valoracion = valor
                except ValueError as e:
                    print(f"  Advertencia al valorar: {e}")
                print(f"\n  Obra registrada:\n  {obra}")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "3":
            separador("ASIGNAR OBRA A SALA")
            obra = seleccionar_obra("asignar")
            if not obra:
                continue
            separador("SALAS DISPONIBLES")
            sala = seleccionar_sala("asignar")
            if not sala:
                continue
            try:
                agente.asignar_sala(obra, sala)
                print(f"  '{obra.titulo}' asignada a '{sala.nombre}'.")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "4":
            separador("REPORTAR DAÑO")
            obra = seleccionar_obra("reportar")
            if not obra:
                continue
            descripcion = input("  Descripción del daño: ").strip()
            if not descripcion:
                print("  La descripción no puede estar vacía.")
                continue
            try:
                agente.reportar_danio(obra, descripcion)
                print(f"  Daño registrado. Estado: {obra.estado.value}")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "5":
            separador("DAR BAJA OBRA")
            obra = seleccionar_obra("dar de baja")
            if not obra:
                continue
            try:
                agente.dar_baja_obra(catalogo, obra)
                if obra.sala:
                    obra.sala.eliminar_obra(obra)
                print(f"  '{obra.titulo}' eliminada del catálogo.")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "0":
            agente.cerrar_sesion()
            print("  Sesión cerrada.")
            break
        else:
            print("  Opción inválida.")


# ── Menú Agente Restaurador ────────────────────────────────────────────────────
def menu_agente_restaurador(restaurador: AgenteRestaurador) -> None:
    while True:
        separador(f"MENÚ RESTAURADOR — {restaurador.nombre_usuario}")
        print("  1. Ver obras pendientes de restauración")
        print("  2. Iniciar restauración")
        print("  3. Finalizar restauración")
        print("  4. Ver historial de restauraciones de una obra")
        print("  0. Cerrar sesión")
        opcion = input("\n  Opción: ").strip()

        if opcion == "1":
            separador("OBRAS QUE NECESITAN RESTAURACIÓN")
            pendientes = restaurador.verificar_obras_pendientes(catalogo.obras)
            if not pendientes:
                print("  No hay obras pendientes de restauración.")
            else:
                for o in pendientes:
                    print(f"  - '{o.titulo}'  ({o.autor})  |  Estado: {o.estado.value}")

        elif opcion == "2":
            separador("INICIAR RESTAURACIÓN")
            obra = seleccionar_obra("restaurar")
            if not obra:
                continue
            try:
                restaurador.iniciar_restauracion(obra)
                print(f"  Restauración iniciada. Estado: {obra.estado.value}")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "3":
            separador("FINALIZAR RESTAURACIÓN")
            en_restauracion = [o for o in catalogo.obras if o.estado == EstadoObra.EN_RESTAURACION]
            if not en_restauracion:
                print("  No hay obras en restauración activa.")
                continue
            for i, o in enumerate(en_restauracion, 1):
                print(f"  [{i}] '{o.titulo}'  ({o.autor})")
            try:
                idx = int(input("\n  Número de obra (0 para cancelar): "))
                if idx == 0:
                    continue
                if idx < 1 or idx > len(en_restauracion):
                    print("  Número fuera de rango.")
                    continue
                obra = en_restauracion[idx - 1]
                restaurador.finalizar_restauracion(obra)
                print(f"  Restauración finalizada. Estado: {obra.estado.value}")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "4":
            separador("HISTORIAL DE RESTAURACIONES")
            obra = seleccionar_obra("consultar")
            if not obra:
                continue
            try:
                historial = restaurador.consultar_restauraciones(obra)
                if not historial:
                    print(f"  '{obra.titulo}' no tiene restauraciones registradas.")
                else:
                    print(f"\n  Restauraciones de '{obra.titulo}':")
                    for r in historial:
                        fin = r["fecha_fin"] if r["fecha_fin"] else "en curso"
                        print(f"    Inicio: {r['fecha_inicio']}  —  Fin: {fin}")
            except PermissionError as e:
                print(f"  Error: {e}")

        elif opcion == "0":
            restaurador.cerrar_sesion()
            print("  Sesión cerrada.")
            break
        else:
            print("  Opción inválida.")


# ── Menú Director del Museo ────────────────────────────────────────────────────
def menu_director(director: DirectorMuseo) -> None:
    while True:
        separador(f"MENÚ DIRECTOR — {director.nombre_usuario}")
        print("  1. Ver salas del museo")
        print("  2. Agregar sala")
        print("  3. Eliminar sala")
        print("  4. Ver museos colaboradores")
        print("  5. Agregar museo colaborador")
        print("  6. Ceder obra a museo colaborador")
        print("  7. Consultar valoración total del catálogo")
        print("  0. Cerrar sesión")
        opcion = input("\n  Opción: ").strip()

        if opcion == "1":
            separador("SALAS DEL MUSEO")
            if not director.salas:
                print("  No hay salas registradas.")
            else:
                for s in director.salas:
                    print(f"\n{s}")

        elif opcion == "2":
            separador("AGREGAR SALA")
            nombre = input("  Nombre de la nueva sala: ").strip()
            if not nombre:
                print("  El nombre no puede estar vacío.")
                continue
            nueva_sala = Sala(nombre)
            try:
                director.agregar_sala(nueva_sala)
                salas.append(nueva_sala)
                print(f"  Sala '{nombre}' agregada.")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "3":
            separador("ELIMINAR SALA")
            salas_director = director.salas
            if not salas_director:
                print("  No hay salas registradas.")
                continue
            for i, s in enumerate(salas_director, 1):
                print(f"  [{i}] {s.nombre}")
            try:
                idx = int(input("\n  Número de sala a eliminar (0 para cancelar): "))
                if idx == 0:
                    continue
                if idx < 1 or idx > len(salas_director):
                    print("  Número fuera de rango.")
                    continue
                sala = salas_director[idx - 1]
                director.eliminar_sala(sala)
                if sala in salas:
                    salas.remove(sala)
                print(f"  Sala '{sala.nombre}' eliminada.")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "4":
            separador("MUSEOS COLABORADORES")
            museos = director.museos_colaboradores
            if not museos:
                print("  No hay museos colaboradores registrados.")
            else:
                for m in museos:
                    print(f"  - {m}")

        elif opcion == "5":
            separador("AGREGAR MUSEO COLABORADOR")
            nombre = input("  Nombre del museo: ").strip()
            pais   = input("  País            : ").strip()
            if not nombre or not pais:
                print("  Nombre y país son obligatorios.")
                continue
            try:
                nuevo_museo = MuseoColaborador(nombre, pais)
                director.agregar_museo_colaborador(nuevo_museo)
                print(f"  Museo '{nombre}' agregado como colaborador.")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "6":
            separador("CEDER OBRA A MUSEO COLABORADOR")
            museos = director.museos_colaboradores
            if not museos:
                print("  No hay museos colaboradores registrados.")
                continue
            obra = seleccionar_obra("ceder")
            if not obra:
                continue
            print("\n  Museo colaborador:")
            for i, m in enumerate(museos, 1):
                print(f"  [{i}] {m}")
            try:
                idx = int(input("\n  Número de museo (0 para cancelar): "))
                if idx == 0:
                    continue
                if idx < 1 or idx > len(museos):
                    print("  Número fuera de rango.")
                    continue
                museo = museos[idx - 1]
                importe = float(input("  Importe de la cesión (€): ").strip())
                fecha_inicio = pedir_fecha("Fecha inicio de cesión")
                if not fecha_inicio:
                    continue
                raw_fin = input("  Fecha fin (YYYY-MM-DD, vacío = indefinida): ").strip()
                fecha_fin = date.fromisoformat(raw_fin) if raw_fin else None
                director.ceder_obra(obra, museo, importe, (fecha_inicio, fecha_fin))
                print(f"  '{obra.titulo}' cedida a '{museo.nombre}'. Estado: {obra.estado.value}")
            except (ValueError, PermissionError) as e:
                print(f"  Error: {e}")

        elif opcion == "7":
            separador("VALORACIÓN TOTAL DEL CATÁLOGO")
            try:
                total = director.consultar_valoracion_total(catalogo)
                print(f"  Valoración total: {total:,.2f} €")
            except PermissionError as e:
                print(f"  Error: {e}")

        elif opcion == "0":
            director.cerrar_sesion()
            print("  Sesión cerrada.")
            break
        else:
            print("  Opción inválida.")


# ── Bucle principal ─────────────────────────────────────────────────────────────
print("\n  Bienvenido al sistema del Museo")
print("  " + "-" * 52)
print(f"  {'Usuario':<20} {'Rol':<22} {'Contraseña'}")
print("  " + "-" * 52)
print(f"  {'visitante01':<20} {'Visitante':<22} vis123")
print(f"  {'agente_cat01':<20} {'Agente de Catálogo':<22} admin123")
print(f"  {'restaurador01':<20} {'Agente Restaurador':<22} rest456")
print(f"  {'director01':<20} {'Director del Museo':<22} director789")
print("  " + "-" * 52)

while True:
    usuario = login()
    if usuario is None:
        continuar = input("\n  ¿Intentar de nuevo? (s/n): ").strip().lower()
        if continuar != "s":
            print("  Hasta luego.")
            break
        continue

    if isinstance(usuario, Visitante):
        menu_visitante(usuario)
    elif isinstance(usuario, AgenteCatalogo):
        menu_agente_catalogo(usuario)
    elif isinstance(usuario, AgenteRestaurador):
        menu_agente_restaurador(usuario)
    elif isinstance(usuario, DirectorMuseo):
        menu_director(usuario)

    continuar = input("\n  ¿Iniciar otra sesión? (s/n): ").strip().lower()
    if continuar != "s":
        print("  Hasta luego.")
        break
