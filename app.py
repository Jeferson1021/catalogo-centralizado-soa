from flask import Flask, jsonify, request

app = Flask(__name__)

# Catálogo de ejemplo en memoria para la demostración académica.
# Los registros se reinician al detener la aplicación.
services = [
    {
        "id": "SRV-001",
        "name": "ConsultaCliente",
        "description": "Consulta información básica de un cliente.",
        "version": "1.0.0",
        "protocol": "REST",
        "method": "GET",
        "path": "/api/v1/clientes/<cliente_id>",
        "owner": "Equipo SOA",
        "status": "activo",
    },
    {
        "id": "SRV-002",
        "name": "ConsultaPedido",
        "description": "Consulta el estado de un pedido.",
        "version": "1.0.0",
        "protocol": "REST",
        "method": "GET",
        "path": "/api/v1/pedidos/<pedido_id>",
        "owner": "Equipo SOA",
        "status": "activo",
    },
]


@app.get("/")
def home():
    return jsonify({
        "proyecto": "Catálogo centralizado de servicios SOA",
        "estado": "activo",
        "documentacion": "Consulte README.md para los endpoints disponibles.",
    }), 200


@app.get("/health")
def health():
    return jsonify({"status": "UP"}), 200


@app.get("/api/v1/servicios")
def list_services():
    return jsonify({"total": len(services), "servicios": services}), 200


@app.get("/api/v1/servicios/<service_id>")
def get_service(service_id):
    service = next((s for s in services if s["id"].lower() == service_id.lower()), None)
    if service is None:
        return jsonify({"error": "Servicio no encontrado", "id": service_id}), 404
    return jsonify(service), 200


@app.post("/api/v1/servicios")
def create_service():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "El cuerpo debe ser un objeto JSON válido."}), 400

    required = ["id", "name", "description", "version", "protocol", "method", "path", "owner", "status"]
    missing = [field for field in required if not payload.get(field)]
    if missing:
        return jsonify({"error": "Faltan campos obligatorios.", "campos_faltantes": missing}), 400

    if any(s["id"].lower() == str(payload["id"]).lower() for s in services):
        return jsonify({"error": "Ya existe un servicio con ese id.", "id": payload["id"]}), 409

    service = {field: str(payload[field]) for field in required}
    services.append(service)
    return jsonify({"mensaje": "Servicio registrado correctamente.", "servicio": service}), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
