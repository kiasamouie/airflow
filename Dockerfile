# Dockerfile for custom Airflow setup
FROM apache/airflow:2.6.3

# Copy setup.sh to /opt/airflow early in the Dockerfile
COPY setup.sh /opt/airflow/setup.sh

# Ensure setup.sh is executable
RUN chmod +x /opt/airflow/setup.sh

# Remaining Dockerfile content (e.g., copying dags, plugins, etc.)
COPY ./dags /opt/airflow/dags
COPY ./plugins /opt/airflow/plugins
