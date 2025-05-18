# Bienvenidos a 🕹️HogarBot🕹️
---

### 🕹️Descripción General
**HogarBot** es una aplicacion construida por SmartHome Solutions la misma es un sistema de gestión de dispositivos inteligentes para el hogar, desarrollado como parte de una iniciativa educativa para la Tecnicatura superior en desarrollo de Software del ISPC Instituto Superior Politécnico Córdoba, cuyo objetivo es simular soluciones de domótica accesibles y personalizables.
Este proyecto permite a los usuarios interactuar con diversos dispositivos electronicos como ser cámaras de seguridad y electrodomésticos desde una interfaz centralizada. La solución en esta primera etapa consiste en diversas funcionalidades basicas que permiten manipular los dispositivos y generar una automatización.

### 🕹️Características Principales

**Gestión de dispositivos:** Agregar, eliminar, buscar y modificar dispositivos inteligentes.
**Categorización:** Organización de dispositivos según su tipo (entretenimiento, climatización, iluminación, etc.).
**Control de estados:** Monitoreo y cambio de estado (encendido/apagado) de los dispositivos.
**Modo sueño:** Función de automatización que configura dispositivos para optimizar el descanso nocturno.
**Políticas de privacidad:** Implementación de estándares de seguridad para proteger datos sensibles.

### 🕹️Equipo de desarrollo

Equipo de Desarrollo
El proyecto ha sido desarrollado por:

**👨🏾‍💻Fernando Agustín Moyano:** Responsable del diseño e implementación de la base de datos y desarrollo de funcionalidades como la gestión de dispositivos y el control de estados.
**👨🏾‍💻Santino Primero:** Encargado de la implementación de políticas de privacidad de datos y desarrollo de funcionalidades como el modo sueño y funcionalidades para la gestion de los dispositivos.

### 🕹️Tecnologias usadas

Tecnologías Utilizadas

**Lenguaje de programación:** Python
**Base de datos:** Simulación por medio de las estructuras de datos provistas por Python
**Principios de diseño:**  modularidad y separación de responsabilidades por medio de la implementacion de diversos metodos


# Diseño de Base de Datos - Aplicacion 🕹️HogarBot🕹️ construida por SmartHome Solutions
---

## Entidades Identificadas y sus Atributos

### 1. Entidad: Usuario

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| usuario_id    | INT          | Identificador único del usuario  | PK    |
| nombre        | VARCHAR(50)  | Nombre del usuario               |       |
| apellido      | VARCHAR(50)  | Apellido del usuario             |       |
| email         | VARCHAR(100) | Correo electrónico del usuario   | CK    |
| contraseña    | VARCHAR(255) | Contraseña encriptada del usuario|       |
| rol_id        | INT          | ID del rol asignado al usuario   | FK    |
| fecha_registro| DATETIME     | Fecha de registro del usuario    |       |

**Claves Candidatas:**
- usuario_id (PK)
- email (debe ser único)

### 2. Entidad: Rol

| Atributo      | Tipo de Dato | Descripción                   | Clave |
|---------------|--------------|-------------------------------|-------|
| rol_id        | INT          | Identificador único del rol   | PK    |
| nombre        | VARCHAR(30)  | Nombre del rol                | CK    |
| descripcion   | VARCHAR(255) | Descripción de permisos del rol |     |

**Claves Candidatas:**
- rol_id (PK)
- nombre (debe ser único)

### 3. Entidad: Dispositivo

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| dispositivo_id| INT          | Identificador único del dispositivo | PK  |
| nombre        | VARCHAR(100) | Nombre del dispositivo           |       |
| marca         | VARCHAR(50)  | Marca del dispositivo            |       |
| categoria_id  | INT          | ID de la categoría del dispositivo | FK  |
| estado_id     | INT          | ID del estado del dispositivo    | FK    |
| consumo_id    | INT          | ID del consumo del dispositivo   | FK    |
| alimentacion_id| INT         | ID del tipo de alimentación      | FK    |
| ubicacion_id  | INT          | ID de la ubicación del dispositivo | FK  |

**Claves Candidatas:**
- dispositivo_id (PK)

### 4. Entidad: Categoría

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| categoria_id  | INT          | Identificador único de la categoría | PK  |
| nombre        | VARCHAR(50)  | Nombre de la categoría           | CK    |
| descripcion   | VARCHAR(255) | Descripción de la categoría      |       |

**Claves Candidatas:**
- categoria_id (PK)
- nombre (debe ser único)

### 5. Entidad: Estado

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| estado_id     | INT          | Identificador único del estado   | PK    |
| nombre        | VARCHAR(30)  | Nombre del estado (ej: encendido, apagado) | CK |
| descripcion   | VARCHAR(255) | Descripción del estado           |       |

