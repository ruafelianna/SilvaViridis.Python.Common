#!/usr/bin/env bash

coverage run -m pytest -s tests && coverage html
