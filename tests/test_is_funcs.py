"""
Testing is-functions of netsubcalc
"""


from netsubcalc import (
    is_ip,
    is_bin_ip,
    is_mask,
    is_bin_mask,
    is_ip_private
)


def test_is_ip() -> None:
    """
        Test netsublib.is_ip function
        :return:
        """
    test_table = [
        {
            "data": "192.168.16.1",
            "expected": True
        },
        {
            "data": "354.764.234.0",
            "expected": False
        },
        {
            "data": "35f.764.234.0",
            "expected": False
        },
        {
            "data": "35f.764.0",
            "expected": False
        },
        {
            "data": "df.sdg.D$!.v",
            "expected": False
        },
        {
            "data": "wfbhibvqewv!#*%&!371t8./\\",
            "expected": False
        },
    ]
    for test_case in test_table:
        assert is_ip(test_case["data"]) == test_case["expected"]


def test_is_bin_ip() -> None:
    """
        Test netsublib.is_bin_ip function
        :return:
        """
    test_table = [
        {'data': '00000000.00000000.00000000.00000000', 'expected': True},
        {'data': '10000000.00000000.00000000.00000000', 'expected': True},
        {'data': '11000000.00000000.00000000.00000000', 'expected': True},
        {'data': '11100000.00000000.00000000.00000000', 'expected': True},
        {'data': '11110000.00000000.00000000.00000000', 'expected': True},
        {'data': '11111000.00000000.00000000.00000000', 'expected': True},
        {'data': '11111100.00000000.00000000.00000000', 'expected': True},
        {'data': '11111110.00000000.00000000.00000000', 'expected': True},
        {'data': '11111111.00000000.00000000.00000000', 'expected': True},
        {'data': '11111111.10000000.00000000.00000000', 'expected': True},
        {'data': '11111111.11000000.00000000.00000000', 'expected': True},
        {'data': '11111111.11100000.00000000.00000000', 'expected': True},
        {'data': '11111111.11110000.00000000.00000000', 'expected': True},
        {'data': '11111111.11111000.00000000.00000000', 'expected': True},
        {'data': '11111111.11111100.00000000.00000000', 'expected': True},
        {'data': '11111111.11111110.00000000.00000000', 'expected': True},
        {'data': '11111111.11111111.00000000.00000000', 'expected': True},
        {'data': '11111111.11111111.10000000.00000000', 'expected': True},
        {'data': '11111111.11111111.11000000.00000000', 'expected': True},
        {'data': '11111111.11111111.11100000.00000000', 'expected': True},
        {'data': '11111111.11111111.11110000.00000000', 'expected': True},
        {'data': '11111111.11111111.11111000.00000000', 'expected': True},
        {'data': '11111111.11111111.11111100.00000000', 'expected': True},
        {'data': '11111111.11111111.11111110.00000000', 'expected': True},
        {'data': '11111111.11111111.11111111.00000000', 'expected': True},
        {'data': '11111111.11111111.11111111.10000000', 'expected': True},
        {'data': '11111111.11111111.11111111.11000000', 'expected': True},
        {'data': '11111111.11111111.11111111.11100000', 'expected': True},
        {'data': '11111111.11111111.11111111.11110000', 'expected': True},
        {'data': '11111111.11111111.11111111.11111000', 'expected': True},
        {'data': '11111111.11111111.11111111.11111100', 'expected': True},
        {'data': '11111111.11111111.11111111.11111110', 'expected': True},
        {'data': '11111111.11111111.11111111.11111111', 'expected': True},
        {'data': '11111111.11111111.11111111.11111111', 'expected': True},
        {'data': '01111111.11111111.11111111.11111111', 'expected': True},
        {'data': '00111111.11111111.11111111.11111111', 'expected': True},
        {'data': '00011111.11111111.11111111.11111111', 'expected': True},
        {'data': '00001111.11111111.11111111.11111111', 'expected': True},
        {'data': '00000111.11111111.11111111.11111111', 'expected': True},
        {'data': '00000011.11111111.11111111.11111111', 'expected': True},
        {'data': '00000001.11111111.11111111.11111111', 'expected': True},
        {'data': '00000000.11111111.11111111.11111111', 'expected': True},
        {'data': '00000000.01111111.11111111.11111111', 'expected': True},
        {'data': '00000000.00111111.11111111.11111111', 'expected': True},
        {'data': '00000000.00011111.11111111.11111111', 'expected': True},
        {'data': '00000000.00001111.11111111.11111111', 'expected': True},
        {'data': '00000000.00000111.11111111.11111111', 'expected': True},
        {'data': '00000000.00000011.11111111.11111111', 'expected': True},
        {'data': '00000000.00000001.11111111.11111111', 'expected': True},
        {'data': '00000000.00000000.11111111.11111111', 'expected': True},
        {'data': '00000000.00000000.01111111.11111111', 'expected': True},
        {'data': '00000000.00000000.00111111.11111111', 'expected': True},
        {'data': '00000000.00000000.00011111.11111111', 'expected': True},
        {'data': '00000000.00000000.00001111.11111111', 'expected': True},
        {'data': '00000000.00000000.00000111.11111111', 'expected': True},
        {'data': '00000000.00000000.00000011.11111111', 'expected': True},
        {'data': '00000000.00000000.00000001.11111111', 'expected': True},
        {'data': '00000000.00000000.00000000.11111111', 'expected': True},
        {'data': '00000000.00000000.00000000.01111111', 'expected': True},
        {'data': '00000000.00000000.00000000.00111111', 'expected': True},
        {'data': '00000000.00000000.00000000.00011111', 'expected': True},
        {'data': '00000000.00000000.00000000.00001111', 'expected': True},
        {'data': '00000000.00000000.00000000.00000111', 'expected': True},
        {'data': '00000000.00000000.00000000.00000011', 'expected': True},
        {'data': '00000000.00000000.00000000.00000001', 'expected': True},
        {'data': '00000000.00000000.00000000.00000000', 'expected': True},
        {'data': 'abcdefgh.ijklmnop.qrstuvwx.yzabcdef', 'expected': False},
        {'data': 'SDgnW@#&@#YT(#NFEAFNDVIBW$', 'expected': False},
    ]
    for test_case in test_table:
        assert is_bin_ip(test_case["data"]) == test_case["expected"]


