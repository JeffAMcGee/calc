import operator
import unittest
from StringIO import StringIO

from mock import patch

import calc


class TestCalc(unittest.TestCase):

    def test_tokenize(self):
        res = calc.tokenize('3+4')
        self.assertEqual(res,[3,operator.add,4])

    def test_eval_tokens(self):
        res = calc.eval_tokens([3,operator.add,4])
        self.assertEqual(res,7)
        # 3-1+2==4
        res2 = calc.eval_tokens([3,operator.sub,1,operator.add,2])
        self.assertEqual(res2,4)

    def test_main(self):
        # Monkey patch raw_input and stdout using the mock library
        with patch('__builtin__.raw_input') as raw_inp:
            with patch('sys.stdout', new_callable=StringIO) as stdout:
                raw_inp.return_value = '2+3\n'
                calc.main()
                self.assertEqual(stdout.getvalue(),'5\n')


if __name__ == '__main__':
    unittest.main()
