import requests
import json

accountsUrl = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts"
transactionsUrl = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/5a59028c-e757-4f22-b88c-3ba90573383c/transactions?bookingStatus=booked"

headers = {
  'Accept': 'application/json',
  'X-Request-ID': 'd242a8f5-75ed-41f3-9b6e-391b271d7c27',
  'PSU-IP-Address': '127.0.0.1',
  'Authorization': 'Bearer wEDwRNVEfz4fJPBAagkf',
  'Cookie': 'C0WNET=3ae527be-60f6-4492-a1a9-cf9b7effd197; AMWEBJCT!%2Fmga!JSESSIONID=00001ke4HdBWvE0WvlbHNwHHH5h:938ed943-3c20-4801-ace0-52dd1dd31f86; PD-SESSION-ID=1_4_1_PrEMw6xli6ln-9pAYv0t2cwIxyUc0j7py4BwiMRFP63AJ1wq; PGNET=39c2ba38-60f7-4d02-a1f4-fa8c71680c58; TS01136fc4=0107224bed189fdf7430b7fa6121c4ded3a921cf086561dd7ee1f667942456906565dd17620b582c958fb83decd14c5136bdb36b07; TS018787d1=0107224bedc4464dbc722874d325a58531ff3d98631b8fbb71f303465b34be013aa8967cb5c885645d0559258a440c3f6b3457dade'
}

response = requests.request("GET", transactionsUrl, headers=headers)

parsed = json.loads(response.text)

print(json.dumps(parsed, indent=4, sort_keys=True))