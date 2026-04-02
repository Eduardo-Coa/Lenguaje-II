package ClasesTeleventas;
/**
 * Representa a un cliente del sistema TeleVentas.
 *
 * Extiende Usuario con direccion y correo, y permite consultar el catalogo,
 * crear y cancelar ordenes de compra, y presentar quejas.
 */
public class Cliente extends Usuario {

    // Atributos privados del cliente
    private String direccion;
    private String correo;

    // --- Constructor ---

    /** Inicializa un cliente con sus datos personales y credenciales. */
    public Cliente(String userId, String nombre, String contrasena,
                   String direccion, String correo) {
        super(userId, nombre, contrasena);
        this.direccion = direccion;
        this.correo = correo;
    }

    // --- Getters ---

    /** Retorna la direccion de entrega del cliente. */
    public String getDireccion() {
        return direccion;
    }

    /** Retorna el correo electronico del cliente. */
    public String getCorreo() {
        return correo;
    }

    // --- Setters con validacion ---

    /** Actualiza la direccion de entrega del cliente validando que no este vacia. */
    public void setDireccion(String nuevaDireccion) {
        if (nuevaDireccion == null || nuevaDireccion.isBlank()) {
            throw new IllegalArgumentException("La direccion no puede estar vacia.");
        }
        this.direccion = nuevaDireccion;
    }

    /** Actualiza el correo electronico del cliente validando que no este vacio. */
    public void setCorreo(String nuevoCorreo) {
        if (nuevoCorreo == null || nuevoCorreo.isBlank()) {
            throw new IllegalArgumentException("El correo no puede estar vacio.");
        }
        this.correo = nuevoCorreo;
    }

    // --- Metodos ---

    /** Retorna la lista de productos disponibles en el catalogo. */
    public void consultarCatalogo(Catalogo catalogo) {
        catalogo.listaProductos();
    }

    /** Crea y retorna una nueva orden de compra con los detalles y metodo de pago. */
    public OrdenCompra crearOrden(int numeroOrden, java.util.List<DetallePedido> detalles, Pago pago) {
        OrdenCompra orden = new OrdenCompra(numeroOrden, this, pago, detalles);
        System.out.println("Orden creada para cliente " + getNombre() + ".");
        return orden;
    }

    /** Cancela una orden de compra existente del cliente. */
    public void cancelarOrden(OrdenCompra orden) {
        orden.cancelar();
        System.out.println("Orden cancelada para cliente " + getNombre() + ".");
    }

    /** Registra y retorna una queja del cliente indicando el motivo. */
    public Queja presentarQueja(int numeroQueja, String motivo) {
        Queja queja = new Queja(numeroQueja, motivo, this);
        System.out.println("Queja registrada para el cliente " + getNombre() + ".");
        return queja;
    }

    @Override
    public String toString() {
        return "  CLIENTE ID : " + getUserId()    + "\n" +
               "  Nombre     : " + getNombre()    + "\n" +
               "  email      : " + correo         + "\n" +
               "  Direccion  : " + direccion      + "\n";
    }
}
