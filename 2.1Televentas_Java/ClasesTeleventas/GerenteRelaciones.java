package ClasesTeleventas;

import java.util.ArrayList;
import java.util.List;

/**
 * Representa al gerente de relaciones del sistema TeleVentas.
 *
 * Extiende Usuario y es responsable de recibir y gestionar
 * las quejas remitidas por los clientes.
 */
public class GerenteRelaciones extends Usuario {

    // Lista que acumula las quejas recibidas durante la sesion
    private List<Queja> quejas;

    // --- Constructor ---

    /** Inicializa el gerente con sus credenciales y una lista vacia de quejas. */
    public GerenteRelaciones(String userId, String contrasena, String nombre) {
        super(userId, nombre, contrasena);
        this.quejas = new ArrayList<>();
    }

    // --- Getters ---

    /** Retorna la lista de quejas recibidas por el gerente. */
    public List<Queja> getQuejas() {
        return quejas;
    }

    // --- Metodos ---

    /** Recibe una queja ya remitida y la agrega a la lista del gerente. */
    public void recibirQueja(Queja queja) {
        if (!queja.getEstado().equals(Queja.EN_REVISION)) {
            throw new IllegalStateException(
                "La queja no ha sido remitida aun. Estado actual: " + queja.getEstado());
        }
        quejas.add(queja);
        System.out.println("Gerente " + getNombre() + " recibio la queja " + queja.getNumeroQueja() + ". " +
                           "Cliente: " + queja.getCliente().getNombre() + ". " +
                           "Motivo: " + queja.getMotivo());
    }

    @Override
    public String toString() {
        return "  GERENTE DE RELACIONES\n" +
               "  id     : " + getUserId()   + "\n" +
               "  nombre : " + getNombre()   + "\n" +
               "  quejas : " + quejas.size() + "\n";
    }
}
