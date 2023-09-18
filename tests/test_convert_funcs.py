"""
Testing convert functions of netsubcalc
"""

import netsubcalc as nsc


def test_ip2bin():
    """
    Test netsublib.ip2bin function
    :return:
    """

    test_table = [
        {'data': '255.255.255.255', 'expected': '11111111.11111111.11111111.11111111'},
        {'data': '127.255.255.255', 'expected': '01111111.11111111.11111111.11111111'},
        {'data': '63.255.255.255', 'expected': '00111111.11111111.11111111.11111111'},
        {'data': '31.255.255.255', 'expected': '00011111.11111111.11111111.11111111'},
        {'data': '15.255.255.255', 'expected': '00001111.11111111.11111111.11111111'},
        {'data': '7.255.255.255', 'expected': '00000111.11111111.11111111.11111111'},
        {'data': '3.255.255.255', 'expected': '00000011.11111111.11111111.11111111'},
        {'data': '1.255.255.255', 'expected': '00000001.11111111.11111111.11111111'},
        {'data': '0.255.255.255', 'expected': '00000000.11111111.11111111.11111111'},
        {'data': '0.127.255.255', 'expected': '00000000.01111111.11111111.11111111'},
        {'data': '0.63.255.255', 'expected': '00000000.00111111.11111111.11111111'},
        {'data': '0.31.255.255', 'expected': '00000000.00011111.11111111.11111111'},
        {'data': '0.15.255.255', 'expected': '00000000.00001111.11111111.11111111'},
        {'data': '0.7.255.255', 'expected': '00000000.00000111.11111111.11111111'},
        {'data': '0.3.255.255', 'expected': '00000000.00000011.11111111.11111111'},
        {'data': '0.1.255.255', 'expected': '00000000.00000001.11111111.11111111'},
        {'data': '0.0.255.255', 'expected': '00000000.00000000.11111111.11111111'},
        {'data': '0.0.127.255', 'expected': '00000000.00000000.01111111.11111111'},
        {'data': '0.0.63.255', 'expected': '00000000.00000000.00111111.11111111'},
        {'data': '0.0.31.255', 'expected': '00000000.00000000.00011111.11111111'},
        {'data': '0.0.15.255', 'expected': '00000000.00000000.00001111.11111111'},
        {'data': '0.0.7.255', 'expected': '00000000.00000000.00000111.11111111'},
        {'data': '0.0.3.255', 'expected': '00000000.00000000.00000011.11111111'},
        {'data': '0.0.1.255', 'expected': '00000000.00000000.00000001.11111111'},
        {'data': '0.0.0.255', 'expected': '00000000.00000000.00000000.11111111'},
        {'data': '0.0.0.127', 'expected': '00000000.00000000.00000000.01111111'},
        {'data': '0.0.0.63', 'expected': '00000000.00000000.00000000.00111111'},
        {'data': '0.0.0.31', 'expected': '00000000.00000000.00000000.00011111'},
        {'data': '0.0.0.15', 'expected': '00000000.00000000.00000000.00001111'},
        {'data': '0.0.0.7', 'expected': '00000000.00000000.00000000.00000111'},
        {'data': '0.0.0.3', 'expected': '00000000.00000000.00000000.00000011'},
        {'data': '0.0.0.1', 'expected': '00000000.00000000.00000000.00000001'},
        {'data': '0.0.0.0', 'expected': '00000000.00000000.00000000.00000000'},
        {'data': 'abc.def.ghi.jkl', 'expected': None},
    ]
    for test_case in test_table:
        assert nsc.ip2bin(test_case["data"]) == test_case["expected"]


test_ip2bin()


