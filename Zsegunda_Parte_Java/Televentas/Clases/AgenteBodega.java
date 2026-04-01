package Clases;

/**
 * Representa al agente de bodega del sistema TeleVentas.
 *
 * Extiende Usuario y es responsable de consultar ordenes confirmadas,
 * empacar pedidos y asignar una transportadora para su envio.
 */
public class AgenteBodega extends Usuario {

    // Atributos privados
    private int numeroBodega;

    // --- Constructor ---

    /** Inicializa el agente con sus credenciales y numero de bodega. */
    public AgenteBodega(String userId, String contrasena, int numeroBodega, String nombre) {
        super(userId, nombre, contrasena);
        this.numeroBodega = numeroBodega;
    }

    // --- Getters ---

    /** Retorna el numero de bodega asignada al agente. */
    public int getNumeroBodega() {
        return numeroBodega;
    }

    // --- Metodos ---

    /** Muestra el detalle de productos y total de una orden confirmada. */
    public void consultarOrden(OrdenCompra orden) {
        if (!orden.getEstado().equals(OrdenCompra.CONFIRMADA)) {
            throw new IllegalStateException(
                "Solo se pueden consultar ordenes confirmadas. " +
                "Estado actual: " + orden.getEstado());
        }
        for (DetallePedido detalle : orden.getDetalles()) {
            System.out.printf("  - %s | Cantidad: %d | Subtotal: $%,.2f%n",
                detalle.getProducto().getDescripcion(),
                detalle.getCantidad(),
                detalle.subtotal());
        }
        System.out.printf("  Total: $%,.2f%n", orden.calcularTotal());
    }

    /** Asigna una transportadora al pedido empacado y lo despacha. */
    public void asignarTransporte(Pedido pedido, Transportadora empresa) {
        System.out.println("Agente " + getNombre() + " asignando transporte " +
                           "al pedido " + pedido.getNumeroPedido() + ".");
        pedido.asignarTransporte(empresa);
    }

    @Override
    public String toString() {
        return "  AGENTE DE BODEGA\n" +
               "  id     : " + getUserId()   + "\n" +
               "  nombre : " + getNombre()   + "\n" +
               "  bodega : " + numeroBodega  + "\n";
    }
}
