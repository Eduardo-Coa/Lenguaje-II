package Clases_Museo;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

/**
 * Usuario encargado de gestionar el catalogo de obras y las salas.
 *
 * Extiende Usuario con operaciones de registro, baja, asignacion
 * de sala, valoracion y reporte de danos sobre las obras.
 */
public class AgenteCatalogo extends Usuario {

    // --- Constructor ---

    /**
     * Inicializa el agente de catalogo con sus credenciales de acceso.
     *
     * @param nombreUsuario Nombre de usuario del sistema.
     * @param contrasena    Contrasena del agente.
     */
    public AgenteCatalogo(String nombreUsuario, String contrasena) {
        super(nombreUsuario, contrasena);
    }

    // --- Metodos ---

    /** @return El rol del usuario en el sistema. */
    @Override
    public String getRol() { return "Agente de Catalogo"; }

    /**
     * Agrega una obra al catalogo del museo.
     *
     * @param catalogo Catalogo donde se registrara la obra.
     * @param obra     Obra a registrar.
     * @throws SecurityException si el agente no esta autenticado.
     */
    public void registrarObra(Catalogo catalogo, Obra obra) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para registrar obras.");
        }
        catalogo.agregarObra(obra);
    }

    /**
     * Elimina una obra del catalogo del museo.
     *
     * @param catalogo Catalogo del que se retirara la obra.
     * @param obra     Obra a eliminar.
     * @throws SecurityException si el agente no esta autenticado.
     */
    public void darBajaObra(Catalogo catalogo, Obra obra) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para dar de baja obras.");
        }
        catalogo.eliminarObra(obra);
    }

    /**
     * Asigna una obra a una sala determinada.
     *
     * @param obra Obra a asignar.
     * @param sala Sala donde se expondra la obra.
     * @throws SecurityException si el agente no esta autenticado.
     */
    public void asignarSala(Obra obra, Sala sala) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para asignar salas.");
        }
        obra.setSala(sala);
        sala.agregarObra(obra);
    }

    /**
     * Registra un reporte de dano sobre una obra y cambia su estado a DANADA.
     *
     * @param obra        Obra danada.
     * @param descripcion Descripcion del dano observado.
     * @throws SecurityException si el agente no esta autenticado.
     */
    public void reportarDanio(Obra obra, String descripcion) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para reportar danos.");
        }
        Map<String, Object> reporte = new HashMap<>();
        reporte.put("fecha", LocalDate.now());
        reporte.put("descripcion", descripcion);
        reporte.put("reportadoPor", nombreUsuario);
        obra.reportesDanos.add(reporte);
        obra.estado = Obra.EstadoObra.DANADA;
    }
}
