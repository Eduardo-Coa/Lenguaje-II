package Clases_Museo;

import java.time.LocalDate;

/**
 * Obra de arte tridimensional elaborada con un material especifico.
 *
 * Extiende Obra agregando el material con el que fue construida
 * la escultura.
 */
public class Escultura extends Obra {

    // --- Enum ---

    /** Materiales utilizados en la elaboracion de esculturas. */
    public enum MaterialEscultura {
        MARMOL("Marmol"),
        GRANITO("Granito"),
        BRONCE("Bronce"),
        ORO("Oro"),
        CONCRETO("Concreto"),
        MADERA("Madera");

        private final String valor;
        MaterialEscultura(String valor) { this.valor = valor; }

        /** @return La descripcion textual del material. */
        public String getValor() { return valor; }
    }

    // Atributo privado
    private MaterialEscultura material;

    // --- Constructor ---

    /**
     * Inicializa la escultura con todos sus datos incluyendo el material.
     *
     * @param titulo            Titulo de la escultura.
     * @param autor             Autor de la escultura.
     * @param periodo           Periodo historico de la escultura.
     * @param fechaCreacion     Fecha en que fue creada.
     * @param fechaEntradaMuseo Fecha en que ingreso al museo.
     * @param material          Material con el que fue elaborada.
     */
    public Escultura(String titulo, String autor, Periodo periodo,
                     LocalDate fechaCreacion, LocalDate fechaEntradaMuseo,
                     MaterialEscultura material) {
        super(titulo, autor, periodo, fechaCreacion, fechaEntradaMuseo);
        this.material = material;
    }

    // --- Getter ---

    /** @return El material con el que fue elaborada la escultura. */
    public MaterialEscultura getMaterial() { return material; }

    // --- Metodos ---

    /** @return El tipo de obra. */
    @Override
    public String obtenerTipo() { return "Escultura"; }

    @Override
    public String toString() {
        return obtenerTipo() + "\n " +
               "Titulo       : " + titulo + "\n " +
               "Autor        : " + autor + "\n " +
               "Creacion     : " + fechaCreacion + "\n " +
               "Periodo      : " + periodo.getValor() + "\n " +
               "Material     : " + material.getValor() + "\n " +
               "Estado       : " + estado.getValor() + "\n " +
               "Entrada museo: " + fechaEntradaMuseo + "\n " +
               String.format("Valoracion   : %.2f EUR", valoracion) + "\n";
    }
}
