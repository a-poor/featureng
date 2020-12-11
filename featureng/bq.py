
from google.cloud import bigquery


class BigQueryLoader:
    def __init__(self,project=None,credentials=None):
        self.auth = auth
        self.client = bigquery.Client(
            project=project,
            credentials=credentials)

    def _query(self,q,*args,**kwargs):
        res = self.client.query(q,*args,**kwargs)
        return [dict(r) for r in res]
