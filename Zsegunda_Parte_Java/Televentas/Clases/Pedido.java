package Clases;

/**
 * Representa el pedido fisico armado por el Agente de Bodega en TeleVentas.
 *
 * A partir de una orden confirmada, gestiona el empaque de los productos
 * y la asignacion de una transportadora para su despacho.
 */
public class Pedido {

    // Estados validos
    public static final String PENDIENTE           = "pendiente";
    public static final String EMPACADO            = "empacado";
    public static final String TRANSPORTE_ASIGNADO = "transporte_asignado";
    public static final String EN_DESPACHO         = "en_despacho";

    // Atributos privados
    private int numeroPedido;
    private OrdenCompra orden;
    private String estado;
    private Transportadora transportadora;

    // --- Constructor ---

    /** Inicializa el pedido en estado PENDIENTE a partir de una orden de compra. */
    public Pedido(int numeroPedido, OrdenCompra orden) {
        this.numeroPedido  = numeroPedido;
        this.orden         = orden;
        this.estado        = PENDIENTE;
        this.transportadora = null;
    }

    // --- Getters ---

    /** Retorna el numero identificador del pedido. */
    public int getNumeroPedido() { return numeroPedido; }

    /** Retorna la orden de compra asociada al pedido. */
    public OrdenCompra getOrden() { return orden; }

    /** Retorna el estado actual del pedido. */
    public String getEstado() { return estado; }

    /** Retorna la transportadora asignada al pedido. */
    public Transportadora getTransportadora() { return transportadora; }

    // --- Metodos ---

    /** Empaca el pedido si la orden esta confirmada. */
    public void empacar() {
        if (!estado.equals(PENDIENTE)) {
            throw new IllegalStateException(
                "El pedido ya fue empacado. Estado: " + estado);
        }
        if (!orden.getEstado().equals(OrdenCompra.CONFIRMADA)) {
            throw new IllegalStateException(
                "Solo se pueden empacar ordenes confirmadas.");
        }
        this.estado = EMPACADO;
        System.out.println("Pedido " + numeroPedido + " empacado. " +
                           "Productos: " + orden.getDetalles().size());
    }

    /** Asigna una transportadora al pedido empacado y lo pone en despacho. */
    public void asignarTransporte(Transportadora empresa) {
        if (!estado.equals(EMPACADO)) {
            throw new IllegalStateException(
                "El pedido debe estar empacado antes de asignar transporte.");
        }
        this.transportadora = empresa;
        this.estado = TRANSPORTE_ASIGNADO;
        System.out.println("Transportadora asignada al pedido " + numeroPedido + ".");

        if (empresa.recibirPedido(this)) {
            this.estado = EN_DESPACHO;
            System.out.println("Pedido " + numeroPedido + " en despacho.");
        }
    }

    @Override
    public String toString() {
        String envio = (transportadora != null)
            ? transportadora.getEstadoEnvio()
            : "sin asignar";
        return "  PEDIDO # "  + numeroPedido        + "\n" +
               "  estado : "  + estado              + "\n" +
               "  orden  : "  + orden.getNumeroOrden() + "\n" +
               "  envio  : "  + envio               + "\n";
    }
}
