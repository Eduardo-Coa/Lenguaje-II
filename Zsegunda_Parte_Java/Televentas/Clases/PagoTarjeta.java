package Clases;

/**
 * Representa un pago con tarjeta de credito en TeleVentas.
 *
 * Extiende Pago con los datos especificos de la tarjeta y valida
 * que la informacion sea correcta antes de procesar el cobro.
 */
public class PagoTarjeta extends Pago {

    // Atributos privados
    private String numeroTarjeta;
    private String titular;
    private String vencimiento;
    private String cvv;

    // --- Constructor ---

    /** Inicializa el pago con tarjeta con los datos del titular y la tarjeta. */
    public PagoTarjeta(int numeroReferencia, double monto,
                       String numeroTarjeta, String titular,
                       String vencimiento, String cvv) {
        super(numeroReferencia, monto);
        this.numeroTarjeta = numeroTarjeta;
        this.titular       = titular;
        this.vencimiento   = vencimiento;
        this.cvv           = cvv;
    }

    // --- Getters ---

    /** Retorna el numero de tarjeta enmascarado, mostrando solo los ultimos 4 digitos. */
    public String getNumeroTarjeta() {
        return "**** **** **** " + numeroTarjeta.substring(numeroTarjeta.length() - 4);
    }

    /** Retorna el nombre del titular de la tarjeta. */
    public String getTitular() { return titular; }

    /** Retorna la fecha de vencimiento de la tarjeta. */
    public String getVencimiento() { return vencimiento; }

    // --- Metodos ---

    /** Valida que los datos de la tarjeta tengan el formato correcto. */
    public boolean validarTarjeta() {
        boolean numeroValido     = numeroTarjeta.length() == 16 && numeroTarjeta.matches("\\d+");
        boolean cvvValido        = cvv.length() == 3 && cvv.matches("\\d+");
        boolean vencimientoValido = vencimiento.length() == 5 && vencimiento.contains("/");
        boolean titularValido    = !titular.isBlank();
        return numeroValido && cvvValido && vencimientoValido && titularValido;
    }

    /** Valida la tarjeta y procesa el pago, actualizando el estado segun el resultado. */
    @Override
    public boolean procesarPago() {
        if (!validarTarjeta()) {
            setEstado("rechazado");
            System.out.println("Pago rechazado. Datos de la tarjeta invalidos.");
            return false;
        }
        setEstado("aprobado");
        System.out.printf("Pago aprobado. Tarjeta %s — monto $%,.2f%n",
                getNumeroTarjeta(), getMonto());
        return true;
    }

    @Override
    public String toString() {
        return "  PAGO CON TARJETA\n" +
               "  referencia : " + getNumeroReferencia()               + "\n" +
               "  tarjeta    : " + getNumeroTarjeta()                  + "\n" +
               "  titular    : " + titular                             + "\n" +
               "  vencimiento: " + vencimiento                         + "\n" +
               String.format("  monto      : $%,.2f%n", getMonto())   +
               "  estado     : " + getEstado()                         + "\n";
    }
}
