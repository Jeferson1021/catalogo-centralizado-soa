# Catálogo centralizado de servicios SOA

Proyecto académico que implementa un servicio REST para consultar y registrar metadatos de servicios SOA. Se relaciona con el patrón **Centralización de Metadatos**, definido como patrón principal en el trabajo de arquitectura.

> **Alcance:** prototipo educativo. Los registros se guardan en memoria y se pierden al detener o reiniciar la aplicación. No está diseñado para producción.

## Requisitos

- Python 3.10 o superior
- `pip`

## Instalación y ejecución

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Luego abre `http://127.0.0.1:5000/` en el navegador.

## Endpoints disponibles

| Método | Ruta | Función | Código normal |
|---|---|---|---|
| GET | `/` | Información básica del proyecto | 200 |
| GET | `/health` | Comprueba que la API está activa | 200 |
| GET | `/api/v1/servicios` | Lista el catálogo | 200 |
| GET | `/api/v1/servicios/SRV-001` | Consulta un servicio por ID | 200 |
| POST | `/api/v1/servicios` | Registra un servicio nuevo | 201 |

Errores previstos: `400` si el JSON es inválido o faltan campos, `404` si no existe el identificador y `409` si se intenta duplicar un ID.

## Probar la API

Con la aplicación en ejecución, abre en el navegador:

- `http://127.0.0.1:5000/health`
- `http://127.0.0.1:5000/api/v1/servicios`
- `http://127.0.0.1:5000/api/v1/servicios/SRV-001`

Para registrar un servicio nuevo, ejecuta en una terminal:

```bash
curl -X POST http://127.0.0.1:5000/api/v1/servicios -H "Content-Type: application/json" -d '{"id":"SRV-003","name":"ConsultaInventario","description":"Consulta disponibilidad de un producto.","version":"1.0.0","protocol":"REST","method":"GET","path":"/api/v1/inventario/<producto_id>","owner":"Equipo SOA","status":"activo"}'
```

## Estructura

```text
proyecto_catalogo_soa/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── evidencias/
```

La carpeta `evidencias/` queda destinada a capturas tomadas por el equipo al ejecutar y probar realmente la API.

## Cómo se relaciona con SOA

- **Consumidor:** navegador, `curl` u otra aplicación que invoca la API.
- **Servicio REST/proveedor:** aplicación Flask que recibe las solicitudes HTTP.
- **Contrato/interfaz:** rutas, métodos HTTP, campos JSON y códigos de estado documentados en este archivo.
- **Repositorio de metadatos:** catálogo consultable mediante `/api/v1/servicios`.
- **Gobernanza:** cada registro incluye identificador, nombre, versión, propietario y estado.

## Evidencias que debe aportar el equipo

Guarden capturas auténticas en `evidencias/` de: (1) aplicación iniciada, (2) listado de servicios, (3) consulta por ID, (4) registro exitoso con código HTTP 201 y (5) repositorio público mostrando los archivos. No incluyan contraseñas, tokens ni datos personales reales.

## Publicar en GitHub

Repositorio previsto: `https://github.com/Jeferson1021/catalogo-centralizado-soa`

Para subir estos archivos, descomprima el ZIP en su equipo, abra el repositorio en GitHub y use **Add file → Upload files**. Arrastre los archivos y carpetas del proyecto (no solo el archivo ZIP), escriba un mensaje como `Agrega implementación REST del catálogo SOA` y seleccione **Commit changes**. Revise después que `app.py`, `requirements.txt` y este `README.md` aparezcan en la página principal del repositorio.

Para un entorno productivo se necesitarían persistencia en base de datos, autenticación y autorización, validaciones más robustas, pruebas automatizadas y despliegue seguro.
