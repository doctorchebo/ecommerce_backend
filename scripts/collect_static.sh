#!/bin/bash
source /home/ubuntu/ecommerce/ecommerce/.venv/bin/activate
python /home/ubuntu/ecommerce/ecommerce/manage.py collectstatic --noinput
