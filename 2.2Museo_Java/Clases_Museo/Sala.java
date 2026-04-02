package Clases_Museo;

import java.util.ArrayList;
import java.util.List;

/**
 * Sala del museo que agrupa obras de arte para su exposicion.
 *
 * Permite agregar y retirar obras, y ofrece una vista de las
 * obras actualmente asignadas a ella.
 */
public class Sala {

    // Atributos privados
    private String nombre;
    private List<Obra> obras;

    // --- Constructor ---

    /**
     * Inicializa la sala con un nombre y sin obras asignadas.
     *
     * @param nombre Nombre identificador de la sala.
     */
    public Sala(String nombre) {
        this.nombre = nombre;
        this.obras  = new ArrayList<>();
    }

    // --- Getters ---

    /** @return El nombre de la sala. */
    public String getNombre() { return nombre; }

    /** @return Una copia de la lista de obras en la sala. */
    public List<Obra> getObras() { return new ArrayList<>(obras); }

    // --- Metodos ---

    /**
     * Agrega una obra a la sala si no estaba asignada previamente.
     *
     * @param obra Obra a agregar.
     * @throws IllegalArgumentException si la obra ya esta en la sala.
     */
    public void agregarObra(Obra obra) {
        if (obras.contains(obra)) {
            throw new IllegalArgumentException(
                "La obra '" + obra.getTitulo() + "' ya esta en la sala '" + nombre + "'.");
        }
        obras.add(obra);
    }

    /**
     * Retira una obra de la sala.
     *
     * @param obra Obra a retirar.
     * @throws IllegalArgumentException si la obra no esta en la sala.
     */
    public void eliminarObra(Obra obra) {
        if (!obras.remove(obra)) {
            throw new IllegalArgumentException(
                "La obra '" + obra.getTitulo() + "' no esta en la sala '" + nombre + "'.");
        }
    }

    @Override
    public String toString() {
        if (obras.isEmpty()) {
            return "Sala '" + nombre + "' — sin obras asignadas.";
        }
        StringBuilder sb = new StringBuilder("Sala '" + nombre + "' (" + obras.size() + " obras):");
        for (Obra obra : obras) {
            sb.append("\n  - ").append(obra.getTitulo()).append(" (").append(obra.getAutor()).append(")");
        }
        return sb.toString();
    }
}
