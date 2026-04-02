package ClasesTeleventas;
/**
 * Clase base para todos los usuarios del sistema TeleVentas.
 *
 * Almacena las credenciales y provee el metodo de autenticacion
 * que heredan Cliente, AgenteBodega y GerenteRelaciones.
 */
public class Usuario {

    // Atributos privados para proteger los datos del usuario
    private String userId;
    private String nombre;
    private String contrasena;

    // --- Constructor ---

    /** Inicializa un usuario con su identificador, nombre y contrasena. */
    public Usuario(String userId, String nombre, String contrasena) {
        this.userId = userId;
        this.nombre = nombre;
        this.contrasena = contrasena;
    }

    // --- Getters ---

    /** Retorna el nombre del usuario. */
    public String getNombre() {
        return nombre;
    }

    /** Retorna el ID del usuario. */
    public String getUserId() {
        return userId;
    }

    /** Retorna la contrasena del usuario. */
    public String getContrasena() {
        return contrasena;
    }

    // --- Setter con validacion ---

    /** Actualiza la contrasena del usuario validando que no este vacia. */
    public void setContrasena(String nuevaContrasena) {
        if (nuevaContrasena == null || nuevaContrasena.isBlank()) {
            throw new IllegalArgumentException("La contrasena no puede estar vacia.");
        }
        this.contrasena = nuevaContrasena;
    }

    // --- Metodos ---

    /** Verifica si las credenciales ingresadas coinciden con las almacenadas. */
    public boolean validarCredenciales(String userId, String contrasena) {
        return this.userId.equals(userId) && this.contrasena.equals(contrasena);
    }

    @Override
    public String toString() {
        return "Usuario(id=" + userId + ", nombre=" + nombre + ")";
    }
}
