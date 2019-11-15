import pydata_google_auth
import pandas_gbq
import pandas as pd
from google.cloud import bigquery
client = bigquery.Client()

class GBQ:

    def __init__(self):
        self.client = bigquery.Client()
        self.dataset_id = 'prices'
        self.project_id = 'data-258920'

    def read_table(self, table_id, dt=False):
        addr = self.project_id +"."+ self.dataset_id +"."+table_id
        query = (
            "SELECT ts, open FROM `" +addr+ "` "
        )
        query_job = self.client.query(query, location="US")
        idx_arr = []
        price_arr = []
        for row in query_job:
            idx_arr.append(row[0])
            price_arr.append(row[1])
        
        if dt == True:
            idx_arr = pd.to_datetime(idx_arr, unit='s')

        s = pd.Series(price_arr, index=idx_arr)
        s.name = table_id
        return s

    def agg_tables(self, cur_arr):
        print(cur_arr)
        # arr = [x for x in ap.asset_pairs_USD.keys()]
        for pair in cur_arr:
            s = self.read_table(table_id=pair, dt=True)
            df_ = pd.DataFrame(s).sort_index()
            df_ = df_.loc[~df_.index.duplicated(keep='first')]
            df_.asfreq(freq='D', method='ffill')
            
            if pair==cur_arr[0]:
                print(1)
                df = df_
            else:
                df = pd.concat([df,df_], axis=1)
                print(df)
        df.name = 'combined'
        return df
    
    def get_credentials():
        scopes = [
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/bigquery'
        ]
        credentials = pydata_google_auth.get_user_credentials(scopes)
        return credentials

# def write_table(self, df, if_exists='replace'):
#     table_id = self.dataset_id + '.' + df.name
#     df.to_gbq(destination_table = table_id, project_id = self.project_id, if_exists=if_exists)

# def append_table(self, pair, if_exists='append'):
#     table_id = self.dataset_id + '.' + self.pair
#     df.to_gbq(destination_table = table_id, project_id = self.project_id, if_exists=if_exists)



