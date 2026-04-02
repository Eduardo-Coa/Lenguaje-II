package Clases_Museo;

/**
 * Museo colaborador con el que se pueden gestionar cesiones de obras.
 *
 * Almacena el nombre y el pais del museo para identificarlo
 * dentro del sistema de cesiones.
 */
public class MuseoColaborador {

    // Atributos privados
    private String nombre;
    private String pais;

    // --- Constructor ---

    /**
     * Inicializa el museo colaborador con su nombre y pais.
     *
     * @param nombre Nombre del museo colaborador.
     * @param pais   Pais donde se ubica el museo.
     */
    public MuseoColaborador(String nombre, String pais) {
        this.nombre = nombre;
        this.pais   = pais;
    }

    // --- Getters ---

    /** @return El nombre del museo colaborador. */
    public String getNombre() { return nombre; }

    /** @return El pais donde se ubica el museo colaborador. */
    public String getPais() { return pais; }

    @Override
    public String toString() {
        return "Museo '" + nombre + "' (" + pais + ")";
    }
}
