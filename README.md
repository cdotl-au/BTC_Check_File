# BTC_Check_File

(EDUCATIONAL PURPOSES ONLY)

Processes an input file of words or passphrases and converts them to bitcoin wallets addresses and checks for a match in the blockchain wallet text fie containing wallets with balances.

This was coded for a brainwallet where I only had some of the words and using other code which I may upload later I could include the known words and X amount of valid words to append etc.

Steps:

1) Download the latest wallet file [link to follow] containing wallets with a positive balance
2) Run: python TSV_Split.py
   which will split out just the wallet address to "wallets.txt"
3) Run: python BTC_Check_File.txt
   which will process the password / passphrase file.

The program writes to a log every 100 attempts so that you can trim the input file and restart if needed.

TSV_Split
------------------------
This takes the tab seperated wallets file [link to follow] and splits out column 1 into "wallets.txt" this is loaded by the BTC_Check_File.py into a frozen set for searching.

#the TSV input file can be adjusted (TSV Format)
input_file = "bitcoin_addresses_and_balance_LATEST.tsv"

#the output file for the single column with just the wallet address which we know has a balance > 0
output_file = "wallets.txt"

#adjust the row limit which is set to 50M rows
row_limit = 50000000

#adjust the minimum satoshi's 
stop_value = 2000000

So with the above settings includes any wallets with >= 2,000,000 satoshi's (0.2 BTC) in the file "wallets.txt" which is processed by BTC_Check_File.py up to a maximum rows specified by row_limit. 

More notes to follow.
