package Interfaces;

import java.util.Map;

/**
 * Interfaz que debe implementar el sistema de inventario externo de TeleVentas.
 *
 * Permite consultar productos, actualizar el stock al empacar pedidos
 * y verificar disponibilidad antes de confirmar una orden de compra.
 */
public interface IInventario {

    /** Retorna la informacion de un producto dado su codigo. */
    Map<String, Object> consultarProducto(int codigo);

    /** Descuenta la cantidad indicada del stock del producto. */
    void actualizarStock(int codigo, int qty);

    /** Retorna true si el producto existe y tiene stock disponible. */
    boolean verificarDisponibilidad(int codigo);
}
