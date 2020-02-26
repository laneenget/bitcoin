import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitcoin(TestCase):

    @patch('bitcoin.request_bitcoin_rate')
    def test_request(self, mock_rates):
        mock_rate = 10.25
        api_response = {'bpi': 'USD', 'float_rate': mock_rate}
        mock_rates.side_effect = api_response
        converted = bitcoin.do_math(10, mock_rate)
        self.assertEqual(102.5, converted)

if __name__ == '__main__':
    unittest.main()