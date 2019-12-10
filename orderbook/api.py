import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


'''
@returns pd.DataFrame, index=price, <exchange_name> = units at that price

'''
class OrderBooks:

    def __init__(self, exchanges, coin, base, side):
        self.exchanges = exchanges
        self.coin = coin
        self.base = base
        self.side = side
        self.ob_dispatch = {'hitbtc': self.hitbtc_orderbook,
                            'kraken': self.kraken_orderbook}

    def combine(self):
        for ex in self.exchanges:
            if ex==self.exchanges[0]:
                self.df = self.ob_dispatch[ex]()
            else:
                df_ = self.ob_dispatch[ex]()
                self.df = self.df.join(df_, how='outer')
        if self.side == 'bid':
            self.df.sort_index(axis=0, ascending=False, inplace=True)
        else:
            self.df.sort_index(axis=0, ascending=True, inplace=True)
        self.df['combined'] = self.df[self.exchanges].sum(axis=1, skipna=True)
        self.df['cumulative'] = self.df['combined'].cumsum()

        return self.df

        # hitbtc_ob = hitbtc_orderbook()
        # # print(hitbtc_ob)
        # kraken_ob = kraken_orderbook()
        # # print(kraken_ob)
        # df_ob = hitbtc_ob
        # df_ob = df_ob.join(kraken_ob, how='outer')
        # df_ob.sort_index(inplace=True)
        # df_ob['combined'] = df_ob[['hitbtc', 'kraken']].sum(axis=1, skipna=True)
        # df_ob['cumulative'] = df_ob['combined'].cumsum()
        # return df_ob

    def hitbtc_orderbook(self):
        pair = self.coin + self.base #'BTCUSD'

        url = 'https://api.hitbtc.com/api/2/public/orderbook/' + pair + '?limit=0'
        r = requests.get(url)
        x = r.json()
        
        df = pd.DataFrame(x[self.side])
        df['hitbtc'] = df['size'].astype(float)
        df.index = df['price'].astype(float)
        del df['price']
        del df['size']

        if(self.side=='bid'):
            df.sort_index(axis=0, ascending=False, inplace=True)
        df['hitbtc_cum'] = df['hitbtc'].cumsum()
        
        return df

    def kraken_orderbook(self):
        pair = 'XBTUSD'
        if(self.coin == 'BTC'):
            pair = 'XBT' + self.base
        else:
            pair = self.coin + self.base

        url = 'https://api.kraken.com/0/public/Depth?pair=' + pair + '&count=500'
        r = requests.get(url)
        x = r.json()
        
        df = pd.DataFrame(x['result']['XXBTZUSD'][self.side+'s'], columns=['price', 'kraken', 'ts'])
        df.index = df['price'].astype(float)
        df['kraken'] = df['kraken'].astype(float)
        del df['price']
        del df['ts']

        if(self.side=='bid'):
            df.sort_index(axis=0, ascending=False, inplace=True)
        df['kraken_cum'] = df['kraken'].cumsum()
        
        return df

    def binance(self):

        url = 'https://api.binance.com/api/v3/depth' + pair + '?limit=0'
        r = requests.get(url)
        x = r.json()
        
        df = pd.DataFrame(x[self.side+'s'], columns=['price', 'binance'])
        df.index = df['price'].astype(float)
        df['binance'] = df['binance'].astype(float)
        del df['price']
    
    def bitfinex(self):
        pass

    def huobi_global(self):
        pass

    def okex(self):
        pass
    
    def coinbase_pro(self):
        pass

    def bittrex(self):
        pass



def plot_ob(df_bid, df_ask, exchanges, coin, base):
    df_bid.sort_index(inplace=True)
    # print(df_bid, df_ask)

    colors = {'hitbtc': 'blue',
              'kraken': 'orange'}

    fig, ax = plt.subplots()

    ### cumulative ###
    x_bid = df_bid.index.to_numpy()
    y_bid = df_bid.cumulative.to_numpy()
    plt.plot(x_bid, y_bid, color = 'red', label='bid') 
    ax.fill_between(x_bid, y_bid, interpolate=True, color='lightcoral')

    x_ask = df_ask.index.to_numpy()
    y_ask = df_ask.cumulative.to_numpy()
    plt.plot(x_ask, y_ask, color = 'green', label='ask') 
    ax.fill_between(x_ask, y_ask, interpolate=True, color='lightgreen')

    # x = np.concatenate([x1,x2])
    # y = np.concatenate([df_bid.cumulative.to_numpy(), df_ask.cumulative.to_numpy()])
    # plt.plot(x, y, color = 'black', label='cumulative') 
    
    for ex in exchanges:
        x = np.concatenate([df_bid.index[df_bid[ex+'_cum'].notnull()].to_numpy(), df_ask.index[df_ask[ex+'_cum'].notnull()].to_numpy()])
        y = np.concatenate([df_bid[ex+'_cum'][df_bid[ex+'_cum'].notnull()].to_numpy(), df_ask[ex+'_cum'][df_ask[ex+'_cum'].notnull()].to_numpy()])
        plt.plot(x, y, color = colors[ex], label=ex) 
    
    # plt.plot(df.index[df['kraken_cum'].notnull()].values, df['kraken_cum'][df['kraken_cum'].notnull()].values, color = 'yellow', label='kraken') 
    ax.set(xlabel='Price', ylabel='Quantity', title=coin+base+' Orderbook')
    ax.set_xlim(0, 15000)
    ax.set_ylim(0, max(max(y_bid), max(y_ask)))
    ax.ticklabel_format(useOffset=False, style='plain')
    plt.legend()
    plt.show()







### parameters ###
exchanges = ['hitbtc', 'kraken']
coin = 'BTC'
base = 'USD'

side = 'bid'
OB_bid = OrderBooks(exchanges, coin, base, side)
df_bid = OB_bid.combine() 
print(df_bid)

side='ask'
OB_ask = OrderBooks(exchanges, coin, base, side)
df_ask = OB_ask.combine()
print(df_ask)

plot_ob(df_bid, df_ask, exchanges, coin, base)









