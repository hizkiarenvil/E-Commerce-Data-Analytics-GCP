from google.cloud import storage

def create_bucket(gcs_test_ecommerce):
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_test_ecommerce)

    # Create the bucket
    bucket.create()

    print(f'Bucket {gcs_test_ecommerce} created!')

if __name__ == '__main__':
    create_bucket('gcs_test_ecommerce')
