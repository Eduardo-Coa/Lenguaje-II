package ClasesTeleventas;

import java.time.LocalDate;
import java.util.List;

/**
 * Representa una orden de compra realizada por un cliente en TeleVentas.
 *
 * Agrupa los detalles del pedido, el metodo de pago y el estado actual.
 */
public class OrdenCompra {

    // Estados validos
    public static final String PENDIENTE   = "pendiente";
    public static final String CONFIRMADA  = "confirmada";
    public static final String CANCELADA   = "cancelada";
    public static final String EN_DESPACHO = "en_despacho";
    public static final String ENTREGADA   = "entregada";

    // Atributos privados
    private int numeroOrden;
    private LocalDate fecha;
    private String estado;
    private Cliente cliente;
    private Pago pago;
    private List<DetallePedido> detalles;

    // --- Constructor ---

    /** Inicializa la orden validando que tenga al menos un producto. */
    public OrdenCompra(int numeroOrden, Cliente cliente, Pago pago, List<DetallePedido> detalles) {
        if (detalles == null || detalles.isEmpty()) {
            throw new IllegalArgumentException("La orden debe tener al menos un producto.");
        }
        this.numeroOrden = numeroOrden;
        this.fecha       = LocalDate.now();
        this.estado      = PENDIENTE;
        this.cliente     = cliente;
        this.pago        = pago;
        this.detalles    = detalles;
    }

    // --- Getters ---

    /** Retorna el numero identificador de la orden. */
    public int getNumeroOrden() { return numeroOrden; }

    /** Retorna la fecha en que se creo la orden. */
    public LocalDate getFecha() { return fecha; }

    /** Retorna el estado actual de la orden. */
    public String getEstado() { return estado; }

    /** Retorna el cliente que realizo la orden. */
    public Cliente getCliente() { return cliente; }

    /** Retorna el metodo de pago asociado a la orden. */
    public Pago getPago() { return pago; }

    /** Retorna la lista de detalles de productos de la orden. */
    public List<DetallePedido> getDetalles() { return detalles; }

    // --- Metodos ---

    /** Calcula y retorna el valor total de la orden sumando los subtotales. */
    public double calcularTotal() {
        double total = 0;
        for (DetallePedido d : detalles) {
            total += d.subtotal();
        }
        return total;
    }

    /** Confirma la orden procesando el pago. */
    public void confirmar() {
        if (!estado.equals(PENDIENTE)) {
            throw new IllegalStateException(
                "Solo se puede confirmar una orden pendiente. Estado actual: " + estado);
        }
        if (!pago.procesarPago()) {
            throw new IllegalStateException("El pago no pudo procesarse.");
        }
        this.estado = CONFIRMADA;
        System.out.println("Orden " + numeroOrden + " confirmada con exito.");
    }

    /** Cancela la orden si aun no ha sido entregada. */
    public void cancelar() {
        if (estado.equals(ENTREGADA)) {
            throw new IllegalStateException("Ya no se puede cancelar, la orden fue entregada.");
        }
        this.estado = CANCELADA;
        System.out.println("Orden " + numeroOrden + " cancelada.");
    }

    @Override
    public String toString() {
        StringBuilder detallesStr = new StringBuilder();
        for (DetallePedido d : detalles) {
            detallesStr.append(String.format("    [%d] %s  x%d  —  $%,.2f%n",
                d.getProducto().getNumeroProducto(),
                d.getProducto().getDescripcion(),
                d.getCantidad(),
                d.subtotal()));
        }
        return "  ORDEN # "   + numeroOrden                         + "\n" +
               "  fecha   : " + fecha                               + "\n" +
               "  estado  : " + estado                              + "\n" +
               "  cliente : " + cliente.getNombre()                 + "\n" +
               String.format("  total   : $%,.2f%n", calcularTotal()) +
               "  detalle :\n" + detallesStr;
    }
}
