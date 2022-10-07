# bitcoin-mining
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

Evgeni Semenov, dev@safemail.sbs