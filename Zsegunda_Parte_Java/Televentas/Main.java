import Clases.*;

import java.util.Arrays;
import java.util.List;

/**
 * Punto de entrada del sistema TeleVentas en Java.
 *
 * Demuestra el flujo completo: catalogo, orden de compra,
 * pago, pedido, transporte, entrega y queja.
 */
public class Main {

    public static void main(String[] args) {
        System.out.println("=== Sistema TeleVentas ===\n");

        // --- Usuarios ---
        Cliente cliente = new Cliente(
            "cli01", "pass123", "Eduardo Coa",
            "Calle 47 #6-33", "dcoa_37@unisalle.edu.co"
        );
        GerenteRelaciones gerente = new GerenteRelaciones("ger01", "ger123", "Diunis Perez");
        AgenteBodega agente = new AgenteBodega("age01", "agent123", 5, "Pedro Martinez");
        Transportadora transportadora = new Transportadora(1, "TransRapido S.A.");

        System.out.println(cliente);
        System.out.println(agente);
        System.out.println(gerente);

        // --- Catalogo y productos ---
        Producto ferrari     = new Producto(101, "Ferrari",     90_000.00, 10);
        Producto lamborghini = new Producto(102, "Lamborghini", 50_000.00, 50);
        Producto porsche     = new Producto(103, "Porsche",     80_000.00, 25);

        List<Producto> listaProductos = Arrays.asList(ferrari, lamborghini, porsche);
        Catalogo catalogo = new Catalogo(1, listaProductos);

        System.out.println(catalogo);
        for (Producto p : catalogo.listaProductos()) {
            System.out.printf("  [%d] %s  —  $%,.2f  (stock: %d)%n",
                p.getNumeroProducto(), p.getDescripcion(),
                p.getPrecio(), p.getCantidadDisponible());
        }

        // --- Crear orden ---
        System.out.println("\n-- Orden de compra --");
        List<DetallePedido> detalles = Arrays.asList(
            new DetallePedido(ferrari, 1),
            new DetallePedido(lamborghini, 2)
        );
        PagoTarjeta pago = new PagoTarjeta(
            1001,
            detalles.stream().mapToDouble(DetallePedido::subtotal).sum(),
            "1234567890123456", "Eduardo Coa", "12/26", "123"
        );
        OrdenCompra orden = new OrdenCompra(1001, cliente, pago, detalles);
        orden.confirmar();
        System.out.println(orden);

        // --- Pedido y transporte ---
        System.out.println("-- Pedido y transporte --");
        Pedido pedido = new Pedido(5001, orden);
        pedido.empacar();
        agente.asignarTransporte(pedido, transportadora);
        System.out.println(pedido);

        // --- Confirmar entrega ---
        transportadora.confirmarEntrega();
        System.out.println("Estado envio: " + transportadora.getEstadoEnvio() + "\n");

        // --- Queja ---
        System.out.println("-- Queja --");
        Queja queja = cliente.presentarQueja(1, "El pedido llego con retraso.");
        queja.remitirGerente();
        gerente.recibirQueja(queja);
        System.out.println(queja);
        System.out.println("Quejas recibidas por el gerente: " + gerente.getQuejas().size());
    }
}
