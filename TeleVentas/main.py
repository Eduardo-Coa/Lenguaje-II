from Clases.Producto import Producto
from Clases.DetallePedido import DetallePedido
from Clases.PagoTarjeta import PagoTarjeta
from Clases.OrdenCompra import OrdenCompra
from Clases.Pedido import Pedido
from Clases.Catalogo import Catalogo
from Clases.Cliente import Cliente
from Clases.AgenteBodega import AgenteBodega
from Clases.GerenteRelaciones import GerenteRelaciones
from Clases.Transportadora import Transportadora
from Clases.Inventario import Inventario

# ── Estado global del sistema ──────────────────────────────────────────────────
ordenes: list = []
pedidos: list = []
contador_orden = 1000
contador_pedido = 5000
contador_queja = 1

# ── Datos iniciales ────────────────────────────────────────────────────────────
inventario = Inventario("http://api.televentas.com/inventario", "Inventario Central")
inventario.registrar_producto(101, 'Televisor 55"',  1_200_000.00, 10)
inventario.registrar_producto(102, "Control Remoto",    45_000.00, 50)
inventario.registrar_producto(103, "Soporte de Pared",  80_000.00, 25)

prod1 = Producto(101, 'Televisor 55"',  1_200_000.00, 10)
prod2 = Producto(102, "Control Remoto",    45_000.00, 50)
prod3 = Producto(103, "Soporte de Pared",  80_000.00, 25)
productos_sistema = [prod1, prod2, prod3]

catalogo = Catalogo(1, [prod1, prod2, prod3])
transportadora = Transportadora(1, "TransRápido S.A.")

# ── Usuarios registrados ───────────────────────────────────────────────────────
usuarios = [
    Cliente("Ana_Garcia",    "Ana García",    "pass123", "Calle 45 #12-30", "ana@correo.com"),
    Cliente("Carlos_Lopez",  "Carlos López",  "pass456", "Av. 68 #20-15",   "carlos@correo.com"),
    AgenteBodega("Pedro_Martinez", "agent123", 5, "Pedro Martínez"),
    GerenteRelaciones("Laura_Mendez", "ger789", "Laura Méndez"),
]


# ── Utilidades ─────────────────────────────────────────────────────────────────
def separador(titulo: str = "") -> None:
    print("\n" + "=" * 55)
    if titulo:
        print(f"  {titulo}")
        print("=" * 55)


def login() -> object | None:
    separador("TELEVENTAS — Inicio de sesión")
    uid = input("  Usuario    : ").strip()
    pwd = input("  Contraseña : ").strip()
    for u in usuarios:
        if u.validar_credenciales(uid, pwd):
            print(f"\n  Bienvenido/a, {u.nombre}.")
            return u
    print("  Credenciales incorrectas.")
    return None


