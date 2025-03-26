import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        block_data = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_data).hexdigest()
    
    def mine_block(self, difficulty):
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, 'Genesis Block', '0')
        self.chain.append(genesis_block)
    
    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
    
    def tamper_with_block(self, index, new_data):
        if 0 < index < len(self.chain):
            self.chain[index].transactions = new_data
            self.chain[index].hash = self.chain[index].compute_hash()

    def print_chain(self):
        for block in self.chain:
            print(vars(block))

# Demo
blockchain = Blockchain()
blockchain.add_block(["Alice pays Bob 10 BTC"])
blockchain.add_block(["Bob pays Charlie 5 BTC"])
print("Original Blockchain:")
blockchain.print_chain()

print("\nTampering with the second block...")
blockchain.tamper_with_block(1, ["Alice pays Bob 100 BTC"])
print("Updated Blockchain:")
blockchain.print_chain()

print("\nIs blockchain valid?", blockchain.is_chain_valid())
