#!/bin/sh
# Start Vault in the background
vault server -dev -dev-root-token-id=root &
sleep 5
# Keep the container running
tail -f /dev/null