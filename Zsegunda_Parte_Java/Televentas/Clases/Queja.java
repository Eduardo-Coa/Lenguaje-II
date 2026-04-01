package Clases;

import java.time.LocalDate;

/**
 * Representa una queja presentada por un cliente en el sistema TeleVentas.
 *
 * Registra el motivo, la fecha y el estado del reclamo, y permite
 * remitirla al gerente de relaciones para su atencion.
 */
public class Queja {

    // Estados validos
    public static final String REGISTRADA  = "registrada";
    public static final String EN_REVISION = "en_revision";
    public static final String RESUELTA    = "resuelta";
    public static final String CERRADA     = "cerrada";

    // Atributos privados
    private int numeroQueja;
    private LocalDate fecha;
    private String motivo;
    private String estado;
    private Cliente cliente;

    // --- Constructor ---

    /** Inicializa una queja validando que el motivo no este vacio. */
    public Queja(int numeroQueja, String motivo, Cliente cliente) {
        if (motivo == null || motivo.isBlank()) {
            throw new IllegalArgumentException("El motivo de la queja no puede estar vacio.");
        }
        this.numeroQueja = numeroQueja;
        this.fecha       = LocalDate.now();
        this.motivo      = motivo.strip();
        this.estado      = REGISTRADA;
        this.cliente     = cliente;
    }

    // --- Getters ---

    /** Retorna el numero identificador de la queja. */
    public int getNumeroQueja() {
        return numeroQueja;
    }

    /** Retorna la fecha en que se registro la queja. */
    public LocalDate getFecha() {
        return fecha;
    }

    /** Retorna el motivo de la queja. */
    public String getMotivo() {
        return motivo;
    }

    /** Retorna el estado actual de la queja. */
    public String getEstado() {
        return estado;
    }

    /** Retorna el cliente que presento la queja. */
    public Cliente getCliente() {
        return cliente;
    }

    // --- Metodos ---

    /** Confirma el registro de la queja si aun no ha sido procesada. */
    public void registrarQueja() {
        if (!estado.equals(REGISTRADA)) {
            throw new IllegalStateException("La queja ya fue procesada. Estado: " + estado);
        }
        System.out.println("Queja " + numeroQueja + " registrada. " +
                           "Cliente: " + cliente.getNombre() + ". " +
                           "Motivo: " + motivo);
    }

    /** Cambia el estado de la queja a EN_REVISION y la remite al gerente. */
    public void remitirGerente() {
        if (!estado.equals(REGISTRADA)) {
            throw new IllegalStateException("La queja ya fue procesada. Estado: " + estado);
        }
        this.estado = EN_REVISION;
        System.out.println("Queja #" + numeroQueja + " remitida al gerente.\n" +
                           "  Cliente: " + cliente.getNombre() + ".\n");
    }

    @Override
    public String toString() {
        return "QUEJA # "   + numeroQueja          + "\n" +
               "  fecha  : " + fecha               + "\n" +
               "  motivo : " + motivo              + "\n" +
               "  estado : " + estado              + "\n" +
               "  cliente: " + cliente.getNombre() + "\n";
    }
}
