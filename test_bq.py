
# import featureng

def test_gcp_auth():
    import os
    import json
    from pathlib import Path
    from google.cloud import bigquery

    # Get the path to the credentials
    creds = Path(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
    assert creds.exists()

    # Try to load the json file
    with creds.open() as f:
        json.load(f)

    # Try to authenticate
    client = bigquery.Client.from_service_account_json(creds)
