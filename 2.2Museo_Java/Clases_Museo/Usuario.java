package Clases_Museo;

/**
 * Clase abstracta base para todos los usuarios del sistema Museo.
 *
 * Almacena las credenciales y provee autenticacion y cierre de sesion
 * que heredan Visitante, AgenteCatalogo, AgenteRestaurador y DirectorMuseo.
 */
public abstract class Usuario {

    // Atributos protegidos para acceso desde las subclases
    protected String nombreUsuario;
    protected String contrasena;
    protected boolean autenticado;

    // --- Constructor ---

    /**
     * Inicializa el usuario con credenciales y sesion cerrada.
     *
     * @param nombreUsuario Nombre de usuario del sistema.
     * @param contrasena    Contrasena del usuario.
     */
    public Usuario(String nombreUsuario, String contrasena) {
        this.nombreUsuario = nombreUsuario;
        this.contrasena    = contrasena;
        this.autenticado   = false;
    }

    // --- Getters ---

    /** @return El nombre de usuario. */
    public String getNombreUsuario() { return nombreUsuario; }

    /** @return true si el usuario tiene sesion activa. */
    public boolean isAutenticado() { return autenticado; }

    // --- Setter con validacion ---

    /**
     * Actualiza la contrasena del usuario validando que no este vacia.
     *
     * @param nueva Nueva contrasena a establecer.
     */
    public void setContrasena(String nueva) {
        if (nueva == null || nueva.isBlank()) {
            throw new IllegalArgumentException("La contrasena no puede estar vacia.");
        }
        this.contrasena = nueva;
    }

    // --- Metodos ---

    /**
     * Verifica la contrasena y marca al usuario como autenticado.
     *
     * @param contrasena Contrasena a verificar.
     * @return true si la contrasena es correcta.
     */
    public boolean autenticar(String contrasena) {
        this.autenticado = this.contrasena.equals(contrasena);
        return this.autenticado;
    }

    /** Cierra la sesion del usuario. */
    public void cerrarSesion() {
        this.autenticado = false;
    }

    // --- Metodo abstracto ---

    /** @return El rol del usuario en el sistema. */
    public abstract String getRol();

    @Override
    public String toString() {
        return "Usuario(" + nombreUsuario + ", rol=" + getRol() + ")";
    }
}
