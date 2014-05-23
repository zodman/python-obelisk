import obelisk
import os, sys

from twisted.internet import reactor

from obelisk.util import to_btc
from obelisk import MAX_UINT32

if __name__ == '__main__':
    c = obelisk.ObeliskOfLightClient("tcp://obelisk.unsystem.net:9091")
    tx = "0100000001991b71e521cef46662b284eb59d93f88e4d236a39748e53918d329f0501c549a010000006a47304402203bfca328f41239f9612caa8d83078712dc4a42be450af82593f477feb7660eee02207c969813a6719322990501a1976e3e8cc092e89079a0b7a0b69835093175dba6012102db459ed89d9bd5d91cad525594849f19263a13d3e937f2243d223ccead2f8f3cffffffff0200ca9a3b000000001976a91499a81f84f221206e0d0ec549997a20e28285348788ac9090dea91a0000001976a91473912b81bf654a1d43499e0dcf8a5ad4ff067b2f88ac00000000"
    def cb(*args):
        ec, result = args
        print result.encode("hex")
        reactor.stop()
    c.validate_transaction(tx.decode("hex"), cb)

    reactor.run()
