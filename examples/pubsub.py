from twisted.internet import reactor

import obelisk

####################################################
# Class to receive pubsub callbacks
#
# When you pass the block and tx addresses in the client constructor
# the base class automatically calls 'on_raw_block' and 'on_raw_transaction'
# callbacks when notifications arrive.
#
# If you prefer to pass your own callbacks, don't pass the addresses to
# the constructor, and call 'setup_block_sub' and/or 
# 'setup_transaction_sub' yourself.

class ObeliskPubSubClient(obelisk.ObeliskOfLightClient):
    def on_raw_block(self, height, hash, header, tx_num, tx_hashes):
        print "* block", height, len(tx_hashes)

    def on_raw_transaction(self, hash, transaction):
        tx = obelisk.serialize.deser_tx(transaction)
        outputs = []
        for output in tx.outputs:
            outputs.append(obelisk.util.format_satoshis(output.value))
        print "* tx", hash.encode('hex'), ", ".join(outputs)
        


if __name__ == '__main__':
    args = (
            'tcp://85.25.198.97:9091', 'tcp://85.25.198.97:9093', 'tcp://85.25.198.97:9094',
        )
    c = ObeliskPubSubClient(*args)
    reactor.run()


