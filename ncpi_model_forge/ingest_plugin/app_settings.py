import os

from kf_lib_data_ingest.app.settings.development import (
    SECRETS,
    AUTH_CONFIGS,
)

TARGET_API_CONFIG = os.path.join(
    os.path.dirname(__file__), "ncpi_forge_fhir.py"
)
