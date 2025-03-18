#!/usr/bin/env bash

coverage run -m pytest -s tests/$1 && coverage html