# ── Menú Cliente ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
def menu_cliente(cliente: Cliente) -> None:
    global contador_orden, contador_queja

    while True:
        separador(f"MENÚ CLIENTE — {cliente.nombre}")
        print("  1. Consultar catálogo")
        print("  2. Suscribirse al catálogo")
        print("  3. Buscar producto")
        print("  4. Crear orden de compra")
        print("  5. Cancelar una orden")
        print("  6. Presentar una queja")
        print("  0. Cerrar sesión")
        opcion = input("\n  Opción: ").strip()

        if opcion == "1":
            separador("CATÁLOGO DE PRODUCTOS")
            for p in cliente.consultar_catalogo(catalogo):
                print(
                    f"  [{p['numero_producto']}] {p['descripcion']}"
                    f"  —  ${p['precio']:>12,.2f}  (stock: {p['cantidad_disponible']})"
                )

        elif opcion == "2":
            try:
                cliente.suscribir_catalogo(catalogo)
                catalogo.enviar_catalogo(cliente)
            except ValueError as e:
                print(f"  {e}")

        elif opcion == "3":
            termino = input("  Término de búsqueda: ").strip()
            resultados = catalogo.buscar_producto(termino)
            for p in resultados:
                print(f"  [{p.numero_producto}] {p.descripcion}  —  ${p.precio:>12,.2f}")

        elif opcion == "4":
            separador("CREAR ORDEN DE COMPRA")
            for p in productos_sistema:
                print(f"  [{p.numero_producto}] {p.descripcion}  —  ${p.precio:>12,.2f}")
            detalles = []
            while True:
                try:
                    cod = int(input("\n  Código del producto (0 para terminar): "))
                except ValueError:
                    print("  Código inválido.")
                    continue
                if cod == 0:
                    break
                prod = next((p for p in productos_sistema if p.numero_producto == cod), None)
                if not prod:
                    print("  Producto no encontrado.")
                    continue
                try:
                    qty = int(input(f"  Cantidad de '{prod.descripcion}': "))
                    detalles.append(DetallePedido(prod, qty))
                except ValueError as e:
                    print(f"  {e}")

            if not detalles:
                print("  Orden cancelada (sin productos).")
                continue

            separador("DATOS DE PAGO — Tarjeta de crédito")
            try:
                numero_tarjeta = input("  Número de tarjeta (16 dígitos): ").strip()
                titular        = input("  Titular             : ").strip()
                vencimiento    = input("  Vencimiento (MM/AA) : ").strip()
                cvv            = input("  CVV (3 dígitos)     : ").strip()
                total = sum(d.subtotal() for d in detalles)
                contador_orden += 1
                pago = PagoTarjeta(contador_orden, total, numero_tarjeta, titular, vencimiento, cvv)
                orden = OrdenCompra(contador_orden, cliente, pago, detalles, inventario)
                orden.confirmar()
                ordenes.append(orden)
                print(orden)
            except ValueError as e:
                print(f"  Error: {e}")

        elif opcion == "5":
            mis_ordenes = [o for o in ordenes if o.cliente.user_id == cliente.user_id]
            if not mis_ordenes:
                print("  No tienes órdenes registradas.")
                continue
            separador("TUS ÓRDENES")
            for o in mis_ordenes:
                print(f"  [{o.numero_orden}] estado={o.estado}  total=${o.calcular_total():,.2f}")
            try:
                num = int(input("\n  Número de orden a cancelar: "))
                orden = next((o for o in mis_ordenes if o.numero_orden == num), None)
                if not orden:
                    print("  Orden no encontrada.")
                else:
                    cliente.cancelar_orden(orden)
            except ValueError as e:
                print(f"  {e}")

        elif opcion == "6":
            motivo = input("  Motivo de la queja: ").strip()
            if not motivo:
                print("  El motivo no puede estar vacío.")
                continue
            try:
                queja = cliente.presentar_queja(contador_queja, motivo)
                contador_queja += 1
                queja.registrar_queja()
                queja.remitir_gerente()
                gerente = next((u for u in usuarios if isinstance(u, GerenteRelaciones)), None)
                if gerente:
                    gerente.recibir_queja(queja)
            except ValueError as e:
                print(f"  {e}")

        elif opcion == "0":
            print("  Sesión cerrada.")
            break
        else:
            print("  Opción inválida.")


