import requests 

url = 'https://safe-transaction-mainnet.safe.global/api/v1/safes/0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8/multisig-transactions/'
r = requests.get(url)
data =  r.json()

wc_tx_all = 0

while True:  
    
    wc_tx_all = wc_tx_all + len([x for x in data['results'] if x['origin'] and "WalletConnect" in x['origin']])     
    
    if data['next'] is None:    
        break
        
    r = requests.get(data['next'])
    data =  r.json()
    
print(f'{wc_tx_all} WalletConnect transactions were made with this Safe') 
