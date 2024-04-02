# BTC_Check_File
Process an input file of words or passphrases and converts them to bitcoin wallets addresses and checks for a match in the blockchain wallet text fie containing wallets with balances.

Steps:

1) Download the latest wallet file [link to follow] containing wallets with a positive balance
2) Run: python TSV_Split.py
   which will split out just the wallet address to "wallets.txt"
3) Run: python BTC_Check_File.txt
   which will process the password / passphrase file.

The program writes to a log every 100 attempts so that you can trim the input file and restart if needed.

More notes to follow.
