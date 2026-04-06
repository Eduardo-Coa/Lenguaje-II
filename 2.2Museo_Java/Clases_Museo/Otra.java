package Clases_Museo;

import java.time.LocalDate;

/**
 * Obra de arte que no encaja en las categorias de Cuadro ni Escultura.
 *
 * Extiende Obra permitiendo describir libremente el tipo de obra
 * mediante un campo de texto.
 */
public class Otra extends Obra {

    // Atributo privado
    private String tipoDescripcion;

    // --- Constructor ---

    /**
     * Inicializa la obra con todos sus datos incluyendo la descripcion del tipo.
     *
     * @param titulo            Titulo de la obra.
     * @param autor             Autor de la obra.
     * @param periodo           Periodo historico de la obra.
     * @param fechaCreacion     Fecha en que fue creada.
     * @param fechaEntradaMuseo Fecha en que ingreso al museo.
     * @param tipoDescripcion   Descripcion libre del tipo de obra.
     */
    public Otra(String titulo, String autor, Periodo periodo,
                LocalDate fechaCreacion, LocalDate fechaEntradaMuseo,
                String tipoDescripcion) {
        super(titulo, autor, periodo, fechaCreacion, fechaEntradaMuseo);
        this.tipoDescripcion = tipoDescripcion;
    }

    // --- Getter ---

    /** @return La descripcion libre del tipo de obra. */
    public String getTipoDescripcion() { return tipoDescripcion; }

    // --- Metodos ---

    /** @return El tipo de obra. */
    @Override
    public String obtenerTipo() { return "Otra"; }

    @Override
    public String toString() {
        return obtenerTipo() + "\n " +
               "Titulo       : " + titulo + "\n " +
               "Autor        : " + autor + "\n " +
               "Creacion     : " + fechaCreacion + "\n " +
               "Periodo      : " + periodo.getValor() + "\n " +
               "Tipo         : " + tipoDescripcion + "\n " +
               "Estado       : " + estado.getValor() + "\n " +
               "Entrada museo: " + fechaEntradaMuseo + "\n " +
               String.format("Valoracion   : %.2f EUR", valoracion) + "\n";
    }
}
