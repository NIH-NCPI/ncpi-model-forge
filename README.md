# NCPI Project Forge FHIR Model

🔥The FHIR model developed in Project Forge

## FHIR 101 - A Practical Guide

If you have never heard of FHIR, are unfamiliar with how to implement FHIR,
or are confused by any of the terms in this README, then
check out the 📓 [FHIR 101 Jupyter Notebook](https://github.com/ncpi-fhir/fhir-101).


## Contributing

If you are a new contributor to the Project Forge FHIR model, 
please review the 📓 [NCPI Project Forge Development Guide](https://www.notion.so/d3b/NCPI-Forge-Development-Guide-4583e53de1fb4ffaa0bc46bc38a3c5fb) Notion page. 
It will walk you through the NCPI software development life cycle 
for the FHIR model using a practical example.

## Overview

This repository contains:

1. [NCPI Project Forge ImplementationGuide](site_root) - the files and required
folder structure needed to build HL7 documentation (known as an ImplementationGuide)
for the FHIR data model
2. [NCPI Project Forge FHIR Model](site_root/input/resources) - conformance and
example resource files that make up the FHIR model
4. [Unit Tests](tests) - to test the FHIR model

## Installation
1. Git clone this repository

```bash
git clone git@github.com:ncpi-fhir/ncpi-model-forge.git
cd ncpi-model-forge
```

2. Set up a Python virtual environment

```bash
# Create virtualenv
python3 -m venv venv

# Activate virtualenv
source venv/bin/activate
```

3. Install the necessary requirements

```bash
pip install -e .
```
Test the installation by running the CLI: `fhirutil -h`. You should see
something that contains:
```
Usage: fhirutil [OPTIONS] COMMAND [ARGS]...

  A CLI utility for validating FHIR Profiles and Resources
```

4. Install Docker CE: https://docs.docker.com/install/

Docker is needed because the fhirutil CLI executes the model validation
inside a Dockerized version of the HL7 IG Publisher.

## Develop

This section gives a quick overview of how to contribute to the Project
Forge FHIR model. Developers are highly encouraged to go through the
📓 [NCPI FHIR Software Development Guide](FHIR-SW-Development-Guide.ipynb).
to learn the NCPI software development life cycle, NCPI modeling standards,
and development tools.

Follow the steps below to get an idea of how FHIR model development and
validation works.

### 1. Add a new example conformance resource

```shell
cp docs/data/StructureDefinition-research-study.json site_root/input/resources/profiles
```

### 2. Add a new example data resource to test the conformance resource

```shell
cp docs/data/ResearchStudy-sd-001.json site_root/input/resources/examples
```

### 3. Validate the model

There are two ways to use the `fhirutil` CLI to validate the model.

```shell
# Method 1 - Uses the Dockerized IG publisher
fhirutil validate ./site_root/ig.ini --publisher_opts='-tx n/a'

# Method 2 - Uses native IG publisher - faster than above method
fhirutil add ./site_root/input/resources
java -jar org.hl7.fhir.publisher.jar -ig site_root/ig.ini -tx n/a
```

#### Method 1 - Dockerized IG Publisher

This method is slower since the `fhirutil` CLI has to spin up the Docker
container which runs the IG Publisher. The benefit of this is that, you
do not have to install the IG Publisher or its dependencies (Java, Jekyll)
on your machine.

The Docker images for the IG Publisher are built in the
[NCPI FHIR IG Publisher](https://github.com/ncpi-fhir/hl7-fhir-ig-publisher)
repository.

#### Method 2 - Native IG Publisher

Method 2 is faster since it's running the IG Publisher on your local machine,
but it means that you must first install the IG Publisher yourself.

1. Install the dependencies: [IG Publisher installation instructions](https://confluence.hl7.org/display/FHIR/IG+Publisher+Documentation#IGPublisherDocumentation-Installing).

2. Download the right version of the IG Publisher jar.

    The version you use should be identical to what the Dockerized IG Publisher
    uses. You can use the [Fetch IG Publisher script](https://github.com/ncpi-fhir/hl7-fhir-ig-publisher/blob/master/scripts/fetch_publisher_jar.sh) to download the correct version
    of the IG Publisher jar.

### 4. View Validation Results

The CLI will log output to the screen and tell you whether
validation succeeded or failed. You can view detailed validation
results at `./site_root/output/qa.html`

### Repository Layout

- Source files for FHIR Model ImplementationGuide (IG): `site_root`
- Unit tests: `tests`

```text
site_root
├── ig.ini                                     -> IG configuration file
└── input
    ├── ImplementationGuide-KidsFirst.json     -> IG FHIR resource
    └── resources                              -> FHIR resources that make up the models
        ├── examples                           -> Example resources
        ├── extensions                         -> Extensions
        ├── profiles                           -> StructureDefinition (non-Extension)
        ├── search                             -> SearchParameters
        └── terminology                        -> CodeSystems, ValueSets
```

The files `ig.ini` and `ImplementationGuide-NCPI-Project-Forge.json` contain
configuration information for the FHIR model's ImplementationGuide and
affect which resources are validated and included in the generated site.

Read more about them at <https://build.fhir.org/ig/FHIR/ig-guidance/index.html>
and <http://www.hl7.org/fhir/implementationguide.html>

### Naming Conventions

Since the NCPI FHIR model is validated using the `ncpi-fhir-utility`,
the FHIR resource payloads and filenames are expected to follow certain
standards otherwise validation will fail.  

Please see the NCPI FHIR Utility's
[naming conventions doc](https://github.com/ncpi-fhir/ncpi-fhir-utility/blob/master/docs/naming_conventions.md) for details.

## Testing

### Unit Tests

The unit test for the FHIR model is the same as the
[Validate the Model](#3-validate-the-model) step in FHIR Model Development section.

The unit test is automatically run by the repository's
[CI pipeline](.circleci/config.yml).
