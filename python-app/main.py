import hvac
import os
import time

VAULT_ADDR = os.environ.get("VAULT_ADDR", "http://vault:8200")
VAULT_TOKEN = os.environ.get("VAULT_TOKEN", "root")

# Wait for Vault to be ready
authenticated = False
for _ in range(10):
  try:
    client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
    if client.is_authenticated():
      authenticated = True
      break
  except Exception:
    time.sleep(2)

if not authenticated:
  print("Vault not ready")
  exit(1)

secret = client.secrets.kv.v2.read_secret_version(path='creds')
creds = secret['data']['data']

print(f"Fetched creds from Vault: {creds}")