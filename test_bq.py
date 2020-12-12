
# import featureng

def test_gcp_auth():
    import os
    from google.cloud import bigquery
    creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    client = bigquery.Client.from_service_account_json(creds)
