##  Sistema TeleVentas



![Diagrama de Clases UML](Televentas.jpeg)

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


##  Sistema Museo

![Diagrama de Clases UML](MuseoUML.jpeg)


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
