import netsubcalc as nsc






def test_ip2bin():
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