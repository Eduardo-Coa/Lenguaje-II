import Clases_Museo.*;
import Clases_Museo.Cuadro.EstiloCuadro;
import Clases_Museo.Cuadro.TecnicaCuadro;
import Clases_Museo.Escultura.MaterialEscultura;
import Clases_Museo.Obra.EstadoObra;
import Clases_Museo.Obra.Periodo;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * Punto de entrada del sistema Museo en Java.
 * Replica el flujo interactivo del main.py de Python.
 */
public class Main {

    // --- Salas ---
    private static final Sala salaRenacimiento  = new Sala("Sala Renacimiento");
    private static final Sala salaBarroca       = new Sala("Sala Barroca");
    private static final Sala salaImpresionista = new Sala("Sala Impresionista");
    private static final List<Sala> salas = new ArrayList<>(
        Arrays.asList(salaRenacimiento, salaBarroca, salaImpresionista));

    // --- Catalogo ---
    private static final Catalogo catalogo = new Catalogo();

    // --- Museo colaborador ---
    private static final MuseoColaborador museoOrsay =
        new MuseoColaborador("Musee d'Orsay", "Francia");

    // --- Usuarios ---
    private static final List<Usuario> usuarios = Arrays.asList(
        new Visitante("visitante01",   "vis123"),
        new AgenteCatalogo("agente_cat01", "admin123"),
        new AgenteRestaurador("restaurador01", "rest456"),
        new DirectorMuseo("director01", "director789")
    );

    private static final Scanner sc = new Scanner(System.in);

    // -----------------------------------------------------------------------

    public static void main(String[] args) {
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(new ByteArrayOutputStream()));

        // Obras preestablecidas
        Cuadro     gioconda = new Cuadro("La Gioconda", "Leonardo da Vinci", Periodo.RENACIMIENTO,
                                LocalDate.of(1503,1,1), LocalDate.of(1797,8,1),
                                EstiloCuadro.RENACIMIENTO, TecnicaCuadro.OLEO);
        Cuadro     meninas  = new Cuadro("Las Meninas", "Diego Velazquez", Periodo.BARROCO,
                                LocalDate.of(1656,1,1), LocalDate.of(1819,11,19),
                                EstiloCuadro.BARROCO, TecnicaCuadro.OLEO);
        Cuadro     noche    = new Cuadro("La noche estrellada", "Vincent van Gogh", Periodo.IMPRESIONISMO,
                                LocalDate.of(1889,6,1), LocalDate.of(1941,1,1),
                                EstiloCuadro.POSTIMPRESIONISMO, TecnicaCuadro.OLEO);
        Escultura  pensador = new Escultura("El pensador", "Auguste Rodin", Periodo.IMPRESIONISMO,
                                LocalDate.of(1904,1,1), LocalDate.of(1950,3,15),
                                MaterialEscultura.BRONCE);

        gioconda.setValoracion(800_000_000.0);
        meninas .setValoracion(250_000_000.0);
        noche   .setValoracion( 50_000_000.0);
        pensador.setValoracion( 35_000_000.0);

        catalogo.agregarObra(gioconda);
        catalogo.agregarObra(meninas);
        catalogo.agregarObra(noche);
        catalogo.agregarObra(pensador);

        salaRenacimiento .agregarObra(gioconda); gioconda.setSala(salaRenacimiento);
        salaBarroca      .agregarObra(meninas);  meninas .setSala(salaBarroca);
        salaImpresionista.agregarObra(noche);    noche   .setSala(salaImpresionista);
        salaImpresionista.agregarObra(pensador); pensador.setSala(salaImpresionista);

        // Historial de restauraciones preestablecido
        gioconda.agregarRestauracion(restauracion(LocalDate.of(1956,6,1),  LocalDate.of(1956,9,15)));
        gioconda.agregarRestauracion(restauracion(LocalDate.of(2004,3,10), LocalDate.of(2004,7,20)));
        meninas .agregarRestauracion(restauracion(LocalDate.of(1984,1,15), LocalDate.of(1984,4,30)));
        noche   .agregarRestauracion(restauracion(LocalDate.of(2002,5,1),  LocalDate.of(2002,8,10)));
        noche   .agregarRestauracion(restauracion(LocalDate.of(2018,11,5), LocalDate.of(2019,2,28)));
        pensador.agregarRestauracion(restauracion(LocalDate.of(1995,7,20), LocalDate.of(1995,10,5)));

