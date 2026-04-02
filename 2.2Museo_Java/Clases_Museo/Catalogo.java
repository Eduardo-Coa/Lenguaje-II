package Clases_Museo;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Gestiona el conjunto de obras de arte registradas en el museo.
 *
 * Permite agregar, eliminar y consultar obras por distintos
 * criterios: autor, periodo, estado, sala y tipo.
 */
public class Catalogo {

    // Atributo privado
    private List<Obra> obras;

    // --- Constructor ---

    /** Inicializa el catalogo con una lista de obras vacia. */
    public Catalogo() {
        this.obras = new ArrayList<>();
    }

    // --- Getter ---

    /** @return Una copia de la lista de obras registradas. */
    public List<Obra> getObras() { return new ArrayList<>(obras); }

    // --- Metodos de registro ---

    /**
     * Agrega una obra al catalogo si no estaba registrada.
     *
     * @param obra Obra a agregar.
     * @throws IllegalArgumentException si la obra ya esta en el catalogo.
     */
    public void agregarObra(Obra obra) {
        if (obras.contains(obra)) {
            throw new IllegalArgumentException(
                "La obra '" + obra.getTitulo() + "' ya esta registrada en el catalogo.");
        }
        obras.add(obra);
    }

    /**
     * Elimina una obra del catalogo.
     *
     * @param obra Obra a eliminar.
     * @throws IllegalArgumentException si la obra no esta en el catalogo.
     */
    public void eliminarObra(Obra obra) {
        if (!obras.remove(obra)) {
            throw new IllegalArgumentException(
                "La obra '" + obra.getTitulo() + "' no esta en el catalogo.");
        }
    }

    // --- Consultas ---

    /**
     * Retorna las obras de un autor dado (busqueda insensible a mayusculas).
     *
     * @param autor Nombre del autor a buscar.
     * @return Lista de obras del autor.
     */
    public List<Obra> buscarPorAutor(String autor) {
        String autorLower = autor.toLowerCase();
        return obras.stream()
            .filter(o -> o.getAutor().toLowerCase().equals(autorLower))
            .collect(Collectors.toList());
    }

    /**
     * Retorna las obras correspondientes a un periodo artistico.
     *
     * @param periodo Periodo historico a filtrar.
     * @return Lista de obras del periodo.
     */
    public List<Obra> buscarPorPeriodo(Obra.Periodo periodo) {
        return obras.stream()
            .filter(o -> o.getPeriodo() == periodo)
            .collect(Collectors.toList());
    }

    /**
     * Retorna las obras que se encuentran en un estado determinado.
     *
     * @param estado Estado de la obra a filtrar.
     * @return Lista de obras en ese estado.
     */
    public List<Obra> buscarPorEstado(Obra.EstadoObra estado) {
        return obras.stream()
            .filter(o -> o.getEstado() == estado)
            .collect(Collectors.toList());
    }

    /**
     * Retorna las obras asignadas a una sala, ordenadas por titulo.
     *
     * @param sala Sala por la que filtrar.
     * @return Lista de obras en la sala, ordenadas alfabeticamente.
     */
    public List<Obra> buscarPorSala(Sala sala) {
        return obras.stream()
            .filter(o -> sala.equals(o.getSala()))
            .sorted(Comparator.comparing(Obra::getTitulo))
            .collect(Collectors.toList());
    }

    /**
     * Retorna las obras de un tipo concreto: Cuadro, Escultura u Otra.
     *
     * @param tipo Tipo de obra a filtrar.
     * @return Lista de obras del tipo indicado.
     */
    public List<Obra> buscarPorTipo(String tipo) {
        return obras.stream()
            .filter(o -> o.obtenerTipo().equals(tipo))
            .collect(Collectors.toList());
    }

    @Override
    public String toString() {
        if (obras.isEmpty()) {
            return "El catalogo esta vacio.";
        }
        StringBuilder sb = new StringBuilder("Catalogo (" + obras.size() + " obras):");
        for (Obra obra : obras) {
            sb.append("\n  - ").append(obra);
        }
        return sb.toString();
    }
}
