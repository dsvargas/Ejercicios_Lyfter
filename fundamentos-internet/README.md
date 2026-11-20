#
 Fundamentos de Internet 


##
 1. Del Cliente al Servidor
 
El usuario escribe www.youtube.com.
El DNS traduce el nombre a una dirección IP.
El navegador se conecta al servidor usando esa IP.
Se establece una conexión segura mediante HTTPS.
El servidor procesa la solicitud.
Envía la página y los datos del video.
El navegador muestra la página.
El video llega por streaming y se reproduce en pantalla.

##
 2. Frontend y Backend en acción
1.
Frontend (lo que ve el usuario)

Es la parte visual de la aplicación con la que interactúan los pacientes y médicos.

Ejemplos:

Formulario para registrarse o iniciar sesión.
Calendario para seleccionar una fecha.
Lista de médicos disponibles.
Pantalla de confirmación de la cita.
Historial de citas.
Todo lo que se ve en la pantalla corresponde al Frontend

Backend (lo que ocurre detrás de escena, de la pantalla)

Es la parte que procesa la información y administra la lógica del sistema.

Ejemplos:

Validar usuarios.
Guardar citas en la base de datos.
Verificar disponibilidad de horarios.
Enviar correos de confirmación.
Gestionar información de pacientes y médicos.

 Todo el procesamiento y almacenamiento de datos corresponde al Backend.

2.
Frontend
HTML → estructura de las páginas.
CSS → diseño y estilos visuales.
Angular/React →  frameworks, interfaz interactiva y dinámica.
Backend
ASP.NET Core (.NET) → creación de APIs y lógica de negocio.
Node.js con Express → servidor JavaScript.
Python con Django o Flask → desarrollo backend.

3.
primero el usuario realiza una accion, seleccionar una fecha y da click en un boton de **agendar cita**.
entonces el navegador envia una solicitud(request) mediante HTTPS a una API del backend y como es una solicitud de un ingreso nuevo acemos un post **POST /api/citas**
y los datos que vamos a enviar en ese post son el nombre, la fecha y la hora.
el backend procesa la solicitud, hace cosas que se especifiquen en el backend como validar datos, consultar en la base de datos y verificar si esta disponible y guarda la cita en la base de datos.
cuando eso pasa y todo sale bien manda una respuesta al frontend para indicar que se guardo exitosamente y algun ID de la cita si fuera necesario.
En caso de positivo o negativo el navegadorrecibe la respuesta(response) y muestra algun tipo de mensaje. 


##
 3. REST vs SOAP vs GraphQL


| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual |
|------------|------------------------|----------------------|-----------------------------|------------|
| REST | JSON (principalmente), XML | Media | Baja | Alta |
| SOAP | XML | Baja | Alta | Media/Baja |
| GraphQL | JSON | Alta | Media/Alta | Alta |


**
¿Cuál es más apropiada para una startup moderna? ¿Por qué?
**
Creo que REST, implementacion mas rapida, menor complejidad, excelente integracion, buen rendimiento, y muchas apis modernas utilizan rest por lo que es mas facil encontrar recursos de apoyo de ser necesario.


##
 4. Explorando APIs con Postman


###
 4.1 Selección de la API

-
 
**
Nombre de la API: Studio Ghibli API
**

-
 
**
Descripción:
Es una API REST pública y gratuita que recopila y cataloga información detallada sobre las películas, personajes, locaciones, especies y vehículos del universo de Studio Ghibli.
**


###
 4.2 Configuración en Postman

-
 
**
Nombre de la colección: Studio Ghibli API
**

-
 
**
Solicitudes agregadas:
**

  
-
 GET - Obtener detalle de la película (es el único método soportado por el endpoint de películas de esta API pública).
  
-
 POST - No lo permite (la API es de solo lectura y no habilita la creación de nuevos recursos).
  
-
 PUT/PATCH/DELETE - No lo permite (la API no expone operaciones de actualización ni eliminación sobre sus registros).

###
 4.3 Ejecución y análisis


|
 Solicitud 
|
 Método 
|
 Endpoint 
|
 Código de estado 
|
 Notas 
|

|
-----------
|
--------
|
----------
|
-------------------
|
-------
|
obtener pelicula por ID
|
           GET 
|
        [https://ghibliapi.vercel.app/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49](https://ghibliapi.vercel.app/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49)
|
         200 OK 
|
              Devuelve el JSON de My Neighbor Totoro con Content-Type: application/json; charset=utf-8.     
|
       
|


###
 4.4 Explicación técnica


####
 [Nombre de la solicitud]

-
 
**
Método HTTP: GET
**

-
 
**
Endpoint: [https://ghibliapi.vercel.app/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49](https://ghibliapi.vercel.app/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49)
**

-
 
**
Parámetros / body: Ninguno (se pasa el UUID directamente en la ruta del endpoint y no requiere body).
**

-
 
**
Descripción de la respuesta: Descripción de la respuesta: Retorna un objeto JSON con los metadatos de la película solicitada (id, title, original_title, description, director, producer, release_date, running_time, rt_score y arreglos de relaciones como people, species, locations y vehicles).
**


**
¿Qué aprendiste del proceso?
**
Aprendí a verificar qué métodos HTTP soporta realmente una API antes de asumir que todos los verbos (GET, POST, PUT, PATCH, DELETE) estarán disponibles. También entendí que las APIs públicas gratuitas suelen restringirse a modo lectura (read-only) para proteger la integridad de los datos compartidos, y que interpretar códigos de estado y headers (Content-Type) es clave para diagnosticar cómo responde un servidor.


###
 4.5 Reflexión final
 A lo largo de este ejercicio comprendí que una API funciona como un puente estandarizado mediante peticiones HTTP donde el cliente solicita o intenta operar sobre recursos y el servidor responde con un código de estado, cabeceras y un cuerpo de datos (habitualmente en JSON). la api de Studio Ghibli API solo responde con éxito a GET y rechaza escrituras o eliminaciones deja en claro que los permisos y rutas disponibles dependen directamente de cómo el servidor haya sido diseñado y protegido.

Postman hizo que esa comunicación cliente-servidor fuera mucho más tangible que solo leer teoría, porque permite armar la petición, cambiar el verbo HTTP o el endpoint y observar de inmediato qué devuelve el servidor. Ver en pantalla el 200 OK con el JSON estructurado frente a una respuesta de rechazo ayuda a conectar la teoría de HTTP con lo que ocurre realmente detrás de cualquier aplicación web o móvil.
como dato estra que no tieene que ver con la api pero investigue a veces cuando se trata de resolver algun error el saber el significado de la respuesta como el 200 o el 404 me dicen por donde esta el camino.