def test_bin2ip():
    """
    Test netsublib.bin2ip function
    :return:
    """

    test_table = [
        {'data': '00000000.00000000.00000000.00000000', 'expected': '0.0.0.0'},
        {'data': '10000000.00000000.00000000.00000000', 'expected': '128.0.0.0'},
        {'data': '11000000.00000000.00000000.00000000', 'expected': '192.0.0.0'},
        {'data': '11100000.00000000.00000000.00000000', 'expected': '224.0.0.0'},
        {'data': '11110000.00000000.00000000.00000000', 'expected': '240.0.0.0'},
        {'data': '11111000.00000000.00000000.00000000', 'expected': '248.0.0.0'},
        {'data': '11111100.00000000.00000000.00000000', 'expected': '252.0.0.0'},
        {'data': '11111110.00000000.00000000.00000000', 'expected': '254.0.0.0'},
        {'data': '11111111.00000000.00000000.00000000', 'expected': '255.0.0.0'},
        {'data': '11111111.10000000.00000000.00000000', 'expected': '255.128.0.0'},
        {'data': '11111111.11000000.00000000.00000000', 'expected': '255.192.0.0'},
        {'data': '11111111.11100000.00000000.00000000', 'expected': '255.224.0.0'},
        {'data': '11111111.11110000.00000000.00000000', 'expected': '255.240.0.0'},
        {'data': '11111111.11111000.00000000.00000000', 'expected': '255.248.0.0'},
        {'data': '11111111.11111100.00000000.00000000', 'expected': '255.252.0.0'},
        {'data': '11111111.11111110.00000000.00000000', 'expected': '255.254.0.0'},
        {'data': '11111111.11111111.00000000.00000000', 'expected': '255.255.0.0'},
        {'data': '11111111.11111111.10000000.00000000', 'expected': '255.255.128.0'},
        {'data': '11111111.11111111.11000000.00000000', 'expected': '255.255.192.0'},
        {'data': '11111111.11111111.11100000.00000000', 'expected': '255.255.224.0'},
        {'data': '11111111.11111111.11110000.00000000', 'expected': '255.255.240.0'},
        {'data': '11111111.11111111.11111000.00000000', 'expected': '255.255.248.0'},
        {'data': '11111111.11111111.11111100.00000000', 'expected': '255.255.252.0'},
        {'data': '11111111.11111111.11111110.00000000', 'expected': '255.255.254.0'},
        {'data': '11111111.11111111.11111111.00000000', 'expected': '255.255.255.0'},
        {'data': '11111111.11111111.11111111.10000000', 'expected': '255.255.255.128'},
        {'data': '11111111.11111111.11111111.11000000', 'expected': '255.255.255.192'},
        {'data': '11111111.11111111.11111111.11100000', 'expected': '255.255.255.224'},
        {'data': '11111111.11111111.11111111.11110000', 'expected': '255.255.255.240'},
        {'data': '11111111.11111111.11111111.11111000', 'expected': '255.255.255.248'},
        {'data': '11111111.11111111.11111111.11111100', 'expected': '255.255.255.252'},
        {'data': '11111111.11111111.11111111.11111110', 'expected': '255.255.255.254'},
        {'data': '11111111.11111111.11111111.11111111', 'expected': '255.255.255.255'},
        {'data': 'abc.def.ghi.jkl', 'expected': None},
    ]

    for test_case in test_table:
        assert nsc.bin2ip(test_case["data"]) == test_case["expected"]


test_bin2ip()


def test_ip2int_list():
    """
    Test netsublib.ip2int_list function
    :return:
    """

    test_table = [
        {'data': '192.168.92.0', 'expected': [192, 168, 92, 0]},
        {'data': '192.168.92.1', 'expected': [192, 168, 92, 1]},
        {'data': '192.168.92.2', 'expected': [192, 168, 92, 2]},
        {'data': '192.168.92.3', 'expected': [192, 168, 92, 3]},
        {'data': '192.168.92.4', 'expected': [192, 168, 92, 4]},
        {'data': '192.168.92.5', 'expected': [192, 168, 92, 5]},
        {'data': '192.168.92.6', 'expected': [192, 168, 92, 6]},
        {'data': '192.168.92.7', 'expected': [192, 168, 92, 7]},
        {'data': '192.168.92.8', 'expected': [192, 168, 92, 8]},
        {'data': '192.168.92.9', 'expected': [192, 168, 92, 9]},
        {'data': '192.168.92.10', 'expected': [192, 168, 92, 10]},
        {'data': '192.168.92.11', 'expected': [192, 168, 92, 11]},
        {'data': '192.168.92.12', 'expected': [192, 168, 92, 12]},
        {'data': '192.168.92.13', 'expected': [192, 168, 92, 13]},
        {'data': '192.168.92.14', 'expected': [192, 168, 92, 14]},
        {'data': '192.168.92.15', 'expected': [192, 168, 92, 15]},
        {'data': '192.168.92.16', 'expected': [192, 168, 92, 16]},
        {'data': '192.168.92.17', 'expected': [192, 168, 92, 17]},
        {'data': '192.168.92.18', 'expected': [192, 168, 92, 18]},
        {'data': '192.168.92.19', 'expected': [192, 168, 92, 19]},
        {'data': '192.168.92.20', 'expected': [192, 168, 92, 20]},
        {'data': '192.168.92.21', 'expected': [192, 168, 92, 21]},
        {'data': '192.168.92.22', 'expected': [192, 168, 92, 22]},
        {'data': '192.168.92.23', 'expected': [192, 168, 92, 23]},
        {'data': '192.168.92.24', 'expected': [192, 168, 92, 24]},
        {'data': '192.168.92.25', 'expected': [192, 168, 92, 25]},
        {'data': '192.168.92.26', 'expected': [192, 168, 92, 26]},
        {'data': '192.168.92.27', 'expected': [192, 168, 92, 27]},
        {'data': '192.168.92.28', 'expected': [192, 168, 92, 28]},
        {'data': '192.168.92.29', 'expected': [192, 168, 92, 29]},
        {'data': '192.168.92.30', 'expected': [192, 168, 92, 30]},
        {'data': '192.168.92.31', 'expected': [192, 168, 92, 31]},
        {'data': 'abc.def.gh.jk', 'expected': None}
    ]

    for test_case in test_table:
        assert nsc.ip2int_list(test_case["data"]) == test_case["expected"]


