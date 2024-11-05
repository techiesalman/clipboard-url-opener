# import time
# import pyperclip
# import re
# import webbrowser

# def is_valid_wallet_address(address):
#     # Adjust regex to accommodate Solana wallet addresses (Base58 encoded, 32-44 characters)
#     pattern = re.compile(r'^[A-HJ-NP-Za-km-z1-9]{32,44}$')
#     return bool(pattern.match(address))

# def main():
#     last_clipboard_content = ""

#     while True:
#         clipboard_content = pyperclip.paste().strip()

#         if clipboard_content != last_clipboard_content:
#             last_clipboard_content = clipboard_content
#             print(f"Clipboard content changed: {clipboard_content}")

#             if is_valid_wallet_address(clipboard_content):
#                 print(f"Valid wallet address detected: {clipboard_content}")
                
#                 dexcheck_url = f"https://dexcheck.ai/app/wallet-analyzer/{clipboard_content}"
#                 solscan_url = f"https://solscan.io/account/{clipboard_content}#balanceChanges"
#                 cielo_url = f"https://app.cielo.finance/profile/{clipboard_content}/pnl/tokens?timeframe=30d"
#                 gmgn_url = f"https://gmgn.ai/sol/address/{clipboard_content}"

#                 # print(f"Opening URL: {dexcheck_url}")
#                 # webbrowser.open(dexcheck_url)  # Opens the Dexcheck URL in the default browser

#                 # print(f"Opening URL: {cielo_url}")
#                 # webbrowser.open(cielo_url)

#                 # print(f"Opening URL: {solscan_url}")
#                 # webbrowser.open(solscan_url)  # Opens the Solscan URL in the default browser

#                 print(f"Opening URL: {gmgn_url}")
#                 webbrowser.open(gmgn_url)

#             else:
#                 print("Invalid wallet address")

#         time.sleep(1)  # Check the clipboard every second

# if __name__ == "__main__":
#     main()
    
import time
import pyperclip
import re
import webbrowser
import json

def is_valid_wallet_address(address):
    pattern = re.compile(r'^[A-HJ-NP-Za-km-z1-9]{32,44}$')
    return bool(pattern.match(address))

def load_opened_addresses(filename="opened_wallets.json"):
    try:
        with open(filename, "r") as file:
            data = file.read().strip()
            if not data:
                return set()
            return set(json.loads(data))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()

def save_opened_addresses(addresses, filename="opened_wallets.json"):
    with open(filename, "w") as file:
        json.dump(list(addresses), file)

def main():
    last_clipboard_content = ""
    opened_addresses = load_opened_addresses()  # Load previously opened addresses
    
    # Toggle to control duplicate opening behavior
    # ignore_duplicates = True  # Set to True to skip duplicates, False to open duplicates
    ignore_duplicates = False  # Set to True to skip duplicates, False to open duplicates

    while True:
        clipboard_content = pyperclip.paste().strip()

        if clipboard_content != last_clipboard_content:
            last_clipboard_content = clipboard_content
            print(f"Clipboard content changed: {clipboard_content}")

            if is_valid_wallet_address(clipboard_content):
                if ignore_duplicates and clipboard_content in opened_addresses:
                    print("Address already opened, skipping.")
                else:
                    print(f"Valid wallet address detected: {clipboard_content}")
                    
                    gmgn_url = f"https://gmgn.ai/sol/address/{clipboard_content}"
                    print(f"Opening URL: {gmgn_url}")
                    webbrowser.open(gmgn_url)

                    if ignore_duplicates:
                        opened_addresses.add(clipboard_content)  # Add to opened list if ignoring duplicates
                        save_opened_addresses(opened_addresses)  # Save the updated list

            else:
                print("Invalid wallet address")

        time.sleep(1)

if __name__ == "__main__":
    main()
