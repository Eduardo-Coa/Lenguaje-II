package Interfaces;

/**
 * Interfaz que deben implementar todas las empresas de transporte en TeleVentas.
 *
 * Garantiza que cualquier transportadora pueda recibir pedidos,
 * confirmar entregas y reportar el estado del envio.
 */
public interface ITransportadora {

    /** Recibe un pedido para su despacho. Retorna true si fue aceptado. */
    boolean recibirPedido(Object pedido);

    /** Confirma que el pedido fue entregado al cliente. Retorna true si fue exitoso. */
    boolean confirmarEntrega();

    /** Retorna el estado actual del envio. */
    String getEstadoEnvio();
}
