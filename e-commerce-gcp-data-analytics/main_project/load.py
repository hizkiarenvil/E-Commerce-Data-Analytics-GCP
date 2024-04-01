import os
from google.cloud import storage
from google.cloud import bigquery
from google.api_core.exceptions import NotFound

# Set Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/your/service-account-key.json'

# Initialize Google Cloud Storage client
storage_client = storage.Client()

# Initialize Google BigQuery client
client = bigquery.Client()

# Define the name of the Cloud Storage bucket
bucket_name = 'renvil_data_bucket'

# Check if the bucket already exists, and create it if not
if not storage_client.lookup_bucket(bucket_name):
    bucket = storage_client.create_bucket(bucket_name, location='US')
else:
    print("Bucket already exists. Using existing bucket.")

# Access the specific bucket
my_bucket = storage_client.get_bucket(bucket_name)

# Function to upload a file to Cloud Storage bucket
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path, timeout=600)  # Set a timeout of 10 minutes
        return True
    except Exception as e:
        print(e)
        return False

# Path to the file to be uploaded to Cloud Storage
file_path = os.path.join(r'D:\Renvil.work\Data Engineering Project\e-commerce-gcp-data-analytics\main_project', 'e_commerce_data.csv')

# Upload the file to the Cloud Storage bucket
upload_to_bucket('dataset_renvil.csv', file_path, 'renvil_data_bucket')

# Define the dataset and table names in BigQuery
dataset_ref = client.dataset('bigquery_ecommerce')
table_ref = dataset_ref.table('ecommerce_data')

# Check if the dataset exists, and create it if not
try:
    client.get_dataset(dataset_ref)
    print("Dataset already exists.")
except NotFound:
    print("Dataset not found, creating...")
    dataset = bigquery.Dataset(dataset_ref)
    client.create_dataset(dataset)
    print("Dataset created successfully.")

# Define job configuration for loading data into BigQuery
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,  # Enable schema auto-detection
    skip_leading_rows=1,  # Assuming a header row
)

# URI for loading data into BigQuery from Cloud Storage
uri = f"gs://{bucket_name}/dataset_renvil.csv"  # Ensure correct GCS path

# Load data from Cloud Storage into BigQuery table
load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)


# Wait for the job to complete
try:
    load_job.result()
    print("Data loaded successfully into BigQuery table!")
except Exception as e:
    print(f"Error during data loading: {e}")
