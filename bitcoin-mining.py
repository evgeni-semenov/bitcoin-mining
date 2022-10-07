#!/usr/bin/env python3
'''
This is a bitcoin mining process simulator.

This simulation is, of course, oversimplified, but you will get a general idea. 
Normally each bitcoin block includes:
- a hash value of previous block (to verify integrity of the blockchain and all the previous transactions)
- transactions included in the block
- a random numeric nonce value

Miners form the blocks and try different nonce values to solve the hash puzzle = find a hash value that matches the criteria.
In Bitcoin network this criteria is simply a N amount of prefix zeros. 

You can experiment with adjusting network_difficulty (although I don't recommend to go above 7-8), and modifying the 
transactions to see how it affects the mining time.

Created by Evgeni Semenov, dev@safemail.sbs
'''
from time import time
from hashlib import sha256

max_nonce = 100000000000 #max nonce value
network_difficulty = 7 #set bitcoin network difficulty (amount of prefix zeros)
transactions = "Pete -> John 50 BTC" #you can modify this string as well
prev_block_hash = '0000008fd16ac7984995098fdfdd5a705154773b18aa207ce92dd68b0a81fadf'

def sha256_encode(block):
    return sha256(block.encode('utf-8')).hexdigest()

def mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros):
    prefix_string = '0'*prefix_zeros

    for nonce in range (max_nonce):
        block = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = sha256_encode(block)

        if new_hash.startswith(prefix_string):
            print("[+++] Yahoo! I have mined some bitcoin with nonce value: "+str(nonce))
            return new_hash

    raise BaseException("[-] Could not find matching hash. Tried "+max_nonce+" times.")

if __name__ == "__main__":
    start_time = time()
    print("[+] Mining started ...")
    next_block_hash = mine_bitcoin(14354, transactions, prev_block_hash, network_difficulty)
    elapsed_time = str(time() - start_time)
    print("... mining ended. Time consumed: "+elapsed_time+" seconds.")
    print("New hash: "+next_block_hash)