**Claves Candidatas:**
- estado_id (PK)
- nombre (debe ser único)

### 6. Entidad: Consumo

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| consumo_id    | INT          | Identificador único del consumo  | PK    |
| nombre        | VARCHAR(30)  | Nivel de consumo (bajo, medio, alto) | CK |
| rango         | VARCHAR(50)  | Rango de consumo en valores     |       |
| unidad_medida | VARCHAR(20)  | Unidad de medida del consumo     |       |

**Claves Candidatas:**
- consumo_id (PK)
- nombre (debe ser único)

### 7. Entidad: Alimentación

| Atributo        | Tipo de Dato | Descripción                     | Clave |
|-----------------|--------------|----------------------------------|-------|
| alimentacion_id | INT          | Identificador único de alimentación | PK |
| tipo_conexion   | VARCHAR(50)  | Tipo de conexión (110V, 220V, batería) | CK |
| autonomia       | INT          | Autonomía en horas (para baterías) |     |

**Claves Candidatas:**
- alimentacion_id (PK)

### 8. Entidad: Ubicación

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| ubicacion_id  | INT          | Identificador único de la ubicación | PK |
| nombre        | VARCHAR(50)  | Nombre de la ubicación (ej: sala, cocina) | CK |
| descripcion   | VARCHAR(255) | Descripción adicional de la ubicación |   |

**Claves Candidatas:**
- ubicacion_id (PK)
- nombre (dentro del mismo hogar, debe ser único)

### 9. Entidad: Usuario_Dispositivo (Tabla de relación)

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| ud_id         | INT          | Identificador único de la relación | PK   |
| usuario_id    | INT          | ID del usuario                   | FK    |
| dispositivo_id| INT          | ID del dispositivo               | FK    |
| tipo_permiso  | VARCHAR(30)  | Tipo de permiso (ver, editar, admin) |    |
| fecha_asignacion | DATETIME  | Fecha de asignación del dispositivo |    |

**Claves Candidatas:**
- ud_id (PK)
- (usuario_id, dispositivo_id) (debe ser única la combinación)

## Leyenda:
- **PK**: Primary Key (Clave Primaria)
- **FK**: Foreign Key (Clave Foránea)
- **CK**: Candidate Key (Clave Candidata)

## Diagrama Entidad-Relación

# Bienvenidos a 🕹️HogarBot🕹️
---

### 🕹️Descripción General
**HogarBot** es una aplicacion construida por SmartHome Solutions la misma es un sistema de gestión de dispositivos inteligentes para el hogar, desarrollado como parte de una iniciativa educativa para la Tecnicatura superior en desarrollo de Software del ISPC Instituto Superior Politécnico Córdoba, cuyo objetivo es simular soluciones de domótica accesibles y personalizables.
Este proyecto permite a los usuarios interactuar con diversos dispositivos electronicos como ser cámaras de seguridad y electrodomésticos desde una interfaz centralizada. La solución en esta primera etapa consiste en diversas funcionalidades basicas que permiten manipular los dispositivos y generar una automatización.

### 🕹️Características Principales

**Gestión de dispositivos:** Agregar, eliminar, buscar y modificar dispositivos inteligentes.
**Categorización:** Organización de dispositivos según su tipo (entretenimiento, climatización, iluminación, etc.).
**Control de estados:** Monitoreo y cambio de estado (encendido/apagado) de los dispositivos.
**Modo sueño:** Función de automatización que configura dispositivos para optimizar el descanso nocturno.
**Políticas de privacidad:** Implementación de estándares de seguridad para proteger datos sensibles.

### 🕹️Equipo de desarrollo

Equipo de Desarrollo
El proyecto ha sido desarrollado por:

**👨🏾‍💻Fernando Agustín Moyano:** Responsable del diseño e implementación de la base de datos y desarrollo de funcionalidades como la gestión de dispositivos y el control de estados.
**👨🏾‍💻Santino Primero:** Encargado de la implementación de políticas de privacidad de datos y desarrollo de funcionalidades como el modo sueño y funcionalidades para la gestion de los dispositivos.

### 🕹️Tecnologias usadas

Tecnologías Utilizadas

**Lenguaje de programación:** Python
**Base de datos:** Simulación por medio de las estructuras de datos provistas por Python
**Principios de diseño:**  modularidad y separación de responsabilidades por medio de la implementacion de diversos metodos


# Diseño de Base de Datos - Aplicacion 🕹️HogarBot🕹️ construida por SmartHome Solutions
---

## Entidades Identificadas y sus Atributos

