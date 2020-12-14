
import pandas as pd
from google.cloud import bigquery

from . import exceptions

from typing import Union, List, Dict, Sequence


class BigQueryClient:
    def __init__(self, client: Union[str, bigquery.client.Client] = None):
        """BigQuery client

        :param client:
        """
        if isinstance(client,bigquery.client.Client):
            self.client = client
        elif isinstance(client,str):
            self.client = bigquery.Client.from_service_account_json(client)
        else:
            self.client = bigquery.Client()

    def _query(self, q, *args, **kwargs):
        res = self.client.query(q,*args,**kwargs)
        return [dict(r) for r in res]


class CensusAcsClient(BigQueryClient):
    def __init__(self):
        super().__init__(*args,**kwargs)
        self.table_ids = self.getTableNames()

    def getTableNames(self):
        return [t.table_id for t in self.client.list_tables(
            "bigquery-public-data.census_bureau_acs")]

    def query(self):
        pass
