package Clases_Museo;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Usuario con maximos privilegios: gestiona salas, cesiones y museos colaboradores.
 *
 * Extiende Usuario con operaciones de administracion del museo:
 * agregar y eliminar salas, registrar museos colaboradores,
 * ceder obras y consultar la valoracion total del catalogo.
 */
public class DirectorMuseo extends Usuario {

    // Atributos privados
    private List<MuseoColaborador> museosColaboradores;
    private List<Sala> salas;

    // --- Constructor ---

    /**
     * Inicializa el director con listas vacias de salas y museos colaboradores.
     *
     * @param nombreUsuario Nombre de usuario del sistema.
     * @param contrasena    Contrasena del director.
     */
    public DirectorMuseo(String nombreUsuario, String contrasena) {
        super(nombreUsuario, contrasena);
        this.museosColaboradores = new ArrayList<>();
        this.salas               = new ArrayList<>();
    }

    // --- Getters ---

    /** @return La lista de museos colaboradores registrados. */
    public List<MuseoColaborador> getMuseosColaboradores() {
        return new ArrayList<>(museosColaboradores);
    }

    /** @return La lista de salas del museo. */
    public List<Sala> getSalas() { return new ArrayList<>(salas); }

    // --- Metodos ---

    /** @return El rol del usuario en el sistema. */
    @Override
    public String getRol() { return "Director del Museo"; }

    /**
     * Agrega una sala al museo si no estaba registrada.
     *
     * @param sala Sala a agregar.
     * @throws SecurityException si el director no esta autenticado.
     */
    public void agregarSala(Sala sala) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para agregar salas.");
        }
        if (!salas.contains(sala)) {
            salas.add(sala);
        }
    }

    /**
     * Elimina una sala del museo.
     *
     * @param sala Sala a eliminar.
     * @throws SecurityException        si el director no esta autenticado.
     * @throws IllegalArgumentException si la sala no existe en el museo.
     */
    public void eliminarSala(Sala sala) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para eliminar salas.");
        }
        if (!salas.remove(sala)) {
            throw new IllegalArgumentException(
                "La sala '" + sala.getNombre() + "' no existe en el museo.");
        }
    }

    /**
     * Agrega un museo al listado de colaboradores si no estaba registrado.
     *
     * @param museo Museo colaborador a registrar.
     * @throws SecurityException si el director no esta autenticado.
     */
    public void agregarMuseoColaborador(MuseoColaborador museo) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para agregar museos colaboradores.");
        }
        if (!museosColaboradores.contains(museo)) {
            museosColaboradores.add(museo);
        }
    }

    /**
     * Cede una obra a un museo colaborador registrando importe y periodo.
     *
     * @param obra   Obra a ceder.
     * @param museo  Museo colaborador receptor.
     * @param importe Importe economico de la cesion; debe ser no negativo.
     * @param inicio Fecha de inicio de la cesion.
     * @param fin    Fecha de fin de la cesion (puede ser null si es indefinida).
     * @throws SecurityException        si el director no esta autenticado.
     * @throws IllegalArgumentException si el museo no es colaborador o el importe es negativo.
     */
    public void cederObra(Obra obra, MuseoColaborador museo, double importe,
                          LocalDate inicio, LocalDate fin) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para ceder obras.");
        }
        if (!museosColaboradores.contains(museo)) {
            throw new IllegalArgumentException(
                "El museo '" + museo.getNombre() + "' no esta en la lista de colaboradores.");
        }
        if (importe < 0) {
            throw new IllegalArgumentException("El importe de la cesion no puede ser negativo.");
        }
        obra.registrarCesion(museo, importe, inicio, fin);
    }

    /**
     * Retorna la suma de las valoraciones de todas las obras del catalogo.
     *
     * @param catalogo Catalogo cuyas obras se sumaran.
     * @return Total en euros de todas las valoraciones.
     * @throws SecurityException si el director no esta autenticado.
     */
    public double consultarValoracionTotal(Catalogo catalogo) {
        if (!autenticado) {
            throw new SecurityException("Debe autenticarse para consultar la valoracion total.");
        }
        return catalogo.getObras().stream()
            .mapToDouble(Obra::getValoracion)
            .sum();
    }
}
