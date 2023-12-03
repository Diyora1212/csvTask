import httpx 
from pprint import pprint
import os
import json
import csv
url = "https://jsonplaceholder.typicode.com/users"
response = httpx.get(url=url)
data = response.json()
#os.mkdir("users")
os.chdir('users')
for user in data:
    with open(f"{user['username']}.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerows(f"id: {user['id']}\n")
        writer.writerows(f"username: {user['username']}\n")
        writer.writerows(f"email: {user['email']}\n")
        writer.writerows(f"website: {user['website']}\n")
        writer.writerows(f"company_name: {user['company']['name']}\n")
        
    
    




