### 1. Entidad: Usuario

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| usuario_id    | INT          | Identificador único del usuario  | PK    |
| nombre        | VARCHAR(50)  | Nombre del usuario               |       |
| apellido      | VARCHAR(50)  | Apellido del usuario             |       |
| email         | VARCHAR(100) | Correo electrónico del usuario   | CK    |
| contraseña    | VARCHAR(255) | Contraseña encriptada del usuario|       |
| rol_id        | INT          | ID del rol asignado al usuario   | FK    |
| fecha_registro| DATETIME     | Fecha de registro del usuario    |       |

**Claves Candidatas:**
- usuario_id (PK)
- email (debe ser único)

### 2. Entidad: Rol

| Atributo      | Tipo de Dato | Descripción                   | Clave |
|---------------|--------------|-------------------------------|-------|
| rol_id        | INT          | Identificador único del rol   | PK    |
| nombre        | VARCHAR(30)  | Nombre del rol                | CK    |
| descripcion   | VARCHAR(255) | Descripción de permisos del rol |     |

**Claves Candidatas:**
- rol_id (PK)
- nombre (debe ser único)

### 3. Entidad: Dispositivo

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| dispositivo_id| INT          | Identificador único del dispositivo | PK  |
| nombre        | VARCHAR(100) | Nombre del dispositivo           |       |
| marca         | VARCHAR(50)  | Marca del dispositivo            |       |
| categoria_id  | INT          | ID de la categoría del dispositivo | FK  |
| estado_id     | INT          | ID del estado del dispositivo    | FK    |
| consumo_id    | INT          | ID del consumo del dispositivo   | FK    |
| alimentacion_id| INT         | ID del tipo de alimentación      | FK    |
| ubicacion_id  | INT          | ID de la ubicación del dispositivo | FK  |

**Claves Candidatas:**
- dispositivo_id (PK)

### 4. Entidad: Categoría

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| categoria_id  | INT          | Identificador único de la categoría | PK  |
| nombre        | VARCHAR(50)  | Nombre de la categoría           | CK    |
| descripcion   | VARCHAR(255) | Descripción de la categoría      |       |

**Claves Candidatas:**
- categoria_id (PK)
- nombre (debe ser único)

### 5. Entidad: Estado

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| estado_id     | INT          | Identificador único del estado   | PK    |
| nombre        | VARCHAR(30)  | Nombre del estado (ej: encendido, apagado) | CK |
| descripcion   | VARCHAR(255) | Descripción del estado           |       |

**Claves Candidatas:**
- estado_id (PK)
- nombre (debe ser único)

### 6. Entidad: Consumo

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| consumo_id    | INT          | Identificador único del consumo  | PK    |
| nombre        | VARCHAR(30)  | Nivel de consumo (bajo, medio, alto) | CK |
| rango         | VARCHAR(50)  | Rango de consumo en valores     |       |
| unidad_medida | VARCHAR(20)  | Unidad de medida del consumo     |       |

**Claves Candidatas:**
- consumo_id (PK)
- nombre (debe ser único)

### 7. Entidad: Alimentación

| Atributo        | Tipo de Dato | Descripción                     | Clave |
|-----------------|--------------|----------------------------------|-------|
| alimentacion_id | INT          | Identificador único de alimentación | PK |
| tipo_conexion   | VARCHAR(50)  | Tipo de conexión (110V, 220V, batería) | CK |
| autonomia       | INT          | Autonomía en horas (para baterías) |     |

**Claves Candidatas:**
- alimentacion_id (PK)

### 8. Entidad: Ubicación

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| ubicacion_id  | INT          | Identificador único de la ubicación | PK |
| nombre        | VARCHAR(50)  | Nombre de la ubicación (ej: sala, cocina) | CK |
| descripcion   | VARCHAR(255) | Descripción adicional de la ubicación |   |

**Claves Candidatas:**
- ubicacion_id (PK)
- nombre (dentro del mismo hogar, debe ser único)

### 9. Entidad: Usuario_Dispositivo (Tabla de relación)

| Atributo      | Tipo de Dato | Descripción                      | Clave |
|---------------|--------------|----------------------------------|-------|
| ud_id         | INT          | Identificador único de la relación | PK   |
| usuario_id    | INT          | ID del usuario                   | FK    |
| dispositivo_id| INT          | ID del dispositivo               | FK    |
| tipo_permiso  | VARCHAR(30)  | Tipo de permiso (ver, editar, admin) |    |
| fecha_asignacion | DATETIME  | Fecha de asignación del dispositivo |    |

**Claves Candidatas:**
- ud_id (PK)
- (usuario_id, dispositivo_id) (debe ser única la combinación)

## Leyenda:
- **PK**: Primary Key (Clave Primaria)
- **FK**: Foreign Key (Clave Foránea)
- **CK**: Candidate Key (Clave Candidata)

## Diagrama Entidad-Relación

https://drive.google.com/file/d/13X4qB3mlL4owHbLlwaCDhUb0C9CRlyHT/view?usp=sharing
