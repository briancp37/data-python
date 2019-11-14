import requests
import pandas as pd
import json
import csv
import time
import pandas_gbq as pd_gbq

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class AssetPairs:
    
    def __init__(self):
        with open('/Users/bpennington/git/data-python/kraken/data/AssetPairs.json') as json_file:
            self.asset_pairs = json.load(json_file)
        
        with open('/Users/bpennington/git/data-python/kraken/data/AssetPairsUSD.json') as json_file:
            self.asset_pairs_USD = json.load(json_file)


    def get_AssetPairs(self, base_currency=None):
        url = 'https://api.kraken.com/0/public/AssetPairs'
        r = requests.get(url)
        x = r.json()
        data = x['result']
        pairs = list(data.keys())
        
        json_dict = {}
        for pair in pairs:
            real_name = data[pair]['altname']
            json_dict[real_name] = data[pair]
            json_dict[real_name]['codename'] = pair

        return json_dict

    def save_AssetPairs(self, base_currency=None):
        if base_currency != None:
            with open('/Users/bpennington/git/data-python/kraken/data/AssetPairs' + base_currency + '.json', 'w') as json_file:
                json.dump(self.asset_pairs_USD, json_file)
        else:
            with open('/Users/bpennington/git/data-python/kraken/data/AssetPairs.json', 'w') as json_file:
                json.dump(self.asset_pairs, json_file)
        # print(path)
        # with open(path, 'w') as json_file:
        #     json.dump(self.asset_pairs, json_file)
        # return None

    # def open_AssetPairs(self, base_currency=None):
    #     if base_currency != None:
    #         path = '/Users/bpennington/git/data-python/kraken/data/AssetPairs' + base_currency + '.json'
    #     else:
    #         path = '/Users/bpennington/git/data-python/kraken/data/AssetPairs.json'
    #     print(path)
    #     # path = '/Users/bpennington/git/data-python/kraken/data/AssetPairsUSD.json'
    #     with open(path) as json_file:
    #         data = json.load(json_file)
    #         print(data)
    #         return data

    def subset_AssetPairs(self, base_currency):
        data = self.asset_pairs
        pairs = list(data.keys())

        subset_json = {}
        for pair in pairs:
            if pair[-3:] == base_currency:
                subset_json[pair] = data[pair]
                # subset_json[data[pair]['altname']] = data[pair]
                # subset_json[data[pair]['altname']]['codename'] = pair
        print(subset_json)
        self.asset_pairs_USD = subset_json

    def date_added(self):
        arr = []
        for pair in list(self.asset_pairs_USD.keys()):
            ts = self.asset_pairs_USD[pair]['first']
            dt = pd.to_datetime(ts, unit='s')
            arr.append([pair,dt])
            # print('{} First Price: {}'.format(pair, dt))
            # print(ts)
        df = pd.DataFrame(arr, columns=['pair', 'first'])
        df.index = df['first']
        df.sort_index(inplace=True)
        del df['first']
        return df


    
'''
pair = asset pair to get OHLC data for
interval = time frame interval in minutes (optional): 1 (default), 5, 15, 30, 60, 240, 1440, 10080, 21600
since = return committed OHLC data since given id (optional.  exclusive)
'''
class DataApi(AssetPairs):

    def __init__(self, pair):
        self.df = pd.DataFrame()
        self.pair = pair
        self.project_id = 'data-258920'
        super().__init__()


    def get_ohlc_df(self, interval=1440, since=None):
        url = 'https://api.kraken.com/0/public/OHLC?pair=' + self.pair + '&interval=' + str(interval)
        r = requests.get(url)
        x = r.json()
        index_arr = []
        price_arr = []

        for row in x['result'][self.asset_pairs_USD[self.pair]['codename']]:
            index_arr.append(row[0])
            price_arr.append([float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7])])
        
        columns = ['open', 'high', 'low', 'close', 'vwap', 'volume', 'count']
        self.df = pd.DataFrame(price_arr, columns = columns, index = index_arr)
        return self.df

    def ohlc_to_gbq(self, df):
        print(self.pair)
        table_id = 'prices.' + self.pair
        pd_gbq.to_gbq(df, table_id, project_id = self.project_id)
    
    def save_ohlc_csv(self, df, pair):
        path = '/Users/bpennington/git/data-python/kraken/data/' + pair + '_ohlc.csv'
        self.df.to_csv(path)

    def open_ohlc(self, pair):
        path = '/Users/bpennington/git/data-python/kraken/data/' + pair + '_ohlc.csv'
        self.df = pd.read_csv(path, index_col = 0)
        return self.df

    def get_prices(self, pairs_arr):

        pairs_arr = ['ZECUSD','XMRUSD','BCHUSD', 'XBTUSD','DASHUSD','LTCUSD','ETHUSD','ETCUSD', 'XRPUSD']
        i=0
        for pair in pairs_arr:
            df = self.open_ohlc(pair)
            if i==0:
                df_comb = pd.DataFrame(df['open'].tolist(), index=df.index, columns = [[pair]])
                print(df_comb)
            else:
                df_comb[pair] = df['open'].tolist()
                # df_comb = pd.concat([df_comb, df], join='inner', axis=1)
            i+=1

        return df_comb








# asset_pairs = get_AssetPairs()
# save_AssetPairs(asset_pairs)
# asset_pairs_USD = subset_AssetPairs('USD')
# print(asset_pairs_USD)
# save_AssetPairs(asset_pairs_USD, 'USD')

# df = get_prices()
# df.index = pd.to_datetime(df.index, unit='s')
# print(df)


# ap = AssetPairs()
# print(ap.date_added().pair)
# asset_pairs = ap.asset_pairs_USD
# arr = []
# for pair in list(asset_pairs.keys()):
#     ts = asset_pairs[pair]['first']
#     dt = pd.to_datetime(ts, unit='s')
#     arr.append([pair,dt])
#     # print('{} First Price: {}'.format(pair, dt))
#     # print(ts)
# df = pd.DataFrame(arr, columns=['pair', 'first'])
# df.index = df['first']
# df.sort_index(inplace=True)
# print(df)

#     df = open_ohlc(pair)
#     print(df.head())
#     first_ts = df.index[0]
#     asset_pairs[pair]['first'] = int(first_ts)

# print(asset_pairs)


# ap.save_AssetPairs('USD')





# i = 0
# for pair in pairs_USD[6:]:
#     codename = asset_pairs_USD[pair]['codename']
#     df = get_ohlc_df(pair, codename)
#     save_ohlc_csv(df, pair)
#     print("{}/{} -- {} download complete".format(i+1, len(pairs_USD), pair))
#     time.sleep(1.5)
#     i += 1
#     print(time.time())






# USD_pairs = [['XBTUSD', 'XXBTZUSD']]




























    # def get_ohcl_param(pair, interval=1440, since=None):
    #     url = 'https://api.kraken.com/0/public/OHLC'#?pair=' + pair + '&interval=' + str(interval)'
    #     params = {'pair': pair,
    #             'interval': interval,
    #             'since': since}
    #     r = requests.get(url=url, params=params)
    #     x = r.json()
    #     print(x)
    #     return(x)