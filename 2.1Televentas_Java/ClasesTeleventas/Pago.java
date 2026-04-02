package ClasesTeleventas;

import java.time.LocalDate;
import java.util.List;

/**
 * Clase abstracta que representa un metodo de pago en TeleVentas.
 *
 * Define la estructura comun para todos los tipos de pago del sistema.
 * Cada subclase debe implementar procesarPago() con su logica especifica.
 */
public abstract class Pago {

    // Estados validos
    private static final List<String> ESTADOS_VALIDOS = List.of("pendiente", "aprobado", "rechazado");

    // Atributos privados
    private int numeroReferencia;
    private double monto;
    private String estado;
    private LocalDate fecha;

    // --- Constructor ---

    /** Inicializa el pago validando que el monto sea mayor a cero. */
    public Pago(int numeroReferencia, double monto) {
        if (monto <= 0) {
            throw new IllegalArgumentException("El monto debe ser mayor a cero.");
        }
        this.numeroReferencia = numeroReferencia;
        this.monto            = monto;
        this.estado           = "pendiente";
        this.fecha            = LocalDate.now();
    }

    // --- Getters ---

    /** Retorna el numero de referencia del pago. */
    public int getNumeroReferencia() { return numeroReferencia; }

    /** Retorna el monto del pago. */
    public double getMonto() { return monto; }

    /** Retorna el estado actual del pago. */
    public String getEstado() { return estado; }

    /** Retorna la fecha en que se registro el pago. */
    public LocalDate getFecha() { return fecha; }

    // --- Setter con validacion ---

    /** Actualiza el estado del pago validando que sea un valor permitido. */
    public void setEstado(String nuevoEstado) {
        if (!ESTADOS_VALIDOS.contains(nuevoEstado)) {
            throw new IllegalArgumentException(
                "Estado invalido. Escoja uno de: " + ESTADOS_VALIDOS);
        }
        this.estado = nuevoEstado;
    }

    // --- Metodo abstracto ---

    /** Procesa el pago segun el metodo especifico. Debe implementarse en cada subclase. */
    public abstract boolean procesarPago();

    @Override
    public String toString() {
        return "  PAGO\n" +
               "  referencia : " + numeroReferencia                  + "\n" +
               String.format("  monto      : $%,.2f%n", monto)      +
               "  estado     : " + estado                            + "\n" +
               "  fecha      : " + fecha                             + "\n";
    }
}