test_ip2int_list()


def test_int_list2ip():
    """
    Test netsublib.int_list2ip function
    :return:
    """

    test_table = [
        {'data': [192, 168, 92, 0], 'expected': '192.168.92.0'},
        {'data': [192, 168, 92, 1], 'expected': '192.168.92.1'},
        {'data': [192, 168, 92, 2], 'expected': '192.168.92.2'},
        {'data': [192, 168, 92, 3], 'expected': '192.168.92.3'},
        {'data': [192, 168, 92, 4], 'expected': '192.168.92.4'},
        {'data': [192, 168, 92, 5], 'expected': '192.168.92.5'},
        {'data': [192, 168, 92, 6], 'expected': '192.168.92.6'},
        {'data': [192, 168, 92, 7], 'expected': '192.168.92.7'},
        {'data': [192, 168, 92, 8], 'expected': '192.168.92.8'},
        {'data': [192, 168, 92, 9], 'expected': '192.168.92.9'},
        {'data': [192, 168, 92, 10], 'expected': '192.168.92.10'},
        {'data': [192, 168, 92, 11], 'expected': '192.168.92.11'},
        {'data': [192, 168, 92, 12], 'expected': '192.168.92.12'},
        {'data': [192, 168, 92, 13], 'expected': '192.168.92.13'},
        {'data': [192, 168, 92, 14], 'expected': '192.168.92.14'},
        {'data': [192, 168, 92, 15], 'expected': '192.168.92.15'},
        {'data': [192, 168, 92, 16], 'expected': '192.168.92.16'},
        {'data': [192, 168, 92, 17], 'expected': '192.168.92.17'},
        {'data': [192, 168, 92, 18], 'expected': '192.168.92.18'},
        {'data': [192, 168, 92, 19], 'expected': '192.168.92.19'},
        {'data': [192, 168, 92, 20], 'expected': '192.168.92.20'},
        {'data': [192, 168, 92, 21], 'expected': '192.168.92.21'},
        {'data': [192, 168, 92, 22], 'expected': '192.168.92.22'},
        {'data': [192, 168, 92, 23], 'expected': '192.168.92.23'},
        {'data': [192, 168, 92, 24], 'expected': '192.168.92.24'},
        {'data': [192, 168, 92, 25], 'expected': '192.168.92.25'},
        {'data': [192, 168, 92, 26], 'expected': '192.168.92.26'},
        {'data': [192, 168, 92, 27], 'expected': '192.168.92.27'},
        {'data': [192, 168, 92, 28], 'expected': '192.168.92.28'},
        {'data': [192, 168, 92, 29], 'expected': '192.168.92.29'},
        {'data': [192, 168, 92, 30], 'expected': '192.168.92.30'},
        {'data': [192, 168, 92, 31], 'expected': '192.168.92.31'},
        {'data': 'abc.def.gh.jk', 'expected': None}
    ]

    for test_case in test_table:
        assert nsc.int_list2ip(test_case["data"]) == test_case["expected"]


test_int_list2ip()


