package ClasesTeleventas;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Representa el catalogo de productos disponibles en TeleVentas.
 *
 * Permite listar, buscar y enviar productos, asi como gestionar
 * las suscripciones de los clientes para recibir el catalogo por correo.
 */
public class Catalogo {

    // Atributos privados
    private int numeroCatalogo;
    private LocalDate fecha;
    private List<Producto> productos;
    private List<Cliente> suscriptores;

    // --- Constructores ---

    /** Inicializa el catalogo con un numero identificador y una lista de productos. */
    public Catalogo(int numeroCatalogo, List<Producto> productos) {
        this.numeroCatalogo = numeroCatalogo;
        this.fecha          = LocalDate.now();
        this.productos      = productos != null ? productos : new ArrayList<>();
        this.suscriptores   = new ArrayList<>();
    }

    /** Inicializa el catalogo con un numero identificador y sin productos. */
    public Catalogo(int numeroCatalogo) {
        this(numeroCatalogo, null);
    }

    // --- Getters ---

    /** Retorna el numero identificador del catalogo. */
    public int getNumeroCatalogo() { return numeroCatalogo; }

    /** Retorna la fecha de creacion del catalogo. */
    public LocalDate getFecha() { return fecha; }

    /** Retorna la lista de productos del catalogo. */
    public List<Producto> getProductos() { return productos; }

    // --- Metodos ---

    /** Retorna la lista de productos del catalogo. */
    public List<Producto> listaProductos() {
        return new ArrayList<>(productos);
    }

    /** Busca productos cuya descripcion contenga el termino ingresado. */
    public List<Producto> buscarProducto(String termino) {
        List<Producto> resultados = new ArrayList<>();
        for (Producto p : productos) {
            if (p.getDescripcion().toLowerCase().contains(termino.toLowerCase())) {
                resultados.add(p);
            }
        }
        if (resultados.isEmpty()) {
            System.out.println("No se encontraron productos con '" + termino + "'.");
        }
        return resultados;
    }

    /** Suscribe a un cliente al catalogo para recibir envios periodicos. */
    public void suscribir(Cliente cliente) {
        if (suscriptores.contains(cliente)) {
            throw new IllegalArgumentException(
                "El cliente " + cliente.getNombre() + " ya esta suscrito.");
        }
        suscriptores.add(cliente);
        System.out.println("El cliente " + cliente.getNombre() +
                           " ha sido suscrito al catalogo " + numeroCatalogo + ".");
    }

    /** Envia el catalogo completo al correo del cliente. */
    public void enviarCatalogo(Cliente cliente) {
        System.out.println("Catalogo " + numeroCatalogo +
                           " enviado a " + cliente.getCorreo() + ".");
    }

    /** Agrega un nuevo producto al catalogo si no existe previamente. */
    public void agregarProducto(Producto producto) {
        if (productos.contains(producto)) {
            throw new IllegalArgumentException(
                "El producto " + producto.getDescripcion() + " ya esta en el catalogo.");
        }
        productos.add(producto);
        System.out.println("Producto '" + producto.getDescripcion() + "' agregado al catalogo.");
    }

    @Override
    public String toString() {
        return "  CATALOGO # "  + numeroCatalogo        + "\n" +
               "  fecha       : " + fecha               + "\n" +
               "  productos   : " + productos.size()    + "\n" +
               "  suscriptores: " + suscriptores.size() + "\n";
    }
}
