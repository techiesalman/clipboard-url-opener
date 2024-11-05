import requests

def check_solana_account_type(address):
    # Define Solana JSON RPC endpoint
    url = "https://api.mainnet-beta.solana.com"
    
    # Define the request payload to check account info
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [
            address,
            {"encoding": "jsonParsed"}
        ]
    }
    
    # Send POST request
    response = requests.post(url, json=payload)
    
    # Parse response
    result = response.json()
    
    # Check if result has value or not
    if 'result' in result and result['result']['value'] is not None:
        account_data = result['result']['value']
        
        # Determine if it's a wallet or contract based on executable status
        if account_data['executable']:
            return f"{address} is a Contract Account."
        else:
            return f"{address} is a Wallet Address."
    else:
        return f"Invalid or nonexistent Solana address: {address}"

# Test with provided address
solana_address = "6WyMwEXs2p9Z12PPPzHr4gwHH2euzMmzEXahUdm5pump"
print(check_solana_account_type(solana_address))
