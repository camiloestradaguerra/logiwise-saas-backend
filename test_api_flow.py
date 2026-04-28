import requests

BASE_URL = "http://127.0.0.1:8000"
USERNAME = "admin@example.com"
PASSWORD = "admin"
TENANT_ID = "tenant1"

def get_token():
    url = f"{BASE_URL}/auth/token"
    data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(url, data=data, headers=headers)
    resp.raise_for_status()
    token = resp.json()["access_token"]
    print("Token obtenido:", token)
    return token

def create_shipment(token):
    url = f"{BASE_URL}/shipments/"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Tenant-ID": TENANT_ID,
        "Content-Type": "application/json"
    }
    payload = {
        "origen": "BOG",
        "destino": "MIA",
        "tipo_carga": "general",
        "estado": "Draft",
        "moneda": "USD",
        "peso": 1000,
        "volumen": 2.5,
        "tenant_id": TENANT_ID
    }
    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()
    shipment = resp.json()
    print("Shipment creado:", shipment)
    return shipment["id"]

def list_shipments(token):
    url = f"{BASE_URL}/shipments/"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Tenant-ID": TENANT_ID
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    shipments = resp.json()
    print("Shipments encontrados:", shipments)
    return shipments

if __name__ == "__main__":
    token = get_token()
    shipment_id = create_shipment(token)
    shipments = list_shipments(token)
    print("\n¡Flujo automatizado completado con éxito!")
