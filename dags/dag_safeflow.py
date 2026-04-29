from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Adiciona a pasta scripts ao caminho para o Airflow achar seus arquivos
sys.path.append(os.path.abspath("/opt/airflow/scripts"))
from transform import limpar_dados_vendas

with DAG(
    'retail_data_safeflow_pipeline',
    start_date=datetime(2026, 4, 28),
    schedule_interval='@daily',
    catchup=False
) as dag:

    # Aqui o Airflow chama a função que você já testou!
    task_transform = PythonOperator(
        task_id='limpar_vendas_varejo',
        python_callable=limpar_dados_vendas,
        op_kwargs={
            'caminho_bruto': '/opt/airflow/data/vendas_brutas.csv',
            'caminho_limpo': '/opt/airflow/data/vendas_limpas.csv'
        }
    )