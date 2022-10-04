**CODE-CHALLENGE**

About The Project

Airflow DAG to download last 3 years google trends data for given 5 key words in to gcs bucket.

1. create gcs bucket.
2. Create serveice acocount
3. Genarate Json key for created service acount and save in local system. 


Update bellow environment variable in docker-compose.yaml

GOOGLE_APPLICATION_CREDENTIALS:
gcs_bucket:

example
GOOGLE_APPLICATION_CREDENTIALS:'/user/keys/gcp_auth.json' #provide your json file local path
gcs_bucket: 'big-data-analytics-ap' #provide your gcs bucket name
