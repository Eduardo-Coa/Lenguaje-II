import ClasesTeleventas.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * Punto de entrada del sistema TeleVentas en Java.
 *
 * Replica el flujo interactivo del main.py de Python:
 * login, menu de cliente, menu de agente de bodega y menu de gerente.
 */
public class Main {

    // --- Estado global del sistema ---
    private static final List<OrdenCompra> ordenes = new ArrayList<>();
    private static final List<Pedido>      pedidos = new ArrayList<>();
    private static int contadorOrden  = 1000;
    private static int contadorPedido = 5000;
    private static int contadorQueja  = 1;

    // --- Datos iniciales ---
    private static final Inventario inventario =
        new Inventario("http://api.televentas.com/inventario", "Inventario Central");

    private static final Producto prod1 = new Producto(101, "Ferrari",     90_000.00, 10);
    private static final Producto prod2 = new Producto(102, "Lamborghini", 50_000.00, 50);
    private static final Producto prod3 = new Producto(103, "Porsche",     80_000.00, 25);
    private static final List<Producto> productosDelSistema = Arrays.asList(prod1, prod2, prod3);

    private static final Catalogo      catalogo      = new Catalogo(1, new ArrayList<>(productosDelSistema));
    private static final Transportadora transportadora = new Transportadora(1, "TransRapido S.A.");

    // --- Usuarios registrados ---
    private static final List<Usuario> usuarios = Arrays.asList(
        new Cliente("cli01", "Eduardo Coa", "pass123", "Calle 47 #6-33", "dcoa_37@unisalle.edu.co"),
        new AgenteBodega("age01", "agent123", 5, "Pedro Martinez"),
        new GerenteRelaciones("ger01", "ger123", "Diunis Perez")
    );

    private static final Scanner sc = new Scanner(System.in);

    // -----------------------------------------------------------------------

    public static void main(String[] args) {
        inventario.registrarProducto(101, "Ferrari",     90_000.00, 10);
        inventario.registrarProducto(102, "Lamborghini", 50_000.00, 50);
        inventario.registrarProducto(103, "Porsche",     80_000.00, 25);

        System.out.println("\n  Bienvenido al sistema TeleVentas");
        separador("");
        System.out.printf("  %-20s %-18s %s%n", "Usuario", "Rol", "Contrasena");
        separador("");
        System.out.printf("  %-20s %-18s %s%n", "cli01", "Cliente",       "pass123");
        System.out.printf("  %-20s %-18s %s%n", "age01", "Agente Bodega", "agent123");
        System.out.printf("  %-20s %-18s %s%n", "ger01", "Gerente",       "ger123");
        separador("");

        while (true) {
            Usuario usuario = login();
            if (usuario == null) {
                System.out.print("\n  Intentar de nuevo? (s/n): ");
                if (!sc.nextLine().trim().equalsIgnoreCase("s")) {
                    System.out.println("  Hasta luego.");
                    break;
                }
                continue;
            }

            if (usuario instanceof Cliente)           menuCliente((Cliente) usuario);
            else if (usuario instanceof AgenteBodega) menuAgente((AgenteBodega) usuario);
            else if (usuario instanceof GerenteRelaciones) menuGerente((GerenteRelaciones) usuario);

            System.out.print("\n  Iniciar otra sesion? (s/n): ");
            if (!sc.nextLine().trim().equalsIgnoreCase("s")) {
                System.out.println("  Hasta luego.");
                break;
            }
        }
    }

    // --- Utilidades --------------------------------------------------------

    private static void separador(String titulo) {
        System.out.println("\n" + "=".repeat(55));
        if (!titulo.isEmpty()) {
            System.out.println("  " + titulo);
            System.out.println("=".repeat(55));
        }
    }

    private static Usuario login() {
        separador("TELEVENTAS — Inicio de sesion");
        System.out.print("  Usuario    : ");
        String uid = sc.nextLine().trim();
        System.out.print("  Contrasena : ");
        String pwd = sc.nextLine().trim();
        for (Usuario u : usuarios) {
            if (u.validarCredenciales(uid, pwd)) {
                System.out.println("\n  Bienvenido/a, " + u.getNombre() + ".");
                return u;
            }
        }
        System.out.println("  Credenciales incorrectas.");
        return null;
    }

    // --- Menu Cliente ------------------------------------------------------

