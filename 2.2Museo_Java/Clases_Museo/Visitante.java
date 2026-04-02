package Clases_Museo;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Usuario publico que puede consultar obras por sala desde el vestibulo.
 *
 * Extiende Usuario con la capacidad de listar las obras de una
 * sala ordenadas alfabeticamente por titulo.
 */
public class Visitante extends Usuario {

    // --- Constructor ---

    /**
     * Inicializa el visitante con sus credenciales de acceso.
     *
     * @param nombreUsuario Nombre de usuario del sistema.
     * @param contrasena    Contrasena del visitante.
     */
    public Visitante(String nombreUsuario, String contrasena) {
        super(nombreUsuario, contrasena);
    }

    // --- Metodos ---

    /** @return El rol del usuario en el sistema. */
    @Override
    public String getRol() { return "Visitante"; }

    /**
     * Retorna las obras asignadas a una sala, ordenadas por titulo.
     *
     * @param sala Sala cuyas obras se desean consultar.
     * @return Lista de obras de la sala ordenadas alfabeticamente.
     * @throws SecurityException si el visitante no esta autenticado.
     */
    public List<Obra> consultarObrasPorSala(Sala sala) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para consultar obras.");
        }
        List<Obra> resultado = new ArrayList<>(sala.getObras());
        resultado.sort(Comparator.comparing(Obra::getTitulo));
        return resultado;
    }
}
