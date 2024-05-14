#!/bin/bash
sudo chown -R ubuntu:www-data /home/ubuntu/ecommerce/ecommerce
sudo systemctl start gunicorn
docker compose up