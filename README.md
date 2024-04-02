# BTC_Check_File

(EDUCATIONAL PURPOSES ONLY)

Processes an input file of words or passphrases and converts them to bitcoin wallets addresses and checks for a match in the blockchain wallet text fie containing wallets with balances.

This was coded for a brainwallet where I only had some of the words and using other code which I may upload later I could include the known words and X amount of valid words to include and test with.

Steps:

1) Download the latest wallet file [link to follow] containing wallets with a positive balance
   
2) Run: python TSV_Split.py
   This will split out just the wallet address to "wallets.txt"

3) Run: python BTC_Check_File.py
   This will process the password / passphrase file: "passphrases.txt"

The program writes to a log every 100 attempts so that you can trim the input file and restart if needed.

BTC_Check_File
------------------------

Processes "passphrases.txt" converting each line to a bitcoin wallet address and check for a match in the frozen set which contains wallets with a balance.

You can adjust the "passphrases.txt" file to anything you like as long as there an password/passphrase per line.

If a match is found success.wav will play 10 times and a file called "win.txt" will be written out and the program will stop.  "win.txt" will have the mneumonic and the 5 bitcoin wallets that were derived and the the WIF uncompressed and compressed to use to import into your bitcoin wallet as well as the private key.

You can test the whole process by grabbing a wallet output and putting in the wallets.txt file.

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

wallets.txt
-------------------------
The sample wallets.txt is the top 1000 bitcoin wallets as of the 2nd April 2024.

passphrases.txt
-------------------------
The sample passphrases.txt is the top 1000 lines from rockyou.txt

More notes to follow.
