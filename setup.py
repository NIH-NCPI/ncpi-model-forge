import os
from setuptools import setup, find_packages

root_dir = os.path.dirname(os.path.abspath(__file__))
req_file = os.path.join(root_dir, 'requirements.txt')
with open(req_file) as f:
    requirements = f.read().splitlines()

FHIR_VERSION = "4.0.1"
version = __import__('ncpi_model_forge').__version__

setup(
    name='ncpi-model-forge',
    version=version,
    description=f'NCPI Project Forge FHIR {FHIR_VERSION} Ingest Plugin',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements
)
