BTC_Check_File

(For Educational Use Only)

Overview:
This program processes a file containing words or passphrases and transforms them into Bitcoin wallet addresses. It then compares these addresses against a blockchain wallet file with existing balances to identify any matches. Primarily, it's designed for recovering brainwallets when only partial information is available. Additional scripts can be used in conjunction with this tool to refine the recovery process.

Instructions:

1. **Obtain Wallet File**: Download the most recent wallet file (link forthcoming) that contains wallet addresses with a positive balance.

2. **Prepare Wallet Addresses**:
   - Execute: `python TSV_Split.py`
   - This script will extract the wallet addresses from the downloaded file and save them to `wallets.txt`.

3. **Process Passphrases**:
   - Execute: `python BTC_Check_File.py`
   - This script processes the file `passphrases.txt`, which should contain passwords or passphrases, one per line.

Features:
- The script logs its progress every 100 attempts, enabling the user to refine the input file and restart if necessary.
- Upon processing `passphrases.txt`, each line is converted into a Bitcoin wallet address. The program then checks for matches against a frozen set of wallet addresses with known balances.

File Adjustments:
- Users can modify `passphrases.txt` as needed, ensuring there is one password or passphrase per line.

Match Found:
- If a match is detected, a sound alert (`success.wav`) will play ten times.
- A file named `win.txt` is generated, containing the mnemonic, the five derived Bitcoin wallet addresses, and the corresponding WIF uncompressed and compressed keys for importing into a Bitcoin wallet, along with the private key.

Testing:
- To verify the functionality, users can add a known wallet address to `wallets.txt`.

TSV_Split Script:
- This script processes a tab-separated wallet file (link forthcoming), extracting the first column into `wallets.txt`.
- The file `bitcoin_addresses_and_balance_LATEST.tsv` can be modified as needed.
- Users can adjust the row limit (default set to 50 million rows) and the minimum satoshi value (default set to 2,000,000 satoshis, or 0.02 BTC).
- Therefore, `wallets.txt` will include any wallet addresses with balances equal to or greater than 2,000,000 satoshis, up to the specified row limit.

Sample Files:
- `wallets.txt`: A sample file containing the top 1000 Bitcoin wallets as of April 2nd, 2024.
- `passphrases.txt`: A sample file with the top 1000 lines from `rockyou.txt`.
