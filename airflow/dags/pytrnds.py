import json
import os
from datetime import date ,datetime,timedelta
from airflow.models import Variable

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow import settings
from airflow.models import Connection
from pytrends.request import TrendReq
import pandas as pd
import time
from dateutil.relativedelta import relativedelta  

gcs_bucket = os.getenv("gcs_bucket")


args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}



with DAG(
        dag_id="pythrends_to_gcs",
        default_args=args,
        schedule_interval='5 0 * * *',
        start_date=days_ago(1),
        dagrun_timeout=timedelta(minutes=5),
        is_paused_upon_creation=False
) as dag:


    def pythrends_tio_gcs(keywords_list=['BMW','Audi','Volkswagen','Mercedes','Lamborghini']):
        startTime = time.time()
        pytrend = TrendReq(hl='en-GB', tz=360)
    
        today = date.today().strftime('%Y-%m-%d')
        my_date_years = date.today() - relativedelta(years = 3)
        from_date = my_date_years.strftime('%Y-%m-%d')
    
        pytrend.build_payload(
        kw_list=keywords_list,
        cat=0,
        timeframe='2022-09-23 2022-09-24',
        #geo='GB'
        )
        data = pytrend.interest_over_time()
  
        #data = data.drop(labels=['isPartial'],axis='columns')
        result = data.loc[from_date:today]
        
        result.to_csv(f'gs://{gcs_bucket}/trends/search_trends.csv')
        executionTime = (time.time() - startTime)
        print('Execution time in sec.: ' + str(executionTime))



    pythrends_tio_gcs_operator = PythonOperator(
    task_id='pythrends_tio_gcs',
    python_callable=pythrends_tio_gcs
    )
    
    

pythrends_tio_gcs_operator
