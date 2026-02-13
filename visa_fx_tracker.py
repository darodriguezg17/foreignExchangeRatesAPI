import requests
import json

from requests.auth import HTTPBasicAuth

# Rutas a los certificados de Visa
CERT_FILE = 'cert.pem'
KEY_FILE = 'key.pem'

user_id = 'user_id'
password = 'password'

# Endpoint de Sandbox para tasas de cambio
url = "https://sandbox.api.visa.com/forexrates/v2/foreignexchangerates"

# Estructura de la solicitud (Payload) en JSON
payload = json.dumps({
    "acquirerDetails": {
        "bin": 408999,
        "settlement": {
            "currencyCode": "840"
        }
    },
    "rateProductCode": "A",
    "markupRate": "0.07",
    "destinationCurrencyCode": "170",
    "sourceAmount": "100.55",
    "sourceCurrencyCode": "840"
})

# Ejecución de la solicitud usando Two-Way SSL
try:
    response = requests.post(
    url, 
    headers={'Content-Type': 'application/json'}, # Solo dejamos el tipo de contenido
    data=payload, 
    cert=(CERT_FILE, KEY_FILE),
    auth=HTTPBasicAuth(user_id, password) # Requests hace el trabajo sucio por ti
)
    
    if response.status_code == 200:
        print("Conexión exitosa con Visa Gateway")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error técnico: {response.status_code}") # Análisis de códigos de error
except Exception as e:
    print(f"Falla de conexión: {e}")
