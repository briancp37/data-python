import pydata_google_auth
import pandas_gbq
import pandas as pd
from google.cloud import bigquery
client = bigquery.Client()
from api import 

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
        df.name = 'daily_combined'
        return df
    
    def get_credentials():
        scopes = [
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/bigquery'
        ]
        credentials = pydata_google_auth.get_user_credentials(scopes)
        return credentials

    def write_table(self, df, if_exists='replace'):
        table_id = self.dataset_id + '.' + df.name
        df.to_gbq(destination_table = table_id, project_id = self.project_id, if_exists=if_exists)

    def update_all_prices(self):
        markets = [x for x in ap.asset_pairs_USD.keys()]
        last_ts = get_last_ts()
        price_dict = {}
        data = get_daily_prices()
    
    def append_pair_table(self, pair):
        table_id = self.dataset_id + '.' + pair
        df.to_gbq(destination_table = table_id, project_id = self.project_id, if_exists=append)

    def get_last_ts():
        last_ts = 1
        return last_ts

    


    def get_ohlc_dfs(self, interval=1440, since=None):
        url = 'https://api.kraken.com/0/public/OHLC?pair=' + self.pair + '&interval=' + str(interval)
        r = requests.get(url)
        x = r.json()
        index_ts = []
        price_arr = []

        for row in x['result'][self.asset_pairs_USD[self.pair]['codename']]:
            index_ts.append(row[0])
            price_arr.append([row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7])])
        
        columns = ['ts', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'count']
        index_dt = pd.to_datetime(index_ts, unit='s')
        self.df = pd.DataFrame(price_arr, columns = columns, index = index_dt)
        return self.df