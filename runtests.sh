#!/bin/bash
set -eux

docker-compose run -e MODE='development'  --rm dashboard pytest -v --ignore=publishing --cov-report term-missing --cov=. --cov-config .coveragerc $*
