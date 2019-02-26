import hashlib as hasher
import datetime as date


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce, self.hash = self.hash_miner()

    def hash_miner(self, difficulty="0000"):
        nonce = 0
        while True:
            hash = self.hash_block(nonce)
            if hash.startswith(difficulty):
                return [nonce, hash]
            else:
                nonce += 1

    def hash_block(self, nonce=0):
        sha = hasher.sha256()
        sha.update(str(nonce).encode("utf-8") +
                   str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


def genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = input('Enter your data: ')
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


blockchain = [genesis_block()]
previous_block = blockchain[0]

blocks = 2

for i in range(0, blocks):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("\nBlock #{} was mined successfully".format(block_to_add.index))
    print("Previous Hash: {}".format(block_to_add.previous_hash))
    print("Hash: {}".format(block_to_add.hash))
    print("Date and Time: {}".format(block_to_add.timestamp))
    print("Nonce: {}\n".format(block_to_add.nonce))