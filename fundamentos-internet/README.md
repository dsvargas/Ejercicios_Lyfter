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
Nombre de la colección:
**

-
 
**
Solicitudes agregadas:
**

  
-
 GET -
  
-
 POST -
  
-
 PUT/PATCH/DELETE -

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

|
           
|
        
|
          
|
                   
|
       
|


###
 4.4 Explicación técnica


####
 [Nombre de la solicitud]

-
 
**
Método HTTP:
**

-
 
**
Endpoint:
**

-
 
**
Parámetros / body:
**

-
 
**
Descripción de la respuesta:
**


**
¿Qué aprendiste del proceso?
**


###
 4.5 Reflexión final