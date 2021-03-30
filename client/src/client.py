from helpers import get_credentials
from binance.client import Client
import json
import os
import time

# Initialize environment variables
env = os.environ

# Read credentials and initialize Client instance
credentials = get_credentials("credentials/fbltr.json")
client = Client(credentials["api_key"], credentials["api_secret"])

# Get all exchange info
info = client.get_exchange_info()

# Save in the output file
with open(env["OUTPUT_FILE"], "w", encoding='utf-8') as f:
    json.dump(info, f, ensure_ascii=False, indent=4)

print("Info saved!")

while True:
    print("sleeping...")
    time.sleep(5)
