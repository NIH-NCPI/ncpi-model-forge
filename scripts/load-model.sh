#!/bin/bash

BASE_URL=${BASE_URL:-http://localhost:8000}
SERVER_UNAME=${SERVER_UNAME:-admin}
SERVER_PW=${SERVER_PWD:-password}

fhirutil validate ./site_root/ig.ini --publisher_opts='-tx n/a'

# Publish model to server
fhirutil publish site_root/input/resources/terminology \
		--base_url="$BASE_URL" --username="$SERVER_UNAME" --password="$SERVER_PW" && \
\
fhirutil publish site_root/input/resources/extensions \
		--base_url="$BASE_URL" --username="$SERVER_UNAME" --password="$SERVER_PW" && \
\
fhirutil publish site_root/input/resources/profiles \
		--base_url="$BASE_URL" --username="$SERVER_UNAME" --password="$SERVER_PW" && \
\
fhirutil publish site_root/input/resources/search \
		--base_url="$BASE_URL" --username="$SERVER_UNAME" --password="$SERVER_PW" 

