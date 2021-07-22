import requests
import json

accountsURL = "https://sandbox.handelsbanken.com/openbanking/psd2/v2/accounts"
transactionsURL = "https://sandbox.handelsbanken.com/openbanking/psd2/v2/accounts/ae58d1e0-6cf3-11e9-9c41-e957ce7d7d69/transactions"

headers = {
    'Authorization': 'Bearer MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3',
    'PSU-IP-Address': '192.102.28.2',
    'TPP-Request-ID': 'c8271b81-4229-5a1f-bf9c-758f11c1f5b1',
    'TPP-Transaction-ID': '6b24ce42-237f-4303-a917-cf778e5013d6',
    'X-IBM-Client-Id': 'fe68d141-f1ac-4078-ac15-a99a17ef1816',
    'Accept': 'application/json'
}

response = requests.request("GET", transactionsURL, headers=headers)

parsed = json.loads(response.text)

print(json.dumps(parsed, indent=4, sort_keys=True))