import unittest
import chillparse as cp 


class TestCP(unittest.TestCase):

    def test_chillparse(self):
        self.assertEqual( cp.chillparse('version'), ('in', 'version', 0, 'V 5.11'))
        self.assertEqual( cp.chillparse('status'), ('in', 'status', 0, 5))
        self.assertEqual( cp.chillparse('in_pv_00'), ('in', 'pv', 0, ''))
        self.assertEqual( cp.chillparse('out_sp_00 58.7'), ('out', 'sp', 0, '58.7'))
        self.assertEqual( cp.chillparse('out_mode_01 2'), ('out', 'mode', 1, '2'))

if __name__ == '__main__':
    unittest.main()
    