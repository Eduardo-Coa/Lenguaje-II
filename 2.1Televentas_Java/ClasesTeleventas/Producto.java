package ClasesTeleventas;

/**
 * Representa un producto disponible en el catalogo de TeleVentas.
 *
 * Almacena el codigo, descripcion, precio y cantidad disponible.
 */
public class Producto {

    // Atributos privados del producto
    private int numeroProducto;
    private String descripcion;
    private double precio;
    private int cantidadDisponible;

    // --- Constructor ---

    /** Inicializa un producto validando que el precio y stock no sean negativos. */
    public Producto(int numeroProducto, String descripcion, double precio, int cantidadDisponible) {
        if (precio < 0) {
            throw new IllegalArgumentException("El precio no debe ser negativo.");
        }
        if (cantidadDisponible < 0) {
            throw new IllegalArgumentException("La cantidad disponible no puede ser negativa.");
        }
        this.numeroProducto = numeroProducto;
        this.descripcion = descripcion;
        this.precio = precio;
        this.cantidadDisponible = cantidadDisponible;
    }

    // --- Getters ---

    /** Retorna el codigo identificador del producto. */
    public int getNumeroProducto() {
        return numeroProducto;
    }

    /** Retorna la descripcion del producto. */
    public String getDescripcion() {
        return descripcion;
    }

    /** Retorna el precio del producto. */
    public double getPrecio() {
        return precio;
    }

    /** Retorna la cantidad disponible en stock. */
    public int getCantidadDisponible() {
        return cantidadDisponible;
    }

    // --- Setters con validacion ---

    /** Actualiza el precio del producto validando que no sea negativo. */
    public void setPrecio(double nuevoPrecio) {
        if (nuevoPrecio < 0) {
            throw new IllegalArgumentException("El precio no puede ser negativo.");
        }
        this.precio = nuevoPrecio;
    }

    /** Actualiza el stock del producto validando que no sea negativo. */
    public void setCantidadDisponible(int nuevaCantidad) {
        if (nuevaCantidad < 0) {
            throw new IllegalArgumentException("La cantidad disponible no puede ser negativa.");
        }
        this.cantidadDisponible = nuevaCantidad;
    }

    // --- Metodos ---

    /** Actualiza el precio y la cantidad disponible del producto. */
    public void actualizar(double nuevoPrecio, int nuevaCantidad) {
        setPrecio(nuevoPrecio);
        setCantidadDisponible(nuevaCantidad);
    }

    @Override
    public String toString() {
        return "  PRODUCTO # " + numeroProducto                      + "\n" +
               "  descripcion: " + descripcion                       + "\n" +
               String.format("  precio     : $%,.2f%n", precio)     +
               "  stock      : " + cantidadDisponible                + "\n";
    }
}
