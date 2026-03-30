import requests
from requests.auth import HTTPBasicAuth

FACTURAMA_URL = "https://api.facturama.mx/v3/cfdis"

USER = "TU_USER"
PASS = "TU_PASS"

def crear_factura(data):
    response = requests.post(
        FACTURAMA_URL,
        json=data,
        auth=HTTPBasicAuth(USER, PASS)
    )
    return response.json()

def cancelar_factura(cfdi_id):
    response = requests.delete(
        f"{FACTURAMA_URL}/{cfdi_id}",
        auth=HTTPBasicAuth(USER, PASS)
    )
    return response.json()