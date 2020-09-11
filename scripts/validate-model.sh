#!/bin/bash

PUBLISHER="${PUBLISHER:-../org.hl7.fhir.publisher.jar}"

# For some reason, this generates a bunch of files owned by root which then cause problems later on
# during the validation. 
#fhirutil add ./site_root/input/resources
#java -Djava.awt.headless=true -jar $PUBLISHER -ig site_root/ig.ini -tx n/a

fhirutil validate ./site_root/ig.ini --publisher_opts='-tx n/a'