def test_mask2prefix():
    """
    Test netsubcalc.mask2prefix function
    :return:
    """

    test_table = [
        {'data': '0.0.0.0', 'expected': None},
        {'data': '128.0.0.0', 'expected': 1},
        {'data': '192.0.0.0', 'expected': 2},
        {'data': '224.0.0.0', 'expected': 3},
        {'data': '240.0.0.0', 'expected': 4},
        {'data': '248.0.0.0', 'expected': 5},
        {'data': '252.0.0.0', 'expected': 6},
        {'data': '254.0.0.0', 'expected': 7},
        {'data': '255.0.0.0', 'expected': 8},
        {'data': '255.128.0.0', 'expected': 9},
        {'data': '255.192.0.0', 'expected': 10},
        {'data': '255.224.0.0', 'expected': 11},
        {'data': '255.240.0.0', 'expected': 12},
        {'data': '255.248.0.0', 'expected': 13},
        {'data': '255.252.0.0', 'expected': 14},
        {'data': '255.254.0.0', 'expected': 15},
        {'data': '255.255.0.0', 'expected': 16},
        {'data': '255.255.128.0', 'expected': 17},
        {'data': '255.255.192.0', 'expected': 18},
        {'data': '255.255.224.0', 'expected': 19},
        {'data': '255.255.240.0', 'expected': 20},
        {'data': '255.255.248.0', 'expected': 21},
        {'data': '255.255.252.0', 'expected': 22},
        {'data': '255.255.254.0', 'expected': 23},
        {'data': '255.255.255.0', 'expected': 24},
        {'data': '255.255.255.128', 'expected': 25},
        {'data': '255.255.255.192', 'expected': 26},
        {'data': '255.255.255.224', 'expected': 27},
        {'data': '255.255.255.240', 'expected': 28},
        {'data': '255.255.255.248', 'expected': 29},
        {'data': '255.255.255.252', 'expected': 30},
        {'data': '255.255.255.254', 'expected': 31},
        {'data': '255.255.255.255', 'expected': 32}
    ]

    for test_case in test_table:
        assert nsc.mask2prefix(test_case["data"]) == test_case["expected"]


test_mask2prefix()


def test_prefix2mask():
    """
    Test netsubcalc.prefix2mask function
    :return:
    """

    test_table = [
        {'data': 0, 'expected': None},
        {'data': 1, 'expected': '128.0.0.0'},
        {'data': 2, 'expected': '192.0.0.0'},
        {'data': 3, 'expected': '224.0.0.0'},
        {'data': 4, 'expected': '240.0.0.0'},
        {'data': 5, 'expected': '248.0.0.0'},
        {'data': 6, 'expected': '252.0.0.0'},
        {'data': 7, 'expected': '254.0.0.0'},
        {'data': 8, 'expected': '255.0.0.0'},
        {'data': 9, 'expected': '255.128.0.0'},
        {'data': 10, 'expected': '255.192.0.0'},
        {'data': 11, 'expected': '255.224.0.0'},
        {'data': 12, 'expected': '255.240.0.0'},
        {'data': 13, 'expected': '255.248.0.0'},
        {'data': 14, 'expected': '255.252.0.0'},
        {'data': 15, 'expected': '255.254.0.0'},
        {'data': 16, 'expected': '255.255.0.0'},
        {'data': 17, 'expected': '255.255.128.0'},
        {'data': 18, 'expected': '255.255.192.0'},
        {'data': 19, 'expected': '255.255.224.0'},
        {'data': 20, 'expected': '255.255.240.0'},
        {'data': 21, 'expected': '255.255.248.0'},
        {'data': 22, 'expected': '255.255.252.0'},
        {'data': 23, 'expected': '255.255.254.0'},
        {'data': 24, 'expected': '255.255.255.0'},
        {'data': 25, 'expected': '255.255.255.128'},
        {'data': 26, 'expected': '255.255.255.192'},
        {'data': 27, 'expected': '255.255.255.224'},
        {'data': 28, 'expected': '255.255.255.240'},
        {'data': 29, 'expected': '255.255.255.248'},
        {'data': 30, 'expected': '255.255.255.252'},
        {'data': 31, 'expected': '255.255.255.254'},
        {'data': 32, 'expected': '255.255.255.255'}
    ]

    for test_case in test_table:
        assert nsc.prefix2mask(test_case["data"]) == test_case["expected"]


test_prefix2mask()