    private static void menuCliente(Cliente cliente) {
        while (true) {
            separador("MENU CLIENTE — " + cliente.getNombre());
            System.out.println("  1. Consultar catalogo");
            System.out.println("  2. Suscribirse al catalogo");
            System.out.println("  3. Buscar producto");
            System.out.println("  4. Crear orden de compra");
            System.out.println("  5. Cancelar una orden");
            System.out.println("  6. Presentar una queja");
            System.out.println("  0. Cerrar sesion");
            System.out.print("\n  Opcion: ");
            String opcion = sc.nextLine().trim();

            switch (opcion) {
                case "1" -> {
                    separador("CATALOGO DE PRODUCTOS");
                    for (Producto p : catalogo.listaProductos()) {
                        System.out.printf("  [%d] %-14s  —  $%,12.2f  (stock: %d)%n",
                            p.getNumeroProducto(), p.getDescripcion(),
                            p.getPrecio(), p.getCantidadDisponible());
                    }
                }
                case "2" -> {
                    try {
                        catalogo.suscribir(cliente);
                        catalogo.enviarCatalogo(cliente);
                    } catch (IllegalArgumentException e) {
                        System.out.println("  " + e.getMessage());
                    }
                }
                case "3" -> {
                    System.out.print("  Termino de busqueda: ");
                    String termino = sc.nextLine().trim();
                    for (Producto p : catalogo.buscarProducto(termino)) {
                        System.out.printf("  [%d] %-14s  —  $%,12.2f%n",
                            p.getNumeroProducto(), p.getDescripcion(), p.getPrecio());
                    }
                }
                case "4" -> crearOrden(cliente);
                case "5" -> cancelarOrden(cliente);
                case "6" -> presentarQueja(cliente);
                case "0" -> { System.out.println("  Sesion cerrada."); return; }
                default  -> System.out.println("  Opcion invalida.");
            }
        }
    }

    private static void crearOrden(Cliente cliente) {
        separador("CREAR ORDEN DE COMPRA");
        for (Producto p : productosDelSistema) {
            System.out.printf("  [%d] %-14s  —  $%,12.2f%n",
                p.getNumeroProducto(), p.getDescripcion(), p.getPrecio());
        }
        List<DetallePedido> detalles = new ArrayList<>();
        while (true) {
            System.out.print("\n  Codigo del producto (0 para terminar): ");
            try {
                int cod = Integer.parseInt(sc.nextLine().trim());
                if (cod == 0) break;
                Producto prod = productosDelSistema.stream()
                    .filter(p -> p.getNumeroProducto() == cod).findFirst().orElse(null);
                if (prod == null) { System.out.println("  Producto no encontrado."); continue; }
                System.out.print("  Cantidad de '" + prod.getDescripcion() + "': ");
                int qty = Integer.parseInt(sc.nextLine().trim());
                detalles.add(new DetallePedido(prod, qty));
            } catch (IllegalArgumentException e) {
                System.out.println("  Error: " + e.getMessage());
            }
        }
        if (detalles.isEmpty()) { System.out.println("  Orden cancelada (sin productos)."); return; }

        separador("DATOS DE PAGO — Tarjeta de credito");
        try {
            System.out.print("  Numero de tarjeta (16 digitos): "); String numTarjeta = sc.nextLine().trim();
            System.out.print("  Titular             : ");           String titular     = sc.nextLine().trim();
            System.out.print("  Vencimiento (MM/AA) : ");           String vencimiento = sc.nextLine().trim();
            System.out.print("  CVV (3 digitos)     : ");           String cvv         = sc.nextLine().trim();
            double total = detalles.stream().mapToDouble(DetallePedido::subtotal).sum();
            contadorOrden++;
            PagoTarjeta pago = new PagoTarjeta(contadorOrden, total, numTarjeta, titular, vencimiento, cvv);
            OrdenCompra orden = new OrdenCompra(contadorOrden, cliente, pago, detalles);
            orden.confirmar();
            ordenes.add(orden);
            System.out.println(orden);
        } catch (IllegalArgumentException e) {
            System.out.println("  Error: " + e.getMessage());
        }
    }

    private static void cancelarOrden(Cliente cliente) {
        List<OrdenCompra> misOrdenes = ordenes.stream()
            .filter(o -> o.getCliente().getUserId().equals(cliente.getUserId()))
            .toList();
        if (misOrdenes.isEmpty()) { System.out.println("  No tienes ordenes registradas."); return; }
        separador("TUS ORDENES");
        for (OrdenCompra o : misOrdenes)
            System.out.printf("  [%d] estado=%-12s  total=$%,.2f%n",
                o.getNumeroOrden(), o.getEstado(), o.calcularTotal());
        try {
            System.out.print("\n  Numero de orden a cancelar: ");
            int num = Integer.parseInt(sc.nextLine().trim());
            OrdenCompra orden = misOrdenes.stream()
                .filter(o -> o.getNumeroOrden() == num).findFirst().orElse(null);
            if (orden == null) System.out.println("  Orden no encontrada.");
            else               cliente.cancelarOrden(orden);
        } catch (IllegalArgumentException e) {
            System.out.println("  Error: " + e.getMessage());
        }
    }

    private static void presentarQueja(Cliente cliente) {
        System.out.print("  Motivo de la queja: ");
        String motivo = sc.nextLine().trim();
        if (motivo.isEmpty()) { System.out.println("  El motivo no puede estar vacio."); return; }
        try {
            Queja queja = cliente.presentarQueja(contadorQueja++, motivo);
            queja.registrarQueja();
            queja.remitirGerente();
            usuarios.stream()
                .filter(u -> u instanceof GerenteRelaciones)
                .map(u -> (GerenteRelaciones) u)
                .findFirst()
                .ifPresent(g -> g.recibirQueja(queja));
        } catch (IllegalArgumentException e) {
            System.out.println("  Error: " + e.getMessage());
        }
    }

    // --- Menu Agente de Bodega ---------------------------------------------

