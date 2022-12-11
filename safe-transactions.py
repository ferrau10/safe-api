import requests 

url = 'https://safe-transaction-mainnet.safe.global/api/v1/safes/0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8/multisig-transactions/'
r = requests.get(url)
data =  r.json()
wc_tx_all = 0

while data['next']:  
    
    for x in data['results']:
        if isinstance(x['origin'], str) == True and "WalletConnect" in x['origin']: 
            wc_tx_all += 1
    
        
    r = requests.get(data['next'])
    data =  r.json()
    
print(f'{wc_tx_all} WalletConnect transactions were made with this Safe')
