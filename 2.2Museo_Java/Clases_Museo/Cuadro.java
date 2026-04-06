package Clases_Museo;

import java.time.LocalDate;

/**
 * Obra de arte pictorica con estilo y tecnica definidos.
 *
 * Extiende Obra agregando el estilo artistico y la tecnica
 * utilizada en la elaboracion del cuadro.
 */
public class Cuadro extends Obra {

    // --- Enums ---

    /** Estilos artisticos reconocidos en pintura. */
    public enum EstiloCuadro {
        RENACIMIENTO("Renacimiento"),
        BARROCO("Barroco"),
        ROCOCO("Rococo"),
        NEOCLASICISMO("Neoclasicismo"),
        ROMANTICISMO("Romanticismo"),
        REALISMO("Realismo"),
        IMPRESIONISMO("Impresionismo"),
        POSTIMPRESIONISMO("Postimpresionismo"),
        EXPRESIONISMO("Expresionismo"),
        CUBISMO("Cubismo"),
        SURREALISMO("Surrealismo"),
        POP_ART("Pop Art");

        private final String valor;
        EstiloCuadro(String valor) { this.valor = valor; }

        /** @return La descripcion textual del estilo. */
        public String getValor() { return valor; }
    }

    /** Tecnicas pictorias utilizadas en cuadros. */
    public enum TecnicaCuadro {
        FRESCO("Pintura al Fresco"),
        TEMPERA("Temple o Tempera"),
        OLEO("Pintura al Oleo"),
        ACUARELA("Acuarela"),
        ACRILICO("Acrilico");

        private final String valor;
        TecnicaCuadro(String valor) { this.valor = valor; }

        /** @return La descripcion textual de la tecnica. */
        public String getValor() { return valor; }
    }

    // Atributos privados
    private EstiloCuadro estilo;
    private TecnicaCuadro tecnica;

    // --- Constructor ---

    /**
     * Inicializa el cuadro con todos sus datos incluyendo estilo y tecnica.
     *
     * @param titulo            Titulo del cuadro.
     * @param autor             Autor del cuadro.
     * @param periodo           Periodo historico del cuadro.
     * @param fechaCreacion     Fecha en que fue creado.
     * @param fechaEntradaMuseo Fecha en que ingreso al museo.
     * @param estilo            Estilo artistico del cuadro.
     * @param tecnica           Tecnica pictorica utilizada.
     */
    public Cuadro(String titulo, String autor, Periodo periodo,
                  LocalDate fechaCreacion, LocalDate fechaEntradaMuseo,
                  EstiloCuadro estilo, TecnicaCuadro tecnica) {
        super(titulo, autor, periodo, fechaCreacion, fechaEntradaMuseo);
        this.estilo  = estilo;
        this.tecnica = tecnica;
    }

    // --- Getters ---

    /** @return El estilo artistico del cuadro. */
    public EstiloCuadro getEstilo() { return estilo; }

    /** @return La tecnica pictorica del cuadro. */
    public TecnicaCuadro getTecnica() { return tecnica; }

    // --- Metodos ---

    /** @return El tipo de obra. */
    @Override
    public String obtenerTipo() { return "Cuadro"; }

    @Override
    public String toString() {
        return obtenerTipo() + "\n " +
               "Titulo       : " + titulo + "\n " +
               "Autor        : " + autor + "\n " +
               "Creacion     : " + fechaCreacion + "\n " +
               "Periodo      : " + periodo.getValor() + "\n " +
               "Estilo       : " + estilo.getValor() + "\n " +
               "Tecnica      : " + tecnica.getValor() + "\n " +
               "Estado       : " + estado.getValor() + "\n " +
               "Entrada museo: " + fechaEntradaMuseo + "\n " +
               String.format("Valoracion   : %.2f EUR", valoracion) + "\n";
    }
}