        // Director: agregar salas y museo colaborador
        DirectorMuseo director = (DirectorMuseo) usuarios.get(3);
        director.autenticar("director789");
        director.agregarSala(salaRenacimiento);
        director.agregarSala(salaBarroca);
        director.agregarSala(salaImpresionista);
        director.agregarMuseoColaborador(museoOrsay);
        director.cerrarSesion();

        System.setOut(originalOut);

        // Bienvenida
        System.out.println("\n  Bienvenido al sistema del Museo");
        separador("");
        System.out.printf("  %-20s %-22s %s%n", "Usuario", "Rol", "Contrasena");
        separador("");
        System.out.printf("  %-20s %-22s %s%n", "visitante01",   "Visitante",          "vis123");
        System.out.printf("  %-20s %-22s %s%n", "agente_cat01",  "Agente de Catalogo",  "admin123");
        System.out.printf("  %-20s %-22s %s%n", "restaurador01", "Agente Restaurador",  "rest456");
        System.out.printf("  %-20s %-22s %s%n", "director01",    "Director del Museo",  "director789");
        separador("");

        while (true) {
            Usuario usuario = login();
            if (usuario == null) {
                System.out.print("\n  Intentar de nuevo? (s/n): ");
                if (!sc.nextLine().trim().equalsIgnoreCase("s")) {
                    System.out.println("  Hasta luego.");
                    break;
                }
                continue;
            }

            if      (usuario instanceof Visitante)         menuVisitante((Visitante) usuario);
            else if (usuario instanceof AgenteCatalogo)    menuAgenteCatalogo((AgenteCatalogo) usuario);
            else if (usuario instanceof AgenteRestaurador) menuAgenteRestaurador((AgenteRestaurador) usuario);
            else if (usuario instanceof DirectorMuseo)     menuDirector((DirectorMuseo) usuario);

            System.out.print("\n  Iniciar otra sesion? (s/n): ");
            if (!sc.nextLine().trim().equalsIgnoreCase("s")) {
                System.out.println("  Hasta luego.");
                break;
            }
        }
    }

    // --- Utilidades --------------------------------------------------------

    private static Map<String, Object> restauracion(LocalDate inicio, LocalDate fin) {
        Map<String, Object> r = new HashMap<>();
        r.put("fechaInicio", inicio);
        r.put("fechaFin",    fin);
        return r;
    }

    private static void separador(String titulo) {
        System.out.println("\n" + "=".repeat(60));
        if (!titulo.isEmpty()) {
            System.out.println("  " + titulo);
            System.out.println("=".repeat(60));
        }
    }

    private static Usuario login() {
        separador("MUSEO — Inicio de sesion");
        System.out.print("  Usuario    : ");
        String uid = sc.nextLine().trim();
        System.out.print("  Contrasena : ");
        String pwd = sc.nextLine().trim();
        for (Usuario u : usuarios) {
            if (u.getNombreUsuario().equals(uid)) {
                if (u.autenticar(pwd)) {
                    System.out.println("\n  Bienvenido/a, " + u.getNombreUsuario() +
                                       "  [" + u.getRol() + "].");
                    return u;
                } else {
                    System.out.println("  Contrasena incorrecta.");
                    return null;
                }
            }
        }
        System.out.println("  Usuario no encontrado.");
        return null;
    }

    private static Obra seleccionarObra(String accion) {
        List<Obra> obras = catalogo.getObras();
        for (int i = 0; i < obras.size(); i++)
            System.out.printf("  [%d] %-12s '%s'  —  %s  |  %s%n",
                i + 1, obras.get(i).obtenerTipo(), obras.get(i).getTitulo(),
                obras.get(i).getAutor(), obras.get(i).getEstado().getValor());
        try {
            System.out.print("\n  Numero de obra a " + accion + " (0 para cancelar): ");
            int idx = Integer.parseInt(sc.nextLine().trim());
            if (idx == 0) return null;
            if (idx < 1 || idx > obras.size()) { System.out.println("  Numero fuera de rango."); return null; }
            return obras.get(idx - 1);
        } catch (IllegalArgumentException e) {
            System.out.println("  Entrada invalida.");
            return null;
        }
    }

    private static Sala seleccionarSala(String accion) {
        for (int i = 0; i < salas.size(); i++)
            System.out.printf("  [%d] %s%n", i + 1, salas.get(i).getNombre());
        try {
            System.out.print("\n  Numero de sala a " + accion + " (0 para cancelar): ");
            int idx = Integer.parseInt(sc.nextLine().trim());
            if (idx == 0) return null;
            if (idx < 1 || idx > salas.size()) { System.out.println("  Numero fuera de rango."); return null; }
            return salas.get(idx - 1);
        } catch (IllegalArgumentException e) {
            System.out.println("  Entrada invalida.");
            return null;
        }
    }

    private static LocalDate pedirFecha(String etiqueta) {
        System.out.print("  " + etiqueta + " (YYYY-MM-DD): ");
        try {
            return LocalDate.parse(sc.nextLine().trim());
        } catch (Exception e) {
            System.out.println("  Formato de fecha invalido.");
            return null;
        }
    }

    // --- Menu Visitante -----------------------------------------------------

    private static void menuVisitante(Visitante visitante) {
        while (true) {
            separador("MENU VISITANTE — " + visitante.getNombreUsuario());
            System.out.println("  1. Ver salas del museo");
            System.out.println("  2. Consultar obras por sala");
            System.out.println("  3. Buscar en catalogo");
            System.out.println("  0. Cerrar sesion");
            System.out.print("\n  Opcion: ");
            String opcion = sc.nextLine().trim();

            switch (opcion) {
                case "1" -> {
                    separador("SALAS DEL MUSEO");
                    for (Sala s : salas) System.out.println("\n" + s);
                }
                case "2" -> {
                    separador("CONSULTAR OBRAS POR SALA");
                    Sala sala = seleccionarSala("consultar");
                    if (sala == null) break;
                    List<Obra> obras = visitante.consultarObrasPorSala(sala);
                    if (obras.isEmpty()) { System.out.println("  Esta sala no tiene obras asignadas."); break; }
                    separador("OBRAS EN " + sala.getNombre().toUpperCase());
                    for (Obra o : obras)
                        System.out.printf("  - '%s'  (%s)  |  %s%n",
                            o.getTitulo(), o.getAutor(), o.getEstado().getValor());
                }
                case "3" -> {
                    separador("BUSCAR EN CATALOGO");
                    System.out.println("  1. Por autor");
                    System.out.println("  2. Por periodo");
                    System.out.println("  3. Por tipo");
                    System.out.println("  4. Por estado");
                    System.out.print("\n  Opcion: ");
                    String sub = sc.nextLine().trim();
                    List<Obra> resultados = new ArrayList<>();
                    switch (sub) {
                        case "1" -> { System.out.print("  Autor: "); resultados = catalogo.buscarPorAutor(sc.nextLine().trim()); }
                        case "2" -> {
                            Periodo[] periodos = Periodo.values();
                            for (int i = 0; i < periodos.length; i++)
                                System.out.printf("  [%d] %s%n", i + 1, periodos[i].getValor());
                            try {
                                System.out.print("  Periodo: ");
                                int idx = Integer.parseInt(sc.nextLine().trim());
                                if (idx >= 1 && idx <= periodos.length)
                                    resultados = catalogo.buscarPorPeriodo(periodos[idx - 1]);
                            } catch (IllegalArgumentException ignored) {}
                        }
                        case "3" -> { System.out.print("  Tipo (Cuadro / Escultura / Otra): "); resultados = catalogo.buscarPorTipo(sc.nextLine().trim()); }
                        case "4" -> {
                            EstadoObra[] estados = EstadoObra.values();
                            for (int i = 0; i < estados.length; i++)
                                System.out.printf("  [%d] %s%n", i + 1, estados[i].getValor());
                            try {
                                System.out.print("  Estado: ");
                                int idx = Integer.parseInt(sc.nextLine().trim());
                                if (idx >= 1 && idx <= estados.length)
                                    resultados = catalogo.buscarPorEstado(estados[idx - 1]);
                            } catch (IllegalArgumentException ignored) {}
                        }
                        default -> { System.out.println("  Opcion invalida."); }
                    }
                    if (!resultados.isEmpty()) {
                        System.out.println("\n  Resultados (" + resultados.size() + "):");
                        for (Obra r : resultados) System.out.println("  - " + r);
                    } else {
                        System.out.println("  No se encontraron obras.");
                    }
                }
                case "0" -> { visitante.cerrarSesion(); System.out.println("  Sesion cerrada."); return; }
                default  -> System.out.println("  Opcion invalida.");
            }
        }
    }

    // --- Menu Agente Catalogo ----------------------------------------------

    private static void menuAgenteCatalogo(AgenteCatalogo agente) {
        while (true) {
            separador("MENU AGENTE CATALOGO — " + agente.getNombreUsuario());
            System.out.println("  1. Ver catalogo completo");
            System.out.println("  2. Registrar nueva obra");
            System.out.println("  3. Asignar obra a sala");
            System.out.println("  4. Reportar danio en obra");
            System.out.println("  5. Dar baja obra");
            System.out.println("  0. Cerrar sesion");
            System.out.print("\n  Opcion: ");
            String opcion = sc.nextLine().trim();

            switch (opcion) {
                case "1" -> { separador("CATALOGO COMPLETO"); System.out.println(catalogo); }
                case "2" -> registrarObra(agente);
                case "3" -> {
                    separador("ASIGNAR OBRA A SALA");
                    Obra obra = seleccionarObra("asignar");
                    if (obra == null) break;
                    separador("SALAS DISPONIBLES");
                    Sala sala = seleccionarSala("asignar");
                    if (sala == null) break;
                    try {
                        agente.asignarSala(obra, sala);
                        System.out.println("  '" + obra.getTitulo() + "' asignada a '" + sala.getNombre() + "'.");
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "4" -> {
                    separador("REPORTAR DANIO");
                    Obra obra = seleccionarObra("reportar");
                    if (obra == null) break;
                    System.out.print("  Descripcion del danio: ");
                    String desc = sc.nextLine().trim();
                    if (desc.isEmpty()) { System.out.println("  La descripcion no puede estar vacia."); break; }
                    try {
                        agente.reportarDanio(obra, desc);
                        System.out.println("  Danio registrado. Estado: " + obra.getEstado().getValor());
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "5" -> {
                    separador("DAR BAJA OBRA");
                    Obra obra = seleccionarObra("dar de baja");
                    if (obra == null) break;
                    try {
                        agente.darBajaObra(catalogo, obra);
                        if (obra.getSala() != null) obra.getSala().eliminarObra(obra);
                        System.out.println("  '" + obra.getTitulo() + "' eliminada del catalogo.");
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "0" -> { agente.cerrarSesion(); System.out.println("  Sesion cerrada."); return; }
                default  -> System.out.println("  Opcion invalida.");
            }
        }
    }

    private static void registrarObra(AgenteCatalogo agente) {
        separador("REGISTRAR NUEVA OBRA");
        System.out.println("  [1] Cuadro");
        System.out.println("  [2] Escultura");
        System.out.println("  [3] Otra");
        System.out.print("\n  Tipo: ");
        String tipoOp = sc.nextLine().trim();
        if (!tipoOp.equals("1") && !tipoOp.equals("2") && !tipoOp.equals("3")) {
            System.out.println("  Tipo invalido."); return;
        }
        System.out.print("  Titulo       : "); String titulo = sc.nextLine().trim();
        System.out.print("  Autor        : "); String autor  = sc.nextLine().trim();
        if (titulo.isEmpty() || autor.isEmpty()) { System.out.println("  Titulo y autor son obligatorios."); return; }

        Periodo[] periodos = Periodo.values();
        System.out.println("\n  Periodo historico:");
        for (int i = 0; i < periodos.length; i++)
            System.out.printf("  [%d] %s%n", i + 1, periodos[i].getValor());
        Periodo periodo;
        try {
            System.out.print("  Periodo: ");
            int idx = Integer.parseInt(sc.nextLine().trim());
            if (idx < 1 || idx > periodos.length) { System.out.println("  Opcion fuera de rango."); return; }
            periodo = periodos[idx - 1];
        } catch (IllegalArgumentException e) { System.out.println("  Entrada invalida."); return; }

        LocalDate fechaCreacion = pedirFecha("Fecha de creacion");
        if (fechaCreacion == null) return;
        LocalDate fechaEntrada = pedirFecha("Fecha entrada al museo");
        if (fechaEntrada == null) return;

        try {
            Obra obra;
            if (tipoOp.equals("1")) {
                EstiloCuadro[] estilos = EstiloCuadro.values();
                System.out.println("\n  Estilo artistico:");
                for (int i = 0; i < estilos.length; i++)
                    System.out.printf("  [%d] %s%n", i + 1, estilos[i].getValor());
                System.out.print("  Estilo: ");
                int ei = Integer.parseInt(sc.nextLine().trim());
                if (ei < 1 || ei > estilos.length) { System.out.println("  Opcion fuera de rango."); return; }

                TecnicaCuadro[] tecnicas = TecnicaCuadro.values();
                System.out.println("\n  Tecnica:");
                for (int i = 0; i < tecnicas.length; i++)
                    System.out.printf("  [%d] %s%n", i + 1, tecnicas[i].getValor());
                System.out.print("  Tecnica: ");
                int ti = Integer.parseInt(sc.nextLine().trim());
                if (ti < 1 || ti > tecnicas.length) { System.out.println("  Opcion fuera de rango."); return; }
                obra = new Cuadro(titulo, autor, periodo, fechaCreacion, fechaEntrada,
                                  estilos[ei - 1], tecnicas[ti - 1]);
            } else if (tipoOp.equals("2")) {
                MaterialEscultura[] materiales = MaterialEscultura.values();
                System.out.println("\n  Material:");
                for (int i = 0; i < materiales.length; i++)
                    System.out.printf("  [%d] %s%n", i + 1, materiales[i].getValor());
                System.out.print("  Material: ");
                int mi = Integer.parseInt(sc.nextLine().trim());
                if (mi < 1 || mi > materiales.length) { System.out.println("  Opcion fuera de rango."); return; }
                obra = new Escultura(titulo, autor, periodo, fechaCreacion, fechaEntrada,
                                     materiales[mi - 1]);
            } else {
                System.out.print("  Descripcion del tipo: "); String desc = sc.nextLine().trim();
                obra = new Otra(titulo, autor, periodo, fechaCreacion, fechaEntrada, desc);
            }

            agente.registrarObra(catalogo, obra);
            try {
                System.out.print("  Valoracion (EUR): ");
                double valor = Double.parseDouble(sc.nextLine().trim());
                obra.setValoracion(valor);
            } catch (IllegalArgumentException e) {
                System.out.println("  Advertencia al valorar: " + e.getMessage());
            }
            System.out.println("\n  Obra registrada:\n  " + obra);
        } catch (Exception e) {
            System.out.println("  Error: " + e.getMessage());
        }
    }

    // --- Menu Agente Restaurador -------------------------------------------

    @SuppressWarnings("unchecked")
    private static void menuAgenteRestaurador(AgenteRestaurador restaurador) {
        while (true) {
            separador("MENU RESTAURADOR — " + restaurador.getNombreUsuario());
            System.out.println("  1. Ver obras pendientes de restauracion");
            System.out.println("  2. Iniciar restauracion");
            System.out.println("  3. Finalizar restauracion");
            System.out.println("  4. Ver historial de restauraciones de una obra");
            System.out.println("  0. Cerrar sesion");
            System.out.print("\n  Opcion: ");
            String opcion = sc.nextLine().trim();

            switch (opcion) {
                case "1" -> {
                    separador("OBRAS QUE NECESITAN RESTAURACION");
                    List<Obra> pendientes = restaurador.verificarObrasPendientes(catalogo.getObras());
                    if (pendientes.isEmpty()) System.out.println("  No hay obras pendientes de restauracion.");
                    else for (Obra o : pendientes)
                        System.out.printf("  - '%s'  (%s)  |  %s%n",
                            o.getTitulo(), o.getAutor(), o.getEstado().getValor());
                }
                case "2" -> {
                    separador("INICIAR RESTAURACION");
                    Obra obra = seleccionarObra("restaurar");
                    if (obra == null) break;
                    try {
                        restaurador.iniciarRestauracion(obra);
                        System.out.println("  Restauracion iniciada. Estado: " + obra.getEstado().getValor());
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "3" -> {
                    separador("FINALIZAR RESTAURACION");
                    List<Obra> enRest = catalogo.buscarPorEstado(EstadoObra.EN_RESTAURACION);
                    if (enRest.isEmpty()) { System.out.println("  No hay obras en restauracion activa."); break; }
                    for (int i = 0; i < enRest.size(); i++)
                        System.out.printf("  [%d] '%s'  (%s)%n", i + 1,
                            enRest.get(i).getTitulo(), enRest.get(i).getAutor());
                    try {
                        System.out.print("\n  Numero de obra (0 para cancelar): ");
                        int idx = Integer.parseInt(sc.nextLine().trim());
                        if (idx == 0) break;
                        if (idx < 1 || idx > enRest.size()) { System.out.println("  Numero fuera de rango."); break; }
                        restaurador.finalizarRestauracion(enRest.get(idx - 1));
                        System.out.println("  Restauracion finalizada. Estado: " + enRest.get(idx - 1).getEstado().getValor());
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "4" -> {
                    separador("HISTORIAL DE RESTAURACIONES");
                    Obra obra = seleccionarObra("consultar");
                    if (obra == null) break;
                    try {
                        List<Object> historial = restaurador.consultarRestauraciones(obra);
                        if (historial.isEmpty()) {
                            System.out.println("  '" + obra.getTitulo() + "' no tiene restauraciones registradas.");
                        } else {
                            System.out.println("\n  Restauraciones de '" + obra.getTitulo() + "':");
                            for (Object r : historial) {
                                Map<String, Object> map = (Map<String, Object>) r;
                                Object fin = map.get("fechaFin");
                                System.out.println("    Inicio: " + map.get("fechaInicio") +
                                                   "  —  Fin: " + (fin != null ? fin : "en curso"));
                            }
                        }
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "0" -> { restaurador.cerrarSesion(); System.out.println("  Sesion cerrada."); return; }
                default  -> System.out.println("  Opcion invalida.");
            }
        }
    }

    // --- Menu Director del Museo -------------------------------------------

    private static void menuDirector(DirectorMuseo director) {
        while (true) {
            separador("MENU DIRECTOR — " + director.getNombreUsuario());
            System.out.println("  1. Ver salas del museo");
            System.out.println("  2. Agregar sala");
            System.out.println("  3. Eliminar sala");
            System.out.println("  4. Ver museos colaboradores");
            System.out.println("  5. Agregar museo colaborador");
            System.out.println("  6. Ceder obra a museo colaborador");
            System.out.println("  7. Consultar valoracion total del catalogo");
            System.out.println("  0. Cerrar sesion");
            System.out.print("\n  Opcion: ");
            String opcion = sc.nextLine().trim();

            switch (opcion) {
                case "1" -> {
                    separador("SALAS DEL MUSEO");
                    if (director.getSalas().isEmpty()) System.out.println("  No hay salas registradas.");
                    else for (Sala s : director.getSalas()) System.out.println("\n" + s);
                }
                case "2" -> {
                    separador("AGREGAR SALA");
                    System.out.print("  Nombre de la nueva sala: ");
                    String nombre = sc.nextLine().trim();
                    if (nombre.isEmpty()) { System.out.println("  El nombre no puede estar vacio."); break; }
                    try {
                        Sala nueva = new Sala(nombre);
                        director.agregarSala(nueva);
                        salas.add(nueva);
                        System.out.println("  Sala '" + nombre + "' agregada.");
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "3" -> {
                    separador("ELIMINAR SALA");
                    List<Sala> salasDir = director.getSalas();
                    if (salasDir.isEmpty()) { System.out.println("  No hay salas registradas."); break; }
                    for (int i = 0; i < salasDir.size(); i++)
                        System.out.printf("  [%d] %s%n", i + 1, salasDir.get(i).getNombre());
                    try {
                        System.out.print("\n  Numero de sala a eliminar (0 para cancelar): ");
                        int idx = Integer.parseInt(sc.nextLine().trim());
                        if (idx == 0) break;
                        if (idx < 1 || idx > salasDir.size()) { System.out.println("  Numero fuera de rango."); break; }
                        Sala sala = salasDir.get(idx - 1);
                        director.eliminarSala(sala);
                        salas.remove(sala);
                        System.out.println("  Sala '" + sala.getNombre() + "' eliminada.");
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "4" -> {
                    separador("MUSEOS COLABORADORES");
                    List<MuseoColaborador> museos = director.getMuseosColaboradores();
                    if (museos.isEmpty()) System.out.println("  No hay museos colaboradores registrados.");
                    else for (MuseoColaborador m : museos) System.out.println("  - " + m);
                }
                case "5" -> {
                    separador("AGREGAR MUSEO COLABORADOR");
                    System.out.print("  Nombre del museo: "); String nombre = sc.nextLine().trim();
                    System.out.print("  Pais            : "); String pais   = sc.nextLine().trim();
                    if (nombre.isEmpty() || pais.isEmpty()) { System.out.println("  Nombre y pais son obligatorios."); break; }
                    try {
                        director.agregarMuseoColaborador(new MuseoColaborador(nombre, pais));
                        System.out.println("  Museo '" + nombre + "' agregado como colaborador.");
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "6" -> {
                    separador("CEDER OBRA A MUSEO COLABORADOR");
                    List<MuseoColaborador> museos = director.getMuseosColaboradores();
                    if (museos.isEmpty()) { System.out.println("  No hay museos colaboradores registrados."); break; }
                    Obra obra = seleccionarObra("ceder");
                    if (obra == null) break;
                    System.out.println("\n  Museo colaborador:");
                    for (int i = 0; i < museos.size(); i++)
                        System.out.printf("  [%d] %s%n", i + 1, museos.get(i));
                    try {
                        System.out.print("\n  Numero de museo (0 para cancelar): ");
                        int idx = Integer.parseInt(sc.nextLine().trim());
                        if (idx == 0) break;
                        if (idx < 1 || idx > museos.size()) { System.out.println("  Numero fuera de rango."); break; }
                        System.out.print("  Importe de la cesion (EUR): ");
                        double importe = Double.parseDouble(sc.nextLine().trim());
                        LocalDate inicio = pedirFecha("Fecha inicio de cesion");
                        if (inicio == null) break;
                        System.out.print("  Fecha fin (YYYY-MM-DD, vacio = indefinida): ");
                        String rawFin = sc.nextLine().trim();
                        LocalDate fin = rawFin.isEmpty() ? null : LocalDate.parse(rawFin);
                        director.cederObra(obra, museos.get(idx - 1), importe, inicio, fin);
                        System.out.println("  '" + obra.getTitulo() + "' cedida. Estado: " + obra.getEstado().getValor());
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "7" -> {
                    separador("VALORACION TOTAL DEL CATALOGO");
                    try {
                        double total = director.consultarValoracionTotal(catalogo);
                        System.out.printf("  Valoracion total: %,.2f EUR%n", total);
                    } catch (Exception e) { System.out.println("  Error: " + e.getMessage()); }
                }
                case "0" -> { director.cerrarSesion(); System.out.println("  Sesion cerrada."); return; }
                default  -> System.out.println("  Opcion invalida.");
            }
        }
    }
}
