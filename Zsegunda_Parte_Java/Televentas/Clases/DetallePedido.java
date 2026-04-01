package Clases;

/**
 * Representa una linea dentro de una orden de compra en TeleVentas.
 *
 * Asocia un producto con la cantidad solicitada y captura el precio
 * unitario al momento de crear el detalle.
 */
public class DetallePedido {

    // Atributos privados
    private Producto producto;
    private int cantidad;
    // Se captura el precio al momento de crear el detalle para evitar variaciones futuras
    private double precioUnidad;

    // --- Constructor ---

    /** Inicializa el detalle validando que la cantidad sea mayor a cero. */
    public DetallePedido(Producto producto, int cantidad) {
        if (cantidad <= 0) {
            throw new IllegalArgumentException("La cantidad debe ser mayor a cero.");
        }
        this.producto    = producto;
        this.cantidad    = cantidad;
        this.precioUnidad = producto.getPrecio();
    }

    // --- Getters ---

    /** Retorna el producto asociado a este detalle. */
    public Producto getProducto() {
        return producto;
    }

    /** Retorna la cantidad solicitada del producto. */
    public int getCantidad() {
        return cantidad;
    }

    /** Retorna el precio unitario capturado al momento de la orden. */
    public double getPrecioUnidad() {
        return precioUnidad;
    }

    // --- Metodos ---

    /** Calcula y retorna el subtotal multiplicando cantidad por precio unitario. */
    public double subtotal() {
        return cantidad * precioUnidad;
    }

    @Override
    public String toString() {
        return "  DETALLE\n" +
               "  producto    : " + producto.getDescripcion()              + "\n" +
               "  cantidad    : " + cantidad                               + "\n" +
               String.format("  precio unit : $%,.2f%n", precioUnidad)    +
               String.format("  subtotal    : $%,.2f%n", subtotal());
    }
}
