#!/bin/bash
cd /home/ubuntu/ecommerce/ecommerce/
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
