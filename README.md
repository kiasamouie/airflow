
# Airflow Project Setup

This is a Dockerized setup for Apache Airflow. Follow the instructions below to get started.

## Project Structure

- **dags/**: Directory to store Airflow DAGs.
- **logs/**: Directory for storing Airflow logs.
- **plugins/**: Directory for any custom Airflow plugins.
- **docker-compose.yaml**: Docker Compose file to orchestrate services.
- **Dockerfile**: Dockerfile for building a custom Airflow image.

## Instructions

1. **Install Docker and Docker Compose** (if not installed).

2. **Clone the repository** (or download this folder) and navigate into it.

3. **Build and Start Airflow**:

   ```bash
   docker-compose up --build -d
   ```

4. **Access the Airflow Web UI**:

   - Go to `http://localhost:8080` in your browser to access the Airflow UI.

5. **Copy `setup.sh` Manually**:

   Give `setup.sh` full permissions

   ```bash
   chmod 777 ./setup.sh
   ```

   Copy into container

   ```bash
   docker cp setup.sh airflow-webserver:/opt/airflow/setup.sh
   ```

   SSH into container

   ```bash
   docker exec -it airflow-webserver bash
   ```

   Run setup file

   ```bash
   ./setup.sh
   ```
## Sample DAG

A sample DAG, `my_first_dag.py`, is provided under the `dags/` directory. It is a simple example to get started.
