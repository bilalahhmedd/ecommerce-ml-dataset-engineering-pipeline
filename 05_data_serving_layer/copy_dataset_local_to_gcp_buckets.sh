gcloud auth login
gcloud activate-service-account --key-file=path/to/your/service-account-key.json
gsutil -m cp -r /data/input gs://my-bucket/input