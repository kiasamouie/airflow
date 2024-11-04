#!/bin/bash
# setup.sh: Initializes Airflow database and creates an admin user

# Initialize the Airflow database
airflow db init

# Create an admin user if one doesn't already exist
airflow users create \
    --username admin \
    --password password123 \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email kiadoe@example.com || echo "Admin user already exists"
