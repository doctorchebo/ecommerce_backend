#!/bin/bash
cd /home/ubuntu/ecommerce/ecommerce/
python3.7 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
