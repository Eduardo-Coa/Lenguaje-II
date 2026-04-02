package Clases_Museo;

import java.time.LocalDate;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Usuario encargado de gestionar las restauraciones de las obras.
 *
 * Extiende Usuario con operaciones para iniciar y finalizar
 * restauraciones, consultar su historial y detectar obras pendientes.
 */
public class AgenteRestaurador extends Usuario {

    // --- Constructor ---

    /**
     * Inicializa el agente restaurador con sus credenciales de acceso.
     *
     * @param nombreUsuario Nombre de usuario del sistema.
     * @param contrasena    Contrasena del agente.
     */
    public AgenteRestaurador(String nombreUsuario, String contrasena) {
        super(nombreUsuario, contrasena);
    }

    // --- Metodos ---

    /** @return El rol del usuario en el sistema. */
    @Override
    public String getRol() { return "Agente Restaurador"; }

    /**
     * Inicia una restauracion sobre una obra y cambia su estado a EN_RESTAURACION.
     *
     * @param obra Obra sobre la que se iniciara la restauracion.
     * @throws SecurityException si el agente no esta autenticado.
     */
    public void iniciarRestauracion(Obra obra) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para iniciar restauraciones.");
        }
        Map<String, Object> restauracion = new HashMap<>();
        restauracion.put("fechaInicio", LocalDate.now());
        restauracion.put("fechaFin", null);
        obra.restauraciones.add(restauracion);
        obra.estado = Obra.EstadoObra.EN_RESTAURACION;
    }

    /**
     * Finaliza la restauracion activa de una obra y registra la fecha de fin.
     *
     * @param obra Obra con restauracion en curso.
     * @throws SecurityException        si el agente no esta autenticado.
     * @throws IllegalArgumentException si la obra no tiene restauracion activa.
     */
    @SuppressWarnings("unchecked")
    public void finalizarRestauracion(Obra obra) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para finalizar restauraciones.");
        }
        Map<String, Object> activa = null;
        for (Object r : obra.restauraciones) {
            Map<String, Object> map = (Map<String, Object>) r;
            if (map.get("fechaFin") == null) {
                activa = map;
                break;
            }
        }
        if (activa == null) {
            throw new IllegalArgumentException(
                "La obra '" + obra.getTitulo() + "' no tiene una restauracion activa.");
        }
        activa.put("fechaFin", LocalDate.now());
        obra.estado = Obra.EstadoObra.EXPUESTA;
    }

    /**
     * Retorna el historial de restauraciones de una obra, ordenado por fecha de inicio.
     *
     * @param obra Obra de la que se consultara el historial.
     * @return Lista de restauraciones ordenada cronologicamente.
     * @throws SecurityException si el agente no esta autenticado.
     */
    @SuppressWarnings("unchecked")
    public List<Object> consultarRestauraciones(Obra obra) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para consultar restauraciones.");
        }
        return obra.restauraciones.stream()
            .sorted(Comparator.comparing(r ->
                (LocalDate) ((Map<String, Object>) r).get("fechaInicio")))
            .collect(Collectors.toList());
    }

    /**
     * Retorna las obras que nunca han sido restauradas.
     *
     * @param obras Lista de obras a verificar.
     * @return Lista de obras que necesitan restauracion.
     * @throws SecurityException si el agente no esta autenticado.
     */
    public List<Obra> verificarObrasPendientes(List<Obra> obras) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para verificar obras pendientes.");
        }
        return obras.stream()
            .filter(Obra::necesitaRestauracion)
            .collect(Collectors.toList());
    }
}
