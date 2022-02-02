#!/bin/bash

VIRTUAL_ENV=.venv
REQUIREMENTS=requirements.txt

FILENAME=$(basename "$0")
SHORTNAME="${FILENAME%.*}"
SCRIPTNAME="${SHORTNAME}.py"

cd "$( dirname "${BASH_SOURCE[0]}" )"

####
# Create virtualenv if needed
####
if [ ! -d ${VIRTUAL_ENV} ] ; then
    python3 -m venv ${VIRTUAL_ENV} 2>&1 >/dev/null
    ${VIRTUAL_ENV}/bin/python -m pip install --upgrade pip 2>&1 >/dev/null
fi

####
# Install or update requirements
####
if [ -f requirements.txt ] ; then
    ${VIRTUAL_ENV}/bin/pip install -qr requirements.txt 2>&1 >/dev/null
fi

####
# Set environment variables if any
####
for file in .env*; do
    if [ -f ${file} ] ; then
        source ${file}
    fi
done

####
# Invoke script
####
${VIRTUAL_ENV}/bin/python -B ${SCRIPTNAME} $@
