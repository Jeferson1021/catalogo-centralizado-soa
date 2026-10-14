# Catálogo centralizado SOA

## 1. Descripción del proyecto

Este proyecto implementa una API REST con Python y Flask para consultar y registrar metadatos de servicios. Su propósito es centralizar información como el identificador, nombre, versión, protocolo, método HTTP, ruta, propietario y estado de cada servicio.

Es una implementación académica de los conceptos de Arquitectura Orientada a Servicios (SOA).

## 2. Tecnologías utilizadas

- Python 3
- Flask
- API REST mediante HTTP
- JSON para el intercambio de información
- Archivo `servicios.json` para persistir el catálogo

## 3. Estructura del proyecto

```text
catalogo-centralizado-soa-main/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── servicios.json
└── evidencias/
```

La carpeta `.venv/` contiene el entorno virtual local y no debe publicarse en GitHub.

## 4. Instalación y ejecución en Windows

Abre PowerShell en la carpeta del proyecto.

Crea un entorno virtual si todavía no existe:

```powershell
py -m venv .venv
```

Activa el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
py -m pip install -r requirements.txt
```

Inicia el servicio:

```powershell
py app.py
```

Si la aplicación inicia correctamente, estará disponible en:

`http://127.0.0.1:5000`

Mantén abierta esa terminal mientras realizas las pruebas.

## 5. Endpoints disponibles

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Información general del proyecto |
| GET | `/health` | Verificación de disponibilidad |
| GET | `/api/v1/inventario/producto` | Consulta de un producto de prueba |
| GET | `/api/v1/servicios` | Consulta todos los servicios registrados |
| GET | `/api/v1/servicios/<service_id>` | Consulta un servicio por identificador |
| POST | `/api/v1/servicios` | Registra un servicio nuevo |

## 6. Pruebas de la API

Con Flask en ejecución, abre en el navegador:

- `http://127.0.0.1:5000/health`
- `http://127.0.0.1:5000/api/v1/inventario/producto`
- `http://127.0.0.1:5000/api/v1/servicios`
- `http://127.0.0.1:5000/api/v1/servicios/SRV-001`

Para registrar un nuevo servicio desde PowerShell, ejecuta:

```powershell
$body = @{
    id = "SRV-005"
    name = "PruebaCatalogo"
    description = "Servicio de prueba del catalogo centralizado."
    version = "1.0.0"
    protocol = "REST"
    method = "GET"
    path = "/api/v1/prueba-catalogo"
    owner = "Equipo SOA"
    status = "activo"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/api/v1/servicios" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body
```

El ejemplo utiliza `SRV-005` para evitar duplicar los identificadores ya registrados. La ruta `/api/v1/prueba-catalogo` es un metadato de ejemplo: registrarla en el catálogo no crea automáticamente un endpoint funcional.

## 7. Persistencia de datos

Los registros del catálogo se almacenan en `servicios.json`. Los servicios pueden consultarse mediante la API y los registros nuevos se guardan en ese archivo.

Para verificar la persistencia, registra un servicio, reinicia la aplicación y vuelve a consultar:

`http://127.0.0.1:5000/api/v1/servicios`

El registro debe continuar presente después del reinicio.

## 8. Relación con la arquitectura SOA

- **Consumidor:** navegador u otra aplicación que invoca la API.
- **Proveedor:** aplicación Flask que procesa las solicitudes HTTP.
- **Contrato del servicio:** endpoints, métodos HTTP, estructura JSON y códigos de respuesta.
- **Catálogo centralizado:** repositorio de metadatos consultable mediante `/api/v1/servicios`.
- **Gobernanza:** identificación, versión, propietario y estado de los servicios.

## 9. Evidencias de funcionamiento

Guarda en `evidencias/` capturas reales que demuestren:

1. La aplicación iniciada correctamente.
2. La consulta de disponibilidad mediante `/health`.
3. El listado de servicios.
4. La consulta de un servicio por identificador.
5. El registro de un servicio nuevo con respuesta HTTP 201.
6. La persistencia del registro después de reiniciar la aplicación.
7. El repositorio público de GitHub con los archivos del proyecto.

No incluyas contraseñas, tokens ni información personal real.

## 10. Publicación en GitHub

Repositorio previsto:

`https://github.com/Jeferson1021/catalogo-centralizado-soa`

Antes de entregar, verifica que el repositorio exista, sea público y contenga como mínimo `app.py`, `requirements.txt`, `servicios.json`, `README.md`, `.gitignore` y las evidencias disponibles.

No publiques la carpeta `.venv/`.

## 11. Limitaciones y mejoras futuras

Esta implementación es una demostración académica. Para un entorno productivo convendría incorporar una base de datos, autenticación y autorización, validaciones adicionales, pruebas automatizadas, control de concurrencia y despliegue seguro.
