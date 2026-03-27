[Televentas.pdf](https://github.com/user-attachments/files/26291233/Televentas.pdf)

La empresa TeleVentas desea desarrollar un sistema web para el soporte de compras a 
distancia, de los productos que la empresa ofrece, por parte de sus clientes. Se prevé que 
con este sistema, los clientes podrán, fundamentalmente: realizar consultas del catálogo de 
los productos que se ofrecen, para obtener información acerca de un producto particular 
(código, descripción, precio, cantidad disponible, etc.); solicitar le envíen periódicamente y 
por correo electrónico dicho catálogo de productos; ingresar una orden de compra, para que 
se le envíe un conjunto de productos, ajustándose a un tipo de pago para la misma 
(actualmente sólo tarjeta de crédito); presentar una queja (por demoras en la entrega de los 
productos, por ejemplo); y cancelar una orden.
Adicionalmente, se pretende que los agentes del depósito de la empresa utilicen el nuevo 
sistema, consultando las órdenes de compra confirmadas, para armar y empaquetar los 
productos pedidos en dichas órdenes de compra. Asimismo, se debe proveer soporte a estos 
agentes para determinar la logística para la entrega de cada pedido armado, seleccionando 
una empresa de transporte apropiada, y delegando a ésta la entrega del pedido 
correspondiente. Por otra parte, es destacable que la empresa ya posee un sistema de 
inventario para el control de stock de productos. El nuevo sistema deberá interactuar con éste 
para, por ejemplo: consultar descripción y precio de productos al tomar órdenes de compra, 
o bien para actualizar la disponibilidad de productos al armar pedidos. Por otra parte, las 
quejas recibidas por parte de los clientes son remitidas inmediatamente al gerente de 
relaciones de la empresa.

ANALISIS

Se pide crear un sistema de soporte web de compras remotas

- Usuarios (deben validarse para entrar al sistema):

    * CLIENTE: quien puede crear y cancelar órdenes de compra, consultar, suscribirse al catalogo 
    y presentar quejas.

    * AGENTE DE BODEGA: quien recibe las ordenes de compra para armar los pedidos y asignar una 
    transportadora que se encargue del envio.

    * GERENTE DE RELACIONES: quien es el encargado de recibir y dar manejo a las quejas de los clientes.

- CATALOGO: es la clase que recoge los productos que se ofrecen y que van a formar los detalles del 
pedido en la orden de compra que hace el cliente.

- PRODUCTO: contiene la informacion de los productos que conforman el catálogo, tienen un codigo, precio y
cantidad disponible.

- ORDEN DE COMPRA: es la clase que representa la solicitud de compra realizada por un cliente, contiene 
un conjunto de detalles de orden, un tipo de pago asociado y puede encontrarse en distintos estados
(pendiente, confirmada o cancelada).

- DETALLE PEDIDO: representa cada línea dentro de una orden de compra, asociando un producto específico
con la cantidad solicitada por el cliente.

- QUEJA: es la clase que registra el reclamo presentado por un cliente (por ejemplo, demoras en la entrega),
contiene una descripción del motivo y es remitida al Gerente de Relaciones para su atención.

- PEDIDO: es la clase que representa el paquete armado por el Agente de Bodega a partir de una orden de compra
confirmada, contiene los productos empaquetados y tiene asignada una empresa de transporte para su entrega.

- EMPRESA DE TRANSPORTE: representa a las empresas externas disponibles para realizar la entrega de un pedido,
el Agente de Bodega selecciona la más apropiada y le delega el envío correspondiente.

- SISTEMA DE INVENTARIO: representa el sistema externo que ya posee la empresa para el control de stock, el nuevo
sistema interactúa con él para consultar descripción y precio de productos, y para actualizar la disponibilidad
al armar pedidos.

- TARJETA DE CREDITO: es el medio de pago actualmente soportado por el sistema, se asocia a una orden de 
compra y contiene la información necesaria para procesar el pago del cliente.




[Museo UML.pdf](https://github.com/user-attachments/files/26291234/Museo.UML.pdf)

Un museo desea que su Departamento de Informática desarrolle un software para 
automatizar la gestión de sus obras. Sus requisitos son los siguientes:
Se debe mantener el catálogo de obras de arte. La obra de arte característica es el cuadro. 
Pero, además, el museo dispone de esculturas y de otros objetos. Cualquiera de estos tres 
elementos tiene un autor y pertenece a un periodo. Cada obra es valorada económicamente 
y se almacena su fecha de creación y su fecha de entrada en el museo. Los cuadros y 
esculturas tienen un estilo. De los cuadros hay que recoger la técnica y de las esculturas el 
material. La introducción de datos la realiza el encargado del catálogo. Se debe gestionar la 
restauración de obras de arte. Una obra pueda estar expuesta o puede estar en restauración. 
En este último caso hay que recoger el tipo de restauración y la fecha de inicio de la misma. 
En el caso normal, las obras de arte se restauran automáticamente cada cinco años, por lo 
que se requiere un proceso diario que indique qué obras tienen que pasar a restauración. Por 
otro lado, si una obra resulta dañada por alguna causa, se enviará a restauración
inmediatamente. Cuando se termina una restauración, se almacena la fecha de finalización
de esta. De realizar estas operaciones se encarga el restaurador jefe. El restaurador jefe debe
poder consultar todas las restauraciones que se le han
realizado a cada obra de arte, ordenadas por antigüedad.
Las obras de arte se pueden ceder a otros museos. Se desea gestionar un listado de museos
con los que se puede colaborar. Cuando una obra está cedida y es solicitada por otro museo,
será cedida a este último cuando finalice la cesión al primer museo. Cuando una obra de arte
se cede a un museo es preciso recoger el importe pagado por esta cesión y el periodo de
tiempo en que estará cedida. De esta gestión se encarga el director del museo.
El director del museo debe poder consultar la valoración de todas las obras del museo (la
suma total).
El sistema debe disponer de controles de seguridad, por lo que es requisito indispensable que
todos los usuarios se autentifiquen antes de poder utilizar el software. Los visitantes al museo
pueden consultar los listados de obras por salas en un monitor suspendido en el vestíbulo
principal del museo.
El director del museo debe poder consultar la valoración de todas las obras del museo (la
suma total).

ANALISIS

Se pide crear un sistema para la gestión de obras de arte de un museo

- Usuarios (deben validarse para entrar al sistema):

    * VISITANTE: quien puede consultar las obras disponibles organizadas por sala.

    * AGENTE CATALOGO: quien se encarga de registrar y dar de baja obras, asignarlas a una sala,
    valorarlas economicamente y reportar daños sobre ellas.

    * JEFE RESTAURADOR: quien gestiona el proceso de restauracion de las obras, iniciando y
    finalizando restauraciones, consultando el historial y verificando las obras pendientes de restauracion.

    * DIRECTOR MUSEO: quien administra las salas del museo, gestiona los museos colaboradores,
    cede obras a otros museos y cobra los importes correspondientes por dichas cesiones.

- CATALOGO: es la clase que agrupa todas las obras de arte del museo, permite agregar, eliminar y
buscar obras dentro de la coleccion.

- SALA: representa un espacio fisico dentro del museo donde se exponen las obras, permite agregar
y eliminar obras de su coleccion.

- MUSEO COLAB: representa un museo colaborador externo al que el Director puede ceder obras
temporalmente, tiene un nombre y un pais de origen.

- OBRA: clase abstracta que representa cualquier pieza de arte del museo, contiene informacion comun
como titulo, autor, periodo, fecha de creacion, fecha de entrada al museo, valor economico, estado
(expuesta o en restauracion), sala asignada, historial de restauraciones, reporte de daños y cesiones.

    * CUADRO: especialización de Obra que representa una pintura, agrega el estilo pictórico y la
    tecnica utilizada en su elaboracion.

    * ESCULTURA: especialización de Obra que representa una escultura, agrega el material con el
    que fue elaborada.

    * OTRA: especialización de Obra para objetos de arte que no son cuadros ni esculturas, incluye
    una descripcion libre del tipo de pieza.