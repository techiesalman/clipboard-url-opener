import time
import pyperclip
import re
import webbrowser

def is_valid_wallet_address(address):
    # Adjust regex to accommodate Solana wallet addresses (Base58 encoded, 32-44 characters)
    pattern = re.compile(r'^[A-HJ-NP-Za-km-z1-9]{32,44}$')
    return bool(pattern.match(address))

def main():
    last_clipboard_content = ""

    while True:
        clipboard_content = pyperclip.paste().strip()

        if clipboard_content != last_clipboard_content:
            last_clipboard_content = clipboard_content
            print(f"Clipboard content changed: {clipboard_content}")

            if is_valid_wallet_address(clipboard_content):
                print(f"Valid wallet address detected: {clipboard_content}")
                
                dexcheck_url = f"https://dexcheck.ai/app/wallet-analyzer/{clipboard_content}"
                solscan_url = f"https://solscan.io/account/{clipboard_content}#balanceChanges"
                
                print(f"Opening URL: {dexcheck_url}")
                webbrowser.open(dexcheck_url)  # Opens the Dexcheck URL in the default browser
                
                print(f"Opening URL: {solscan_url}")
                webbrowser.open(solscan_url)  # Opens the Solscan URL in the default browser
            else:
                print("Invalid wallet address")

        time.sleep(1)  # Check the clipboard every second

if __name__ == "__main__":
    main()
