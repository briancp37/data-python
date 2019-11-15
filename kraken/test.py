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






# # credentials = {
# #   "type": "service_account",
# #   "project_id": "data-258920",
# #   "private_key_id": "0e8be915edc664df341c5fe90383ad824c69a984",
# #   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC9/lPRzmMOHJLq\nO4WHTLPat7nqs5KNk1zp26dcYbvfqAiYBrTdN6TkaaxI6AjLvlmDD6HUfNgu1TRg\nI1z6ns1hoTw5dvEuN8VWxizBmgcYt/6Am/CxPmiukVCWfbgNIkCJNX322bk+BbsN\nPfS1TO2ChHIpc4f1eQ4mgUUAr692Mba5Mi+h76S0zgMoV2VZE5JCLv3B4Xj60Bmx\n6dstF+wMmETJZyHUsNHDxJjdEbldEJVMvjZFVLDjue+dR7GYWVYP4+Sad8dPhXau\nZOWToLUYGNmwynEJUH3qwrvIDuKkWCZokp7hEnitxfNcT+Zp/N9k7/tKwqB7ijOD\nnieop+ODAgMBAAECggEAC5g7RkkJm4Fb5+aFAhpIuZbPxkZ6MaCmIXFxt74RKJeJ\nGroCDKQKMJRQWsyqSMDPlqN8FUsfKFCDl0BhOrw5PXWJBtq+4jquFNsYPSJov3Xv\nFqstl6t+2PRuThjTBB4sgRMeIlPsLaBM54R57ByLPBVYIDZ4PB9MoUXvT5jpJNXN\nr8NIkorjVKgtzESBaEY24/EpWNUnosqDqR36gcW8KXWWFyHzFB8R3AcabXq+4Va/\n+KfNSSuwGNS21uzI7X1dgDV+bEn+4c7TApN+vHEdETeFPjNPb4nNgiOllxB+mHd5\n54OtkpmSkH2w441vNNk15oSPIzmy6o1V8DymUJWpcQKBgQD8EBjP9d0XOEq9Qr3e\nHr2KL/k7lLgxsZegVXFxoVn37fZlqBbrlzxgBvFsn2A2O/jduIyNBgnppTagauiT\nFddW/AwDxNNrHO58zYYQfVZKFYIOEKjqxmvn3G198TK72hZ2lPvoIH8ruwf9tu7v\nqopCdRW3tjNLdbq85vOeHAv4EQKBgQDA9gnk8q0DGSPGpwMxui8rCp8pQvzkE7t4\nM15KAYBRbk5vGiRSJJw5+vqi+HUpYnfu63vBD1oPH7y2sFTSxVA7FIw2XPXMo+cY\nACNVPDFsG+47oBh1Z6Z2obvEh9YwRAb3vXf8Bes0fjsquZ3Z1IL7r6e4P6nrGvse\nDWDsvyUWUwKBgC796UJL+e3sRrLGEJOqc3ehvftHnJdXHod7pmyiwh0gtgD5t1ww\nk8brRHMVu2AhCiJ712grKgnvDSIXDEjvl3fWAX9qYGfluuh1gHrugvnIzLhGjtdG\nKrPNOnRyVR0EaY+t8tCxzkOe2LyKMD1qM+Bz55qaUzHMPwYcoGpnnCuhAoGAM+M1\nX+pd2cJt22JXuox9WI6fpAHObSpdNAJkLXRf5AXMc5XNBIWxuOmjciVro/hFleqe\nuZh+OCjpnxqlhJPociqhVZEDy8abQtnupmHsTEzqcAAp85AutCHjkwKP9ySj1wSM\n+ilBSTlUgbWuG8BIhJOEf0gnUgBMXJVuZds0ht8CgYAyVCZro2SQAYlkIu7UE2Kq\nq4tIuCfYr1Av6rjYyvyqEO9EnPUBN5j/XG4+qfUxVTUky8DefZKpP5EuZHIeKeTu\n5QFlrSUcCNkgPFgRLv0JnZWjhvn8CVZaOXc6CT7kohy8d01e86qx7bFwgLmyOaaX\nz3TQtQayt4WSSPcJAYGhwg==\n-----END PRIVATE KEY-----\n",
# #   "client_email": "data-962@data-258920.iam.gserviceaccount.com",
# #   "client_id": "112715550593886404273",
# #   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
# #   "token_uri": "https://oauth2.googleapis.com/token",
# #   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
# #   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/data-962%40data-258920.iam.gserviceaccount.com"
# # }

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