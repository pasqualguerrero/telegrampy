#!/usr/bin/env sh

coverage run --source=telegrampy/ --omit=*test* setup.py test
coverage report -m
