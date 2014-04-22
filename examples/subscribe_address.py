import obelisk
import obelisk.bitcoin
import pprint
from twisted.internet import reactor

####################################################
# Testing Code

def print_event(*args):
    address_version, address_hash, height, block_hash, tx = args
    address = obelisk.bitcoin.hash_160_to_bc_address(address_hash, address_version)
    print "update for", address, height
    print "tx: ", tx.encode("hex")
    print "block: ", block_hash, block_hash.encode("hex")
    t = obelisk.bitcoin.Transaction(tx.encode("hex"))
    print t.hash()
    pprint.pprint(t.deserialize())

if __name__ == '__main__':
    c = obelisk.ObeliskOfLightClient('tcp://obelisk-testnet.airbitz.co:9091')
    c.subscribe_address("mypM96wu5GNp3GKQVZNbNjHszaw3vkyb6t", print_event)

    reactor.run()