def test_is_mask() -> None:
    """
        Test netsublib.is_mask function
        :return:
        """
    test_table = [
        {
            "data": "255.0.0.0",
            "expected": True
        },
        {
            "data": "255.255.0.0",
            "expected": True
        },
        {
            "data": "255.255.255.0",
            "expected": True
        },
        {
            "data": "255.240.0.0",
            "expected": True
        },
        {
            "data": "192.168.16.1",
            "expected": False
        },
        {
            "data": "255.255.4.0",
            "expected": False
        },
        {
            "data": "35f.764.234.0",
            "expected": False
        },
        {
            "data": "df.sdg.D$!.v",
            "expected": False
        },
        {
            "data": "wfbhibvqewv!#*%&!371t8./\\",
            "expected": False
        },
    ]
    for test_case in test_table:
        assert is_mask(test_case["data"]) == test_case["expected"]


def test_is_bin_mask() -> None:
    """
        Test netsublib.is_bin_mask function
        :return:
        """
    test_table = [
        {'data': '00000000.00000000.00000000.00000000', 'expected': False},
        {'data': '10000000.00000000.00000000.00000000', 'expected': True},
        {'data': '11000000.00000000.00000000.00000000', 'expected': True},
        {'data': '11100000.00000000.00000000.00000000', 'expected': True},
        {'data': '11110000.00000000.00000000.00000000', 'expected': True},
        {'data': '11111000.00000000.00000000.00000000', 'expected': True},
        {'data': '11111100.00000000.00000000.00000000', 'expected': True},
        {'data': '11111110.00000000.00000000.00000000', 'expected': True},
        {'data': '11111111.00000000.00000000.00000000', 'expected': True},
        {'data': '11111111.10000000.00000000.00000000', 'expected': True},
        {'data': '11111111.11000000.00000000.00000000', 'expected': True},
        {'data': '11111111.11100000.00000000.00000000', 'expected': True},
        {'data': '11111111.11110000.00000000.00000000', 'expected': True},
        {'data': '11111111.11111000.00000000.00000000', 'expected': True},
        {'data': '11111111.11111100.00000000.00000000', 'expected': True},
        {'data': '11111111.11111110.00000000.00000000', 'expected': True},
        {'data': '11111111.11111111.00000000.00000000', 'expected': True},
        {'data': '11111111.11111111.10000000.00000000', 'expected': True},
        {'data': '11111111.11111111.11000000.00000000', 'expected': True},
        {'data': '11111111.11111111.11100000.00000000', 'expected': True},
        {'data': '11111111.11111111.11110000.00000000', 'expected': True},
        {'data': '11111111.11111111.11111000.00000000', 'expected': True},
        {'data': '11111111.11111111.11111100.00000000', 'expected': True},
        {'data': '11111111.11111111.11111110.00000000', 'expected': True},
        {'data': '11111111.11111111.11111111.00000000', 'expected': True},
        {'data': '11111111.11111111.11111111.10000000', 'expected': True},
        {'data': '11111111.11111111.11111111.11000000', 'expected': True},
        {'data': '11111111.11111111.11111111.11100000', 'expected': True},
        {'data': '11111111.11111111.11111111.11110000', 'expected': True},
        {'data': '11111111.11111111.11111111.11111000', 'expected': True},
        {'data': '11111111.11111111.11111111.11111100', 'expected': True},
        {'data': '11111111.11111111.11111111.11111110', 'expected': True},
        {'data': '11111111.11111111.11111111.11111111', 'expected': True},
        {'data': '01111111.11111111.11111111.11111111', 'expected': False},
        {'data': '00111111.11111111.11111111.11111111', 'expected': False},
        {'data': '00011111.11111111.11111111.11111111', 'expected': False},
        {'data': '00001111.11111111.11111111.11111111', 'expected': False},
        {'data': '00000111.11111111.11111111.11111111', 'expected': False},
        {'data': '00000011.11111111.11111111.11111111', 'expected': False},
        {'data': '00000001.11111111.11111111.11111111', 'expected': False},
        {'data': '00000000.11111111.11111111.11111111', 'expected': False},
        {'data': '00000000.01111111.11111111.11111111', 'expected': False},
        {'data': '00000000.00111111.11111111.11111111', 'expected': False},
        {'data': '00000000.00011111.11111111.11111111', 'expected': False},
        {'data': '00000000.00001111.11111111.11111111', 'expected': False},
        {'data': '00000000.00000111.11111111.11111111', 'expected': False},
        {'data': '00000000.00000011.11111111.11111111', 'expected': False},
        {'data': '00000000.00000001.11111111.11111111', 'expected': False},
        {'data': '00000000.00000000.11111111.11111111', 'expected': False},
        {'data': '00000000.00000000.01111111.11111111', 'expected': False},
        {'data': '00000000.00000000.00111111.11111111', 'expected': False},
        {'data': '00000000.00000000.00011111.11111111', 'expected': False},
        {'data': '00000000.00000000.00001111.11111111', 'expected': False},
        {'data': '00000000.00000000.00000111.11111111', 'expected': False},
        {'data': '00000000.00000000.00000011.11111111', 'expected': False},
        {'data': '00000000.00000000.00000001.11111111', 'expected': False},
        {'data': '00000000.00000000.00000000.11111111', 'expected': False},
        {'data': '00000000.00000000.00000000.01111111', 'expected': False},
        {'data': '00000000.00000000.00000000.00111111', 'expected': False},
        {'data': '00000000.00000000.00000000.00011111', 'expected': False},
        {'data': '00000000.00000000.00000000.00001111', 'expected': False},
        {'data': '00000000.00000000.00000000.00000111', 'expected': False},
        {'data': '00000000.00000000.00000000.00000011', 'expected': False},
        {'data': '00000000.00000000.00000000.00000001', 'expected': False},
        {'data': 'abcdefgh.ijklmnop.qrstuvwx.yzabcdef', 'expected': False},
        {'data': 'SDgnW@#&@#YT(#NFEAFNDVIBW$', 'expected': False},
    ]
    for test_case in test_table:
        assert is_bin_mask(test_case["data"]) == test_case["expected"]


def test_is_ip_private() -> None:
    """
        Test netsublib.is_ip_private function
        :return:
        """
    test_table = [
        {'data': '10.0.0.1', 'expected': True},
        {'data': '10.0.0.1', 'expected': True},
        {'data': '172.17.2.1', 'expected': True},
        {'data': '192.168.12.2', 'expected': True},
        {'data': '56.174.32.1', 'expected': False},
        {'data': 'abcdefgh.ijklmnop.qrstuvwx.yzabcdef', 'expected': None},
        {'data': 'SDgnW@#&@#YT(#NFEAFNDVIBW$', 'expected': None},
    ]
    for test_case in test_table:
        assert is_ip_private(test_case["data"]) == test_case["expected"]
