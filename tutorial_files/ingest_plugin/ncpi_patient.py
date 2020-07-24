"""
Builds FHIR Patient resources (https://www.hl7.org/fhir/patient.html)
conforming to the NCPI Patient profile:
(ncpi_model_forge/site_root/input/resources/profiles/StructureDefinition-ncpi-patient.json)
from rows of tabular patient/participant data.
"""

# https://hl7.org/fhir/us/core/ValueSet-omb-ethnicity-category.html
omb_ethnicity_category = {
    "Hispanic or Latino": {
        "url": "ombCategory",
        "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "2135-2",
            "display": "Hispanic or Latino",
        },
    },
    "Not Hispanic or Latino": {
        "url": "ombCategory",
        "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "2186-5",
            "display": "Not Hispanic or Latino",
        },
    },
}

# https://hl7.org/fhir/us/core/ValueSet-omb-race-category.html
omb_race_category = {
    "American Indian or Alaska Native": {
        "url": "ombCategory",
        "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "1002-5",
            "display": "American Indian or Alaska Native",
        },
    },
    "Asian": {
        "url": "ombCategory",
        "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "2028-9",
            "display": "Asian",
        },
    },
    "Black or African American": {
        "url": "ombCategory",
        "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "2054-5",
            "display": "Black or African American",
        },
    },
    "Native Hawaiian or Other Pacific Islander": {
        "url": "ombCategory",
        "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "2076-8",
            "display": "Native Hawaiian or Other Pacific Islander",
        },
    },
    "White": {
        "url": "ombCategory",
        "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "2106-3",
            "display": "White",
        },
    },
}

species_dict = {
    "Dog": {
        "url": "http://fhir.kids-first.io/StructureDefinition/species",
        "valueCodeableConcept": {
            "coding": [
                {
                    "system": "http://fhir.kids-first.io/CodeSystem/species",
                    "code": "448771007",
                    "display": "Canis lupus subspecies familiaris",
                }
            ],
            "text": "Dog",
        },
    },
    "Human": {
        "url": "http://fhir.kids-first.io/StructureDefinition/species",
        "valueCodeableConcept": {
            "coding": [
                {
                    "system": "http://fhir.kids-first.io/CodeSystem/species",
                    "code": "337915000",
                    "display": "Homo sapiens",
                }
            ],
            "text": "Human",
        },
    },
}


class Patient:
    class_name = "patient"
    resource_type = "Patient"
    target_id_concept = "PATIENT_FHIR_ID"

    @staticmethod
    def build_key(record):
        assert None is not record["PATIENT_ID"]
        return record["PATIENT_ID"]

    @staticmethod
    def build_entity(record, key, get_target_id_from_record):
        study_id = record.get("STUDY_ID")
        participant_id = record.get("PATIENT_ID")
        ethnicity = record.get("PATIENT_ETHNICITY")
        race = record.get("PATIENT_RACE")
        species = record.get("PATIENT_SPECIES")
        gender = record.get("PATIENT_GENDER")

        entity = {
            "resourceType": Patient.resource_type,
            # This is how you would use get_target_id_from_record, but we're going
            # to skip it here.
            # "id": get_target_id_from_record(Patient, record),
            "meta": {
                "profile": [
                    "http://fhir.ncpi-project-forge.io/StructureDefinition/ncpi-patient"
                ]
            },
            "identifier": [
                {
                    "system": "urn:ncpi-project-forge:unique-string",
                    "value": f"Patient__{study_id}__{key}",
                },
            ],
        }

        if ethnicity:
            if omb_ethnicity_category.get(ethnicity):
                entity.setdefault("extension", []).append(
                    {
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                        "extension": [
                            omb_ethnicity_category[ethnicity],
                            {"url": "text", "valueString": ethnicity},
                        ],
                    }
                )

        if race:
            if omb_race_category.get(race):
                entity.setdefault("extension", []).append(
                    {
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                        "extension": [
                            omb_race_category[race],
                            {"url": "text", "valueString": race},
                        ],
                    }
                )

        if species:
            if species_dict.get(species):
                entity.setdefault("extension", []).append(species_dict[species])

        if gender:
            entity["gender"] = gender

        return entity
