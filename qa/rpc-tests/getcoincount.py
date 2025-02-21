#!/usr/bin/env python3
# Copyright (c) 2024 The Bonkcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import *


class GetCoinCountTest(BitcoinTestFramework):

    def __init__(self):
        super().__init__()
        self.setup_clean_chain = True
        self.num_nodes = 1

    def setup_network(self, split=False):
        self.nodes = start_nodes(self.num_nodes, self.options.tmpdir)
        self.is_network_split=False

    def run_test(self):
        print("Mining blocks...")
        node = self.nodes[0]
        node.generate(1)

        result = node.getcoincount()
        assert_equal(result, 1 * 500000)

        # 100000 and 100001 was use on pepe/doge because they used 10k block halving method while we use 50k block halving method
        # 50000 is number of block produce per halving
        # 50001 is the halving start block
        result = node.getcoincount(50001)
        assert_equal(result, (50000 * 500000) + (1 * 250000))

        result = node.getcoincount(100001)
        assert_equal(result, (50000 * 500000) + (50000 * 250000) + (1 * 125000))

        result = node.getcoincount(150001)
        assert_equal(result, (50000 * 500000) + (50000 * 250000) + (50000 * 125000) + (1 * 62500))

        result = node.getcoincount(200001)
        assert_equal(result, (50000 * 500000) + (50000 * 250000) + (50000 * 125000) + (50000 * 62500) + (1 * 31250))

        result = node.getcoincount(250001)
        assert_equal(result, (50000 * 500000) + (50000 * 250000) + (50000 * 125000)
                           + (50000 *  62500) + (50000 *  31250) + (1     *  15625))

        result = node.getcoincount(300001)
        assert_equal(result, (50000 * 500000) + (50000 * 250000) + (50000 * 125000)
                           + (50000 *  62500) + (50000 *  31250) + (50000 *  15625) + (1 * 10000))

        result = node.getcoincount(1000001)
        assert_equal(result, (50000 * 500000) + (50000 * 250000) + (50000 * 125000)
                           + (50000 *  62500) + (50000 *  31250) + (50000 *  15625) + (700001 * 10000))

if __name__ == '__main__':
    GetCoinCountTest().main()
