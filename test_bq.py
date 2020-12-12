
# import featureng


def test_gcp_auth():
    from google.cloud import bigquery
    client = bigquery.Client()
