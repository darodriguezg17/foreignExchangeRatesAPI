import requests
import json

# Rutas a los certificados de Visa
CERT_FILE = 'cert.pem'
KEY_FILE = 'key.pem'

# Endpoint de Sandbox para tasas de cambio
url = "https://sandbox.api.visa.com/forexrates/v1/foreignexchangerates"

# Estructura de la solicitud (Payload) en JSON
payload = json.dumps({
    "requestHeader": {
        "messageDateTime": "2026-02-12T14:00:00.000",
        "requestMessageId": "6da60e1b8b024532a2487345b"
    },
    "requestData": {
        "sourceCurrencyCode": "840", # USD
        "destinationCurrencyCode": "170", # COP (Colombia)
        "sourceAmount": "100.00"
    }
})

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YOUR_USER_ID:YOUR_PASSWORD' # Credenciales de VDP
}

# Ejecución de la solicitud usando Two-Way SSL
try:
    response = requests.post(url, headers=headers, data=payload, cert=(CERT_FILE, KEY_FILE))
    
    if response.status_code == 200:
        print("Conexión exitosa con Visa Gateway")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error técnico: {response.status_code}") # Análisis de códigos de error
except Exception as e:
    print(f"Falla de conexión: {e}")
