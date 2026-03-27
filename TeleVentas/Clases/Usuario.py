class Usuario:
    """
    Clase base para todos los usuarios del sistema TeleVentas.

    Almacena las credenciales y provee el metodo de autenticación
    que heredan Cliente, AgenteBodega y GerenteRelaciones.
    """

    def __init__(
        self,
        user_id: str,
        nombre: str,
        contrasena: str,
    ) -> None:        
        """Inicializa un usuario con su identificador, nombre y contraseña."""
        # Atributos privados para proteger los datos del usuario
        self.__nombre = nombre
        self.__user_id = user_id
        self.__contrasena = contrasena

    @property
    def nombre(self) -> str:
        """Retorna el nombre del usuario (solo lectura)."""
        return self.__nombre

    @property
    def user_id(self) -> str:
        """Retorna el usuario (solo lectura)."""
        return self.__user_id

    @property
    def contrasena(self) -> str:
        """Retorna la contraseña del usuario (solo lectura)."""
        return self.__contrasena

    def validar_credenciales(self, user_id: str, contrasena: str) -> bool:
        """Verifica si las credenciales ingresadas coinciden con las almacenadas."""
        return self.__user_id == user_id and self.__contrasena == contrasena

    def __str__(self) -> str:
        """Retorna una representación legible del usuario."""
        return f"Usuario(id={self.__user_id}, contrasena={self.__contrasena})"

    def __repr__(self) -> str:
        """Representación oficial del objeto."""
        return self.__str__()


# ------------------------------------ Bloque de prueba interactivo ------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------ 
if __name__ == "__main__":
    print("=== Prueba interactiva: clase Usuario ===\n")

    # Registro del usuario
    print("-- Registro --")
    user_id = input("Ingrese un ID de usuario: ").strip()
    nombre = input("Ingrese su nombre: ").strip()
    contrasena = input("Ingrese una contraseña: ").strip()

    # Se crea el objeto Usuario con los datos ingresados
    usuario = Usuario(user_id, nombre, contrasena)
    print(f"\nUsuario registrado: {usuario}\n")

    # Validación de credenciales
    print("-- Validación --")
    id_ingresado = input("Ingrese su ID para iniciar sesión: ").strip()
    contrasena_ingresada = input("Ingrese su contraseña: ").strip()

    if usuario.validar_credenciales(id_ingresado, contrasena_ingresada):
        print(f"\nAcceso concedido. Bienvenido, {usuario.nombre}.")
    else:
        print("\nAcceso denegado. ID o contraseña incorrectos.")
