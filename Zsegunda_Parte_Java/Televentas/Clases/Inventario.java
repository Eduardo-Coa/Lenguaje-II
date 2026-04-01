package Clases;

import java.util.HashMap;
import java.util.Map;

/**
 * Representa el sistema de inventario externo de TeleVentas.
 *
 * Permite consultar productos, verificar disponibilidad y actualizar
 * el stock al momento de empacar pedidos.
 */
public class Inventario {

    // Atributos privados
    private String urlApi;
    private String nombre;
    // Mapa interno que simula la base de datos del inventario
    private Map<Integer, Map<String, Object>> productos;

    // --- Constructor ---

    /** Inicializa el inventario con su URL de API y nombre identificador. */
    public Inventario(String urlApi, String nombre) {
        this.urlApi    = urlApi;
        this.nombre    = nombre;
        this.productos = new HashMap<>();
    }

    // --- Getters ---

    /** Retorna la URL de la API del inventario. */
    public String getUrlApi() { return urlApi; }

    /** Retorna el nombre del inventario. */
    public String getNombre() { return nombre; }

    // --- Metodos ---

    /** Registra un nuevo producto en el inventario con su stock inicial. */
    public void registrarProducto(int codigo, String descripcion, double precio, int stock) {
        Map<String, Object> datos = new HashMap<>();
        datos.put("codigo",      codigo);
        datos.put("descripcion", descripcion);
        datos.put("precio",      precio);
        datos.put("stock",       stock);
        productos.put(codigo, datos);
        System.out.println("Producto '" + descripcion + "' registrado en inventario.");
    }

    /** Retorna la informacion de un producto por su codigo. Lanza error si no existe. */
    public Map<String, Object> consultarProducto(int codigo) {
        if (!productos.containsKey(codigo)) {
            throw new IllegalArgumentException(
                "Producto con codigo " + codigo + " no encontrado en inventario.");
        }
        return productos.get(codigo);
    }

    /** Descuenta la cantidad indicada del stock del producto. */
    public void actualizarStock(int codigo, int qty) {
        Map<String, Object> producto = consultarProducto(codigo);
        int stockActual = (int) producto.get("stock");
        if (stockActual < qty) {
            throw new IllegalStateException(
                "Stock insuficiente para producto " + codigo + ". " +
                "Disponible: " + stockActual + ", solicitado: " + qty);
        }
        producto.put("stock", stockActual - qty);
        System.out.println("Stock actualizado — producto " + codigo + ": " +
                           stockActual + " → " + (stockActual - qty));
    }

    /** Retorna true si el producto existe y tiene stock mayor a cero. */
    public boolean verificarDisponibilidad(int codigo) {
        try {
            Map<String, Object> producto = consultarProducto(codigo);
            return (int) producto.get("stock") > 0;
        } catch (IllegalArgumentException e) {
            return false;
        }
    }

    @Override
    public String toString() {
        return "  INVENTARIO\n" +
               "  nombre   : " + nombre             + "\n" +
               "  url      : " + urlApi             + "\n" +
               "  productos: " + productos.size()   + "\n";
    }
}
