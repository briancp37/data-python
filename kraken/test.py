from .api import AssetPairs
from .api import DataApi
import requests
from BigQuery import GBQ
import pandas as pd
from google.cloud import bigquery
# client = bigquery.Client()

# ap = api.AssetPairs()

def GBQ_read_table():
    gbq = GBQ()
    table_id = 'ETHUSD'
    s = gbq.read_table(table_id, dt=True)
    return s

def GBQ_agg_tables():
    gbq = GBQ()
    pairs = ['ZECUSD','XMRUSD','BCHUSD', 'XBTUSD','DASHUSD','LTCUSD','ETHUSD','ETCUSD', 'XRPUSD']
    df = gbq.agg_tables(pairs)
    print(df)

def get_credentials():
    return None








#     da = DataApi(pair)
#     df = da.get_ohlc_df()
#     print(df)
#     da.ohlc_to_gbq(df, if_exists = 'replace')
#     i += 1



# da = DataApi('ADAUSD')
# df = da.get_ohlc_df()
# print(df)




# da = api.DataApi('XBTUSD')
# df = da.get_ohlc_df()
# print(df)
# da.ohlc_to_gbq(df)

# project_id = 'data-258920'
# dataset_id = 'prices'
# table_id = 'ADAUSD'
# url = 'https://bigquery.googleapis.com/bigquery/v2/projects/{}/datasets/{}/tables/{}/data'.format(project_id, dataset_id, table_id)
# r = requests.get(url)
# print(r)


# import pandas_gbq
# import pandas
# # import pydata_google_auth

# # SCOPES = [
# #     'https://www.googleapis.com/auth/cloud-platform',
# #     'https://www.googleapis.com/auth/drive',
# #     'https://www.googleapis.com/auth/bigquery'
# # ]

# # credentials = pydata_google_auth.get_user_credentials(
# #     SCOPES,
# #     # Set auth_local_webserver to True to have a slightly more convienient
# #     # authorization flow. Note, this doesn't work if you're running from a
# #     # notebook on a remote sever, such as over SSH or with Google Colab.
# #     # auth_local_webserver=True,
# # )

# # table_id = 'bigquery-public-data.bitcoin_blockchain'
# project_id = 'data-258920'

# sql = """
# SELECT open, high
# FROM `data-258920.prices.btcusd`
# """
# df = pandas_gbq.read_gbq(sql, project_id=project_id)
# print(df)


# # df = pandas.DataFrame(
# #     {
# #         "my_string": ["a", "b", "c"],
# #         "my_int64": [1, 2, 3],
# #         "my_float64": [4.0, 5.0, 6.0],
# #         "my_bool1": [True, False, True],
# #         "my_bool2": [False, True, False],
# #         "my_dates": pandas.date_range("now", periods=3),
# #     }
# # )

# # pandas_gbq.to_gbq(df, table_id, project_id=project_id)


# # df = pandas_gbq.read_gbq(
# #     "",
# #     project_id='data-258920',
# #     credentials=credentials,
# # )




# # ...  # From google-auth or pydata-google-auth library.

# # Update the in-memory credentials cache (added in pandas-gbq 0.7.0).
# # import pydata_google_auth
# # credentials = pydata_google_auth.get_user_credentials(
# #     ['https://www.googleapis.com/auth/bigquery'],
# # )
# # print(credentials)

# # pandas_gbq.context.credentials = credentials
# # pandas_gbq.context.project = 'data-258920'

# # # The credentials and project_id arguments can be omitted.
# # # project_id = 'data-258920'
# # df = pandas_gbq.read_gbq("", project_id = 'data-258920')
# # print(df)