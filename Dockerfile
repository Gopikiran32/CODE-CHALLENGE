
FROM apache/airflow:2.0.1

ARG AIRFLOW_USER_HOME=/usr/local/airflow

COPY airflow/dags ${AIRFLOW_USER_HOME}/dags
COPY requirements.txt /requirements.txt

RUN pip install --user --upgrade pip
RUN pip install --user -r /requirements.txt


USER airflow 