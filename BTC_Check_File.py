import winsound
import time

from bitcoin import sha256, privtopub, pubtoaddr
from bitcoinaddress import Wallet

iAttempts = 0
bFound = False

import datetime

def write_log(log_message, file_name='log.txt'):

    #Get current date and time
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%d-%m-%Y %H:%M:%S')

    #Construct the log message
    full_message = f"{formatted_time} - {log_message}\n"

    #Write to the log file
    with open(file_name, 'a') as file:
        file.write(full_message)

    #print(f"Log entry added: {full_message}")

def IsFound(mnemonic):

    global iAttempts

    #print(f"Mnemonic: {mnemonic}")

    private_key = sha256(mnemonic)

    wallet = Wallet(private_key)
    #print(wallet)

    btc_address = wallet.address.mainnet.pubaddr1
    btc_addressc = wallet.address.mainnet.pubaddr1c
    btc_address3 = wallet.address.mainnet.pubaddr3
    btc_address4 = wallet.address.mainnet.pubaddrbc1_P2WPKH
    btc_address5 = wallet.address.mainnet.pubaddrbc1_P2WSH

    if iAttempts % 100 == 0:
        #print(iAttempts, btc_address, btc_addressc, btc_address3, btc_address4, btc_address5, mnemonic)
        
        tmp = f"{iAttempts:,} {mnemonic}"
        print(tmp)
        write_log(tmp)

    if btc_address in publist or btc_addressc in publist or btc_address3 in publist or btc_address4 in publist or btc_address5 in publist:

        log_message = f"Mnemonic: {mnemonic}\nAddress: {btc_address}\nAddress Compressed: {btc_addressc}\n Address 3: {btc_address3}\n Address 4: {btc_address4}\n Address 5: {btc_address5}\nPrivate Key WIF: {wallet.key.mainnet.wif}\nPrivate Key WIF Compressed: {wallet.key.mainnet.wifc}"

        with open('win.txt', 'a') as file:
            file.write(log_message + '\n')

        print(f"Found {btc_address} {btc_addressc}")

        return True
    else:

        #print(f"Not Found {btc_address} {btc_addressc}")
        return False

def Test(mnemonic):
    private_key = sha256(mnemonic)
    wallet = Wallet(private_key)
    print(f"Bitcoin Address: {wallet.address.mainnet.pubaddr1}")
    print(f"Bitcoin Address Compressed: {wallet.address.mainnet.pubaddr1c}")
    print(f"Private Key WIF: {wallet.key.mainnet.wif}")
    print(f"Private Key WIF Compressed: {wallet.key.mainnet.wifc}")
    return

def myFound():
    global bFound
    bFound = True
    for i in range(10):
        winsound.PlaySound('success.wav', winsound.SND_FILENAME)
        time.sleep(3)  # Sleeps for 3 seconds

##########################################################################################

#addresses_filename = "bitcoin_addresses_and_balance_LATEST.tsv"
addresses_filename = "wallets.txt"

winsound.PlaySound('success.wav', winsound.SND_FILENAME)

print("BTC")
print(f'Loading "{addresses_filename}"...')

with open(addresses_filename) as f:
    #publist = frozenset(line.strip().split('\t')[0] for line in f) #use this if you want to load the whole tsv and not a subset
    publist = frozenset(line.strip() for line in f)

print("Loaded.")
iTotalLines = len(publist)
print(f'Length: {iTotalLines}')

iLines = 0

replace_chars = ['_', '!', '*', '$']  #Characters to replace spaces with

with open('passphrases.txt', 'r', encoding='utf-8', errors='replace') as file:
    for line in file:
        try:
            original_line = line.strip()
            variants = [original_line]

            # Add lower, upper, and title case variants
            for case_function in [str.lower, str.upper, str.title]:
                case_variant = case_function(original_line)
                if case_variant != original_line:
                    variants.append(case_variant)
    
            # Variants without spaces and with space replaced by each character in replace_chars
            for replace_char in [''] + replace_chars:  # Include empty string to remove spaces
                replaced_line = original_line.replace(' ', replace_char)
                if replaced_line != original_line:
                    variants.append(replaced_line)
    
                    # Add lower, upper, and title case variants of the replaced line
                    for case_function in [str.lower, str.upper, str.title]:
                        case_variant = case_function(replaced_line)
                        if case_variant not in variants:  # Avoid duplicates
                            variants.append(case_variant)
    
            # Check each variant
            for variant in variants:
                iAttempts += 1
                if IsFound(variant):
                    myFound()
                    break
    
            iLines += 1  # Only increment if no match was found

        except Exception as e:
            print(f"Error processing line: {e}")
            continue
        
if bFound:
    print("Winner Winner Chicken Dinner!")
else:
    print("Better luck next time!")

print(f"Attempts: {iAttempts} for {iLines} lines")
