package ClasesTeleventas;

/**
 * Representa una empresa de transporte en TeleVentas.
 *
 * Gestiona la recepcion, traslado y confirmacion de entrega
 * de los pedidos despachados.
 */
public class Transportadora {

    // Estados validos
    public static final String SIN_PEDIDO = "sin_pedido";
    public static final String RECIBIDO   = "recibido";
    public static final String EN_CAMINO  = "en_camino";
    public static final String ENTREGADO  = "entregado";

    // Atributos privados
    private int id;
    private String nombre;
    private String estado;
    private Pedido pedido;

    // --- Constructor ---

    /** Inicializa la transportadora sin pedido asignado. */
    public Transportadora(int id, String nombre) {
        this.id     = id;
        this.nombre = nombre;
        this.estado = SIN_PEDIDO;
        this.pedido = null;
    }

    // --- Getters ---

    /** Retorna el identificador de la transportadora. */
    public int getId() { return id; }

    /** Retorna el nombre de la transportadora. */
    public String getNombre() { return nombre; }

    /** Retorna el estado actual del envio. */
    public String getEstadoEnvio() { return estado; }

    // --- Metodos ---

    /** Recibe un pedido y lo pone en camino. Retorna false si ya tiene uno asignado. */
    public boolean recibirPedido(Pedido pedido) {
        if (!estado.equals(SIN_PEDIDO)) {
            System.out.println("Transportadora " + nombre + " ya tiene un pedido asignado.");
            return false;
        }
        this.pedido = pedido;
        this.estado = RECIBIDO;
        System.out.println("Transportadora " + nombre + " recibio el pedido " + pedido.getNumeroPedido() + ".");
        this.estado = EN_CAMINO;
        System.out.println("Pedido en camino con " + nombre + ".");
        return true;
    }

    /** Confirma la entrega del pedido en camino. Lanza error si no hay pedido activo. */
    public boolean confirmarEntrega() {
        if (!estado.equals(EN_CAMINO)) {
            throw new IllegalStateException(
                "No hay pedido en camino. Estado actual: " + estado);
        }
        this.estado = ENTREGADO;
        System.out.println("Transportadora " + nombre + " confirmo la entrega " +
                           "del pedido " + pedido.getNumeroPedido() + ".");
        return true;
    }

    @Override
    public String toString() {
        return "  TRANSPORTADORA # " + id    + "\n" +
               "  nombre : "  + nombre       + "\n" +
               "  estado : "  + estado       + "\n";
    }
}
