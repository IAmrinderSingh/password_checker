import requests
import hashlib
import sys

def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/'+query_char
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Error fetching:{res.status_code},')
    return res