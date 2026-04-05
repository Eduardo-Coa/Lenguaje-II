# Manual de Programación — Lenguaje II

**Autor:** Eduardo Coa  
**Repositorio:** [Eduardo-Coa/Lenguaje-II](https://github.com/Eduardo-Coa/Lenguaje-II)  
**Rama principal de trabajo:** `develop_dcoa37`

---

## Tabla de Contenidos

1. [Descripción General](#1-descripción-general)
2. [Estructura del Proyecto](#2-estructura-del-proyecto)
3. [Estándares y Convenciones](#3-estándares-y-convenciones)
4. [Sistema TeleVentas — Python](#4-sistema-televentas--python)
5. [Sistema Museo — Python](#5-sistema-museo--python)
6. [Sistema TeleVentas — Java](#6-sistema-televentas--java)
7. [Sistema Museo — Java](#7-sistema-museo--java)
8. [Cómo Ejecutar](#8-cómo-ejecutar)
9. [Estructura de Ramas Git](#9-estructura-de-ramas-git)

---

## 1. Descripción General

El proyecto implementa dos sistemas orientados a objetos, cada uno desarrollado primero en **Python** y luego traducido a **Java**:

| Sistema | Descripción |
|---|---|
| **TeleVentas** | Gestión de ventas por televisión: usuarios, productos, órdenes, pagos, pedidos y quejas. |
| **Museo** | Gestión de un museo: obras de arte, salas, restauraciones, cesiones y catálogo. |

Ambos sistemas aplican los principios **SOLID**, herencia, clases abstractas e interfaces.

---

## 2. Estructura del Proyecto

```
Lenguaje II/
├── 1.1TeleVentas_Python/
│   ├── Clases/
│   │   ├── Usuario.py
│   │   ├── Cliente.py
│   │   ├── Producto.py
│   │   ├── Queja.py
│   │   ├── OrdenCompra.py
│   │   ├── Pedido.py
│   │   ├── DetallePedido.py
│   │   ├── Pago.py
│   │   ├── PagoTarjeta.py
│   │   ├── Transportadora.py
│   │   ├── Catalogo.py
│   │   ├── GerenteRelaciones.py
│   │   ├── AgenteBodega.py
│   │   └── Inventario.py
│   ├── Interfaces/
│   │   ├── IInvetario.py
│   │   └── ITransportadora.py
│   └── main.py
│
├── 1.2Museo_Python/
│   └── Clases/
│       ├── Usuario.py
│       ├── Obra.py
│       ├── Cuadro.py
│       ├── Escultura.py
│       ├── Otra.py
│       ├── Sala.py
│       ├── MuseoColaborador.py
│       ├── Catalogo.py
│       ├── Visitante.py
│       ├── AgenteCatalogo.py
│       ├── AgenteRestaurador.py
│       └── DirectorMuseo.py
│
├── 2.1Televentas_Java/
│   ├── ClasesTeleventas/
│   │   └── (mismas clases que Python en Java)
│   ├── Interfaces/
│   │   ├── IInventario.java
│   │   └── ITransportadora.java
│   └── Main.java
│
└── 2.2Museo_Java/
    └── Clases_Museo/
        └── (mismas clases que Python en Java)
```

---

## 3. Estándares y Convenciones

### Python
- **PEP 8:** nombres en `snake_case` para métodos y atributos; `PascalCase` para clases.
- **PEP 257:** docstrings en cada clase y método con formato de una línea o multilínea.
- **Atributos protegidos:** prefijo `_` (ej. `self._nombre`).
- **Propiedades:** `@property` para getters; `@setter` para setters con validación.
- **Clases abstractas:** `ABC` + `@abstractmethod` del módulo `abc`.
- **Enumeraciones:** `Enum` del módulo `enum`.
- **Fechas:** `date` del módulo `datetime`.

### Java
- **Javadoc:** `/** */` en cada clase y método; `@param` y `@return` obligatorios.
- **Convenciones:** `camelCase` para métodos y atributos; `PascalCase` para clases.
- **Encapsulamiento:** atributos `private`; acceso mediante getters/setters públicos.
- **Clases abstractas:** `abstract class`.
- **Interfaces:** `interface` con métodos sin implementación.
- **Enumeraciones:** `enum` definido dentro de la clase que lo usa.
- **Colecciones:** `List<T>` con `ArrayList`; `Map<K,V>` con `HashMap`.
- **Fechas:** `LocalDate` del paquete `java.time`.
- **Validaciones:** `throw new IllegalArgumentException(...)`.
- **Sin herramienta de construcción:** compilación directa con `javac`.

---

## 4. Sistema TeleVentas — Python

### Jerarquía de Clases

```
Usuario (base)
├── Cliente
├── AgenteBodega
└── GerenteRelaciones

Pago (abstracta)
└── PagoTarjeta
```

### Descripción de Clases

| Clase | Responsabilidad |
|---|---|
| `Usuario` | Clase base con autenticación (`autenticar()`, `cerrar_sesion()`). |
| `Cliente` | Crea órdenes, cancela órdenes y presenta quejas. |
| `Producto` | Almacena precio y cantidad disponible con validaciones. |
| `Queja` | Registra quejas con estados: `REGISTRADA`, `EN_REVISION`, `RESUELTA`, `CERRADA`. |
| `OrdenCompra` | Agrupa detalles de pedido; calcula total; puede confirmarse o cancelarse. |
| `Pedido` | Representa el envío físico; estados: `PENDIENTE`, `EMPACADO`, `TRANSPORTE_ASIGNADO`, `EN_DESPACHO`. |
| `DetallePedido` | Captura precio unitario en el momento de la compra y calcula subtotal. |
| `Pago` | Clase abstracta con método `procesar_pago()` que deben implementar las subclases. |
| `PagoTarjeta` | Valida número de tarjeta (solo dígitos) y procesa el pago. |
| `Transportadora` | Recibe pedidos y confirma entregas; maneja estados de envío. |
| `Catalogo` | Almacena productos y permite búsqueda por nombre (insensible a mayúsculas). |
| `GerenteRelaciones` | Recibe quejas desde el cliente y gestiona su resolución. |
| `AgenteBodega` | Consulta órdenes y asigna transportadoras a pedidos. |
| `Inventario` | Registra productos con stock; verifica disponibilidad por cantidad. |

### Interfaces

| Interfaz | Métodos |
|---|---|
| `ITransportadora` | `recibir_pedido()`, `confirmar_entrega()`, `get_estado_envio()` |
| `IInventario` | `consultar_producto()`, `actualizar_stock()`, `verificar_disponibilidad()` |

---

## 5. Sistema Museo — Python

### Jerarquía de Clases

```
Usuario (abstracta)
├── Visitante
├── AgenteCatalogo
├── AgenteRestaurador
└── DirectorMuseo

Obra (abstracta)
├── Cuadro
├── Escultura
└── Otra
```

### Descripción de Clases

| Clase | Responsabilidad |
|---|---|
| `Usuario` | Clase base abstracta con `autenticar()`, `cerrar_sesion()` y `get_rol()` abstracto. |
| `Obra` | Clase base abstracta para obras; incluye enums `Periodo` y `EstadoObra`. |
| `Cuadro` | Obra pictórica con `EstiloCuadro` y `TecnicaCuadro`. |
| `Escultura` | Obra tridimensional con `MaterialEscultura` (mármol, bronce, madera, etc.). |
| `Otra` | Obra que no encaja en las categorías anteriores; tiene descripción libre. |
| `Sala` | Agrupa obras; permite agregar y retirar obras. |
| `MuseoColaborador` | Museo externo con el que se gestionan cesiones de obras. |
| `Catalogo` | Registra obras; permite búsqueda por autor, periodo, estado, sala y tipo. |
| `Visitante` | Puede consultar obras de una sala (ordenadas por título). |
| `AgenteCatalogo` | Registra/elimina obras, asigna salas, valora obras y reporta daños. |
| `AgenteRestaurador` | Inicia/finaliza restauraciones y verifica obras pendientes. |
| `DirectorMuseo` | Gestiona salas, museos colaboradores, cesiones y consulta valoración total. |

### Enumeraciones

| Enum | Valores |
|---|---|
| `Periodo` | `RENACIMIENTO`, `BARROCO`, `ROCOCO`, `NEOCLASICISMO`, `ROMANTICISMO`, `REALISMO`, `IMPRESIONISMO`, `MODERNO_CONTEMPORANEO` |
| `EstadoObra` | `EXPUESTA`, `DANADA`, `EN_RESTAURACION`, `CEDIDA` |
| `EstiloCuadro` | `RENACIMIENTO`, `BARROCO`, `ROCOCO`, `NEOCLASICISMO`, `ROMANTICISMO`, `REALISMO`, `IMPRESIONISMO`, `POSTIMPRESIONISMO`, `EXPRESIONISMO`, `CUBISMO`, `SURREALISMO`, `POP_ART` |
| `TecnicaCuadro` | `FRESCO`, `TEMPERA`, `OLEO`, `ACUARELA`, `ACRILICO` |
| `MaterialEscultura` | `MARMOL`, `GRANITO`, `BRONCE`, `ORO`, `CONCRETO`, `MADERA` |

---

## 6. Sistema TeleVentas — Java

Traducción directa del sistema Python. Paquete: `ClasesTeleventas`.

### Diferencias respecto a Python

| Python | Java |
|---|---|
| `ABC` + `@abstractmethod` | `abstract class` |
| `@property` / `@setter` | `getX()` / `setX()` |
| `list` | `List<T>` con `ArrayList` |
| `dict` | `Map<K,V>` con `HashMap` |
| `raise ValueError` | `throw new IllegalArgumentException` |
| `date.today()` | `LocalDate.now()` |
| `__str__` | `toString()` con `@Override` |
| Constantes de clase `str` | `public static final String` |

### Interfaces Java

```java
// package Interfaces;
interface ITransportadora {
    void recibirPedido(Pedido pedido);
    void confirmarEntrega();
    String getEstadoEnvio();
}

interface IInventario {
    Map<String, Object> consultarProducto(int idProducto);
    void actualizarStock(int idProducto, int cantidad);
    boolean verificarDisponibilidad(int idProducto, int cantidad);
}
```

### Compilación y ejecución

```bash
# Desde 2.1Televentas_Java/
javac ClasesTeleventas/*.java Interfaces/*.java Main.java
java Main
```

---

## 7. Sistema Museo — Java

Traducción directa del sistema Python. Paquete: `Clases_Museo`.

### Notas de implementación

- Los enums (`Periodo`, `EstadoObra`, `EstiloCuadro`, etc.) se definen **dentro** de la clase que los usa.
- `AgenteRestaurador` accede directamente a `obra.restauraciones` y `obra.estado` porque están en el mismo paquete (`protected`).
- `AgenteCatalogo.reportarDanio()` almacena el reporte como `Map<String, Object>` en `obra.reportesDanos`.
- `DirectorMuseo.cederObra()` recibe `LocalDate inicio` y `LocalDate fin` como parámetros separados (en Python era una tupla).

### Compilación y ejecución

```bash
# Desde 2.2Museo_Java/
javac Clases_Museo/*.java
```

---

## 8. Cómo Ejecutar

### Python — TeleVentas

```bash
# Desde la raíz del proyecto
cd 1.1TeleVentas_Python
python main.py
```

### Python — Museo (por clase)

```bash
cd 1.2Museo_Python
python -m Clases.Cuadro
python -m Clases.DirectorMuseo
# (cada archivo tiene un bloque if __name__ == "__main__")
```

### Java — TeleVentas

```bash
cd 2.1Televentas_Java
javac ClasesTeleventas/*.java Interfaces/*.java Main.java
java Main
```

### Java — Museo

```bash
cd 2.2Museo_Java
javac Clases_Museo/*.java
```

**Requisitos:**
- Python 3.10 o superior
- Java 17 o superior (por uso de `List.of()`, `LocalDate`, etc.)

---

## 9. Estructura de Ramas Git

```
main
└── develop
      └── develop_dcoa37   ← rama de trabajo principal
```

| Rama | Descripción |
|---|---|
| `main` | Rama de producción estable. |
| `develop` | Rama de integración. Recibe merges desde ramas de trabajo. |
| `develop_dcoa37` | Rama personal de desarrollo (Eduardo Coa). Todo el trabajo se realiza aquí. |

### Flujo de trabajo

1. Trabajar en `develop_dcoa37`
2. Hacer commit con mensaje que lista solo los nombres de las clases trabajadas
3. Push a `origin develop_dcoa37`
4. Cuando el trabajo está completo, merge hacia `develop`

### Convención de commits

```
# Formato
NombreClase1, NombreClase2, NombreClase3

# Ejemplos
Usuario, Cliente, Producto, Queja
OrdenCompra, Pedido, DetallePedido, Pago, PagoTarjeta
```