# ── Menú Agente de Bodega ───────────────────────────────────────────────────────────────────────────────────────────────────────
def menu_agente(agente: AgenteBodega) -> None:
    global contador_pedido

    while True:
        separador(f"MENÚ AGENTE DE BODEGA — {agente.nombre}")
        print("  1. Ver órdenes confirmadas")
        print("  2. Empacar pedido")
        print("  3. Asignar transporte a pedido empacado")
        print("  0. Cerrar sesión")
        opcion = input("\n  Opción: ").strip()

        if opcion == "1":
            confirmadas = [o for o in ordenes if o.estado == "confirmada"]
            if not confirmadas:
                print("  No hay órdenes confirmadas.")
                continue
            separador("ÓRDENES CONFIRMADAS")
            for o in confirmadas:
                print(f"  [{o.numero_orden}] cliente={o.cliente.nombre}  total=${o.calcular_total():,.2f}")
            try:
                num = int(input("\n  Número de orden a consultar (0 para volver): "))
                if num == 0:
                    continue
                orden = next((o for o in confirmadas if o.numero_orden == num), None)
                if not orden:
                    print("  Orden no encontrada.")
                else:
                    agente.consultar_orden(orden)
            except ValueError as e:
                print(f"  {e}")

        elif opcion == "2":
            confirmadas = [
                o for o in ordenes
                if o.estado == "confirmada"
                and not any(p.orden.numero_orden == o.numero_orden for p in pedidos)
            ]
            if not confirmadas:
                print("  No hay órdenes pendientes de empacar.")
                continue
            separador("ÓRDENES LISTAS PARA EMPACAR")
            for o in confirmadas:
                print(f"  [{o.numero_orden}] cliente={o.cliente.nombre}")
            try:
                num = int(input("\n  Número de orden a empacar: "))
                orden = next((o for o in confirmadas if o.numero_orden == num), None)
                if not orden:
                    print("  Orden no encontrada.")
                else:
                    contador_pedido += 1
                    pedido = Pedido(contador_pedido, orden, inventario)
                    pedido.empacar()
                    pedidos.append(pedido)
                    print(pedido)
            except ValueError as e:
                print(f"  {e}")

        elif opcion == "3":
            empacados = [p for p in pedidos if p.estado == "empacado"]
            if not empacados:
                print("  No hay pedidos empacados esperando transporte.")
                continue
            separador("PEDIDOS EMPACADOS")
            for p in empacados:
                print(f"  [{p.numero_pedido}] orden={p.orden.numero_orden}  cliente={p.orden.cliente.nombre}")
            try:
                num = int(input("\n  Número de pedido a despachar: "))
                pedido = next((p for p in empacados if p.numero_pedido == num), None)
                if not pedido:
                    print("  Pedido no encontrado.")
                else:
                    agente.asignar_transporte(pedido, transportadora)
                    print(pedido)
            except ValueError as e:
                print(f"  {e}")

        elif opcion == "0":
            print("  Sesión cerrada.")
            break
        else:
            print("  Opción inválida.")


# ── Menú Gerente de Relaciones ──────────────────────────────────────────────────────────────────────────────────────────────────
def menu_gerente(gerente: GerenteRelaciones) -> None:
    while True:
        separador(f"MENÚ GERENTE — {gerente.nombre}")
        print("  1. Ver quejas recibidas")
        print("  0. Cerrar sesión")
        opcion = input("\n  Opción: ").strip()

        if opcion == "1":
            quejas = gerente._GerenteRelaciones__quejas
            if not quejas:
                print("  No hay quejas registradas.")
            else:
                separador("QUEJAS RECIBIDAS")
                for q in quejas:
                    print(f"  {q}")

        elif opcion == "0":
            print("  Sesión cerrada.")
            break
        else:
            print("  Opción inválida.")


# ── Bucle principal ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
print("\n  Bienvenido al sistema TeleVentas")
print("  " + "-" * 52)
print(f"  {'Usuario':<20} {'Rol':<18} {'Contraseña'}")
print("  " + "-" * 52)
print(f"  {'Ana_Garcia':<20} {'Cliente':<18} pass123")
print(f"  {'Carlos_Lopez':<20} {'Cliente':<18} pass456")
print(f"  {'Pedro_Martinez':<20} {'Agente Bodega':<18} agent123")
print(f"  {'Laura_Mendez':<20} {'Gerente':<18} ger789")
print("  " + "-" * 52)

while True:
    usuario = login()
    if usuario is None:
        continuar = input("\n  ¿Intentar de nuevo? (s/n): ").strip().lower()
        if continuar != "s":
            print("  Hasta luego.")
            break
        continue

    if isinstance(usuario, Cliente):
        menu_cliente(usuario)
    elif isinstance(usuario, AgenteBodega):
        menu_agente(usuario)
    elif isinstance(usuario, GerenteRelaciones):
        menu_gerente(usuario)

    continuar = input("\n  ¿Iniciar otra sesión? (s/n): ").strip().lower()
    if continuar != "s":
        print("  Hasta luego.")
        break
