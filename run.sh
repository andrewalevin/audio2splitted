#!/bin/bash

source venv/bin/activate

python3 src/audio2splitted/audio2splitted.py --folder out --duration 11 --threshold 14 kofe.m4a