    private static void menuAgente(AgenteBodega agente) {
        while (true) {
            separador("MENU AGENTE DE BODEGA — " + agente.getNombre());
            System.out.println("  1. Ver ordenes confirmadas");
            System.out.println("  2. Empacar pedido");
            System.out.println("  3. Asignar transporte a pedido empacado");
            System.out.println("  0. Cerrar sesion");
            System.out.print("\n  Opcion: ");
            String opcion = sc.nextLine().trim();

            switch (opcion) {
                case "1" -> {
                    List<OrdenCompra> confirmadas = ordenes.stream()
                        .filter(o -> o.getEstado().equals(OrdenCompra.CONFIRMADA)).toList();
                    if (confirmadas.isEmpty()) { System.out.println("  No hay ordenes confirmadas."); break; }
                    separador("ORDENES CONFIRMADAS");
                    for (OrdenCompra o : confirmadas)
                        System.out.printf("  [%d] cliente=%-15s  total=$%,.2f%n",
                            o.getNumeroOrden(), o.getCliente().getNombre(), o.calcularTotal());
                    try {
                        System.out.print("\n  Numero de orden a consultar (0 para volver): ");
                        int num = Integer.parseInt(sc.nextLine().trim());
                        if (num == 0) break;
                        confirmadas.stream().filter(o -> o.getNumeroOrden() == num)
                            .findFirst().ifPresentOrElse(
                                agente::consultarOrden,
                                () -> System.out.println("  Orden no encontrada."));
                    } catch (NumberFormatException e) {
                        System.out.println("  Codigo invalido.");
                    }
                }
                case "2" -> {
                    List<OrdenCompra> sinPedido = ordenes.stream()
                        .filter(o -> o.getEstado().equals(OrdenCompra.CONFIRMADA))
                        .filter(o -> pedidos.stream().noneMatch(p -> p.getOrden().getNumeroOrden() == o.getNumeroOrden()))
                        .toList();
                    if (sinPedido.isEmpty()) { System.out.println("  No hay ordenes pendientes de empacar."); break; }
                    separador("ORDENES LISTAS PARA EMPACAR");
                    for (OrdenCompra o : sinPedido)
                        System.out.printf("  [%d] cliente=%s%n", o.getNumeroOrden(), o.getCliente().getNombre());
                    try {
                        System.out.print("\n  Numero de orden a empacar: ");
                        int num = Integer.parseInt(sc.nextLine().trim());
                        OrdenCompra orden = sinPedido.stream()
                            .filter(o -> o.getNumeroOrden() == num).findFirst().orElse(null);
                        if (orden == null) { System.out.println("  Orden no encontrada."); break; }
                        contadorPedido++;
                        Pedido pedido = new Pedido(contadorPedido, orden);
                        pedido.empacar();
                        pedidos.add(pedido);
                        System.out.println(pedido);
                    } catch (IllegalArgumentException e) {
                        System.out.println("  Error: " + e.getMessage());
                    }
                }
                case "3" -> {
                    List<Pedido> empacados = pedidos.stream()
                        .filter(p -> p.getEstado().equals(Pedido.EMPACADO)).toList();
                    if (empacados.isEmpty()) { System.out.println("  No hay pedidos empacados esperando transporte."); break; }
                    separador("PEDIDOS EMPACADOS");
                    for (Pedido p : empacados)
                        System.out.printf("  [%d] orden=%d  cliente=%s%n",
                            p.getNumeroPedido(), p.getOrden().getNumeroOrden(), p.getOrden().getCliente().getNombre());
                    try {
                        System.out.print("\n  Numero de pedido a despachar: ");
                        int num = Integer.parseInt(sc.nextLine().trim());
                        Pedido pedido = empacados.stream()
                            .filter(p -> p.getNumeroPedido() == num).findFirst().orElse(null);
                        if (pedido == null) { System.out.println("  Pedido no encontrado."); break; }
                        agente.asignarTransporte(pedido, transportadora);
                        System.out.println(pedido);
                    } catch (IllegalArgumentException e) {
                        System.out.println("  Error: " + e.getMessage());
                    }
                }
                case "0" -> { System.out.println("  Sesion cerrada."); return; }
                default  -> System.out.println("  Opcion invalida.");
            }
        }
    }

    // --- Menu Gerente de Relaciones ----------------------------------------

    private static void menuGerente(GerenteRelaciones gerente) {
        while (true) {
            separador("MENU GERENTE — " + gerente.getNombre());
            System.out.println("  1. Ver quejas recibidas");
            System.out.println("  0. Cerrar sesion");
            System.out.print("\n  Opcion: ");
            String opcion = sc.nextLine().trim();

            switch (opcion) {
                case "1" -> {
                    List<Queja> quejas = gerente.getQuejas();
                    if (quejas.isEmpty()) System.out.println("  No hay quejas registradas.");
                    else {
                        separador("QUEJAS RECIBIDAS");
                        for (Queja q : quejas) System.out.println(q);
                    }
                }
                case "0" -> { System.out.println("  Sesion cerrada."); return; }
                default  -> System.out.println("  Opcion invalida.");
            }
        }
    }
}
