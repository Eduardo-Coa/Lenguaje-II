package Clases_Museo;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Clase abstracta que representa una obra de arte del museo.
 *
 * Define los atributos y comportamientos comunes de todas las obras:
 * Cuadro, Escultura y Otra. Gestiona valoracion, estado, sala,
 * restauraciones, reportes de danos y cesiones.
 */
public abstract class Obra {

    // --- Enums ---

    /** Periodos historicos del arte. */
    public enum Periodo {
        RENACIMIENTO("Renacimiento (siglos XV-XVI)"),
        BARROCO("Barroco (siglo XVII)"),
        ROCOCO("Rococo (siglo XVIII)"),
        NEOCLASICISMO("Neoclasicismo (siglos XVIII-XIX)"),
        ROMANTICISMO("Romanticismo (siglo XIX)"),
        REALISMO("Realismo (siglo XIX)"),
        IMPRESIONISMO("Impresionismo (finales del siglo XIX)"),
        MODERNO_CONTEMPORANEO("Arte Moderno y Contemporaneo (siglos XX-XXI)");

        private final String valor;
        Periodo(String valor) { this.valor = valor; }

        /** @return La descripcion textual del periodo. */
        public String getValor() { return valor; }
    }

    /** Estados posibles de una obra de arte. */
    public enum EstadoObra {
        EXPUESTA("Expuesta"),
        DANADA("Danada"),
        EN_RESTAURACION("En restauracion"),
        CEDIDA("Cedida");

        private final String valor;
        EstadoObra(String valor) { this.valor = valor; }

        /** @return La descripcion textual del estado. */
        public String getValor() { return valor; }
    }

    // Atributos protegidos para acceso desde subclases
    protected String titulo;
    protected String autor;
    protected Periodo periodo;
    protected LocalDate fechaCreacion;
    protected LocalDate fechaEntradaMuseo;
    protected double valoracion;
    protected EstadoObra estado;
    protected Sala sala;
    protected List<Object> restauraciones;
    protected List<Object> reportesDanos;
    protected List<Object> cesiones;
    protected List<Object> solicitudesPendientes;

    // --- Constructor ---

    /**
     * Inicializa la obra con sus datos basicos y estado inicial EXPUESTA.
     *
     * @param titulo            Titulo de la obra.
     * @param autor             Autor de la obra.
     * @param periodo           Periodo historico de la obra.
     * @param fechaCreacion     Fecha en que fue creada la obra.
     * @param fechaEntradaMuseo Fecha en que ingreso al museo.
     */
    public Obra(String titulo, String autor, Periodo periodo,
                LocalDate fechaCreacion, LocalDate fechaEntradaMuseo) {
        this.titulo                = titulo;
        this.autor                 = autor;
        this.periodo               = periodo;
        this.fechaCreacion         = fechaCreacion;
        this.fechaEntradaMuseo     = fechaEntradaMuseo;
        this.valoracion            = 0.0;
        this.estado                = EstadoObra.EXPUESTA;
        this.sala                  = null;
        this.restauraciones        = new ArrayList<>();
        this.reportesDanos         = new ArrayList<>();
        this.cesiones              = new ArrayList<>();
        this.solicitudesPendientes = new ArrayList<>();
    }

    // --- Getters ---

    /** @return El titulo de la obra. */
    public String getTitulo() { return titulo; }

    /** @return El autor de la obra. */
    public String getAutor() { return autor; }

    /** @return El periodo historico de la obra. */
    public Periodo getPeriodo() { return periodo; }

    /** @return La fecha de creacion de la obra. */
    public LocalDate getFechaCreacion() { return fechaCreacion; }

    /** @return La fecha en que la obra ingreso al museo. */
    public LocalDate getFechaEntradaMuseo() { return fechaEntradaMuseo; }

    /** @return El estado actual de la obra. */
    public EstadoObra getEstado() { return estado; }

    /** @return La valoracion economica de la obra en euros. */
    public double getValoracion() { return valoracion; }

    /** @return La sala donde esta expuesta la obra. */
    public Sala getSala() { return sala; }

    /** @return La lista de restauraciones registradas. */
    public List<Object> getRestauraciones() { return restauraciones; }

    /** Agrega una entrada de restauracion preestablecida a la obra. */
    public void agregarRestauracion(java.util.Map<String, Object> restauracion) {
        restauraciones.add(restauracion);
    }

    /** @return La lista de reportes de danos. */
    public List<Object> getReportesDanos() { return new ArrayList<>(reportesDanos); }

    /** @return La lista de cesiones registradas. */
    public List<Object> getCesiones() { return new ArrayList<>(cesiones); }

    // --- Setters ---

    /**
     * Actualiza la valoracion economica; debe ser un valor no negativo.
     *
     * @param valor Nueva valoracion en euros.
     */
    public void setValoracion(double valor) {
        if (valor < 0) throw new IllegalArgumentException("La valoracion no puede ser negativa.");
        this.valoracion = valor;
    }

    /**
     * Asigna la obra a una sala.
     *
     * @param sala Sala donde se expondra la obra.
     */
    public void setSala(Sala sala) { this.sala = sala; }

    // --- Metodos de negocio ---

    /** @return true si la obra nunca ha sido restaurada. */
    public boolean necesitaRestauracion() {
        return restauraciones.isEmpty();
    }

    /** @return true si la obra tiene actualmente una cesion activa. */
    public boolean estaCedida() {
        return estado == EstadoObra.CEDIDA;
    }

    /**
     * Registra una nueva cesion de la obra a un museo colaborador.
     *
     * @param museo   Museo receptor de la cesion.
     * @param importe Importe economico de la cesion.
     * @param inicio  Fecha de inicio de la cesion.
     * @param fin     Fecha de fin de la cesion (puede ser null si es indefinida).
     */
    public void registrarCesion(MuseoColaborador museo, double importe,
                                LocalDate inicio, LocalDate fin) {
        cesiones.add(new Object[]{museo, importe, inicio, fin});
        this.estado = EstadoObra.CEDIDA;
    }

    // --- Metodo abstracto ---

    /** @return El tipo de obra: Cuadro, Escultura u Otra. */
    public abstract String obtenerTipo();

    @Override
    public String toString() {
        return obtenerTipo() + "\n " +
               "Titulo       : " + titulo + "\n " +
               "Autor        : " + autor + "\n " +
               "Creacion     : " + fechaCreacion + "\n " +
               "Periodo      : " + periodo.getValor() + "\n " +
               "Estado       : " + estado.getValor() + "\n " +
               "Entrada museo: " + fechaEntradaMuseo + "\n " +
               String.format("Valoracion   : %.2f EUR", valoracion) + "\n";
    }
}
