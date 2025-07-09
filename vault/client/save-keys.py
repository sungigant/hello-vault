from gettext import install
import hvac
import time
import os

VAULT_ADDR = os.environ.get("VAULT_ADDR", "http://vault:8200")
VAULT_TOKEN = os.environ.get("VAULT_TOKEN", "root")

# Wait for Vault to be ready
for _ in range(10):
    try:
        client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
        if client.is_authenticated():
            break
    except Exception:
        time.sleep(2)
else:
    print("Vault not ready")
    exit(1)

client.secrets.kv.v2.create_or_update_secret(
    path='creds',
    secret={'username': 'sparkuser', 'password': 'sparkpass'},
)
print("Secret stored in Vault.")
exit(0)