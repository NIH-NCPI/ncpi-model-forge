from requests import RequestException
from ncpi_fhir_utility.client import FhirApiClient
from tutorial_files.ingest_plugin.ncpi_patient import Patient

all_targets = [
  Patient
]


# Basic example submit method
def submit(host, entity_class, body):
    client = FhirApiClient(base_url=host, auth=("admin", "password"))
    success, result = client.send_request(
        "POST", f"{host}/Patient", json=body
    )
    if success:
        return result["response"]["id"]
    else:
        raise RequestException(f"Sent:\n{body}\nReceived:\n{result}")
