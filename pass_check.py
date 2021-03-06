import requests
import hashlib
import sys

def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/'+query_char
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Error fetching:{res.status_code},')
    return res

def get_pass_leaks_count(hashes,hash_to_check):
    
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    #check password if it exits in api response
    sha1password=hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char,tail=sha1password[:5],sha1password[5:]
    response=request_api_data(first5char) # using first 5 char of hash
    return get_pass_leaks_count(response,tail)

def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should change your password!')
        else:
            print(f"{password} is secure carry on")    
try:
    inputs=input(sys.argv[1:])
except:
    print('Enter argument before proceeding')
    sys.exit(1)
main(inputs) # pass from cli