"""
Testing calculation functions of netsubcalc
"""


import netsubcalc as nsc


def test_netaddr() -> None:
    """
    Test netsubcalc.netaddr function
    :return:
    """
    test_table = [
        {
            'data': ('192.168.62.1', '255.255.255.0'),
            'expected': '192.168.62.0'
        },
        {
            'data': ('172.17.2.172', '255.255.0.0'),
            'expected': '172.17.0.0'
        },
        {
            'data': ('abc.def.ghi.jkl', '255.255.0.0'),
            'expected': None
        },
    ]

    for test_case in test_table:
        assert nsc.netaddr(*test_case['data']) == test_case['expected']


def test_broadcast() -> None:
    """
    Test netsubcalc.broadcast function
    :return:
    """
    test_table = [
        {
            'data': ('192.168.62.1', '255.255.255.0'),
            'expected': '192.168.62.255'
        },
        {
            'data': ('172.17.2.172', '255.255.0.0'),
            'expected': '172.17.255.255'
        },
        {
            'data': ('abc.def.ghi.jkl', '255.255.0.0'),
            'expected': None
        },
    ]

    for test_case in test_table:
        assert nsc.broadcast(*test_case['data']) == test_case['expected']


def test_hosts_count() -> None:
    """
    Test netsubcalc.hosts_count function
    :return:
    """
    test_table = [
        {'data': '0.0.0.0', 'expected': None},
        {'data': '128.0.0.0', 'expected': 2147483648},
        {'data': '192.0.0.0', 'expected': 1073741824},
        {'data': '224.0.0.0', 'expected': 536870912},
        {'data': '240.0.0.0', 'expected': 268435456},
        {'data': '248.0.0.0', 'expected': 134217728},
        {'data': '252.0.0.0', 'expected': 67108864},
        {'data': '254.0.0.0', 'expected': 33554432},
        {'data': '255.0.0.0', 'expected': 16777216},
        {'data': '255.128.0.0', 'expected': 8388608},
        {'data': '255.192.0.0', 'expected': 4194304},
        {'data': '255.224.0.0', 'expected': 2097152},
        {'data': '255.240.0.0', 'expected': 1048576},
        {'data': '255.248.0.0', 'expected': 524288},
        {'data': '255.252.0.0', 'expected': 262144},
        {'data': '255.254.0.0', 'expected': 131072},
        {'data': '255.255.0.0', 'expected': 65536},
        {'data': '255.255.128.0', 'expected': 32768},
        {'data': '255.255.192.0', 'expected': 16384},
        {'data': '255.255.224.0', 'expected': 8192},
        {'data': '255.255.240.0', 'expected': 4096},
        {'data': '255.255.248.0', 'expected': 2048},
        {'data': '255.255.252.0', 'expected': 1024},
        {'data': '255.255.254.0', 'expected': 512},
        {'data': '255.255.255.0', 'expected': 256},
        {'data': '255.255.255.128', 'expected': 128},
        {'data': '255.255.255.192', 'expected': 64},
        {'data': '255.255.255.224', 'expected': 32},
        {'data': '255.255.255.240', 'expected': 16},
        {'data': '255.255.255.248', 'expected': 8},
        {'data': '255.255.255.252', 'expected': 4},
        {'data': '255.255.255.254', 'expected': 2},
        {'data': '255.255.255.255', 'expected': 1}
    ]

    for test_case in test_table:
        assert nsc.hosts_count(test_case['data']) == test_case['expected']


def test_hosts_ip_range() -> None:
    """
    Test netsubcalc.hosts_ip_range function
    :return:
    """
    test_table = [
        {
            'data': ('192.168.62.127', '255.255.255.0'),
            'expected': ('192.168.62.1', '192.168.62.254')
        },
        {
            'data': ('172.17.2.201', '255.255.0.0'),
            'expected': ('172.17.0.1', '172.17.255.254')
        },
        {
            'data': ('abc.def.ghi.jkl', '255.255.0.0'),
            'expected': (None, None)
        }
    ]

    for test_case in test_table:
        assert nsc.hosts_ip_range(*test_case['data']) == test_case['expected']


def test_ip_class() -> None:
    """
    Test netsubcalc.ip_class function
    :return:
    """
    test_table = [
        {
            'data': '120.0.0.201',
            'expected': 'A',
        },
        {
            'data': '172.17.2.201',
            'expected': 'B',
        },
        {
            'data': '192.168.62.127',
            'expected': 'C'
        },
        {
            'data': '224.162.56.3',
            'expected': 'D',
        },
        {
            'data': '250.201.38.16',
            'expected': 'E',
        },
        {
            'data': '127.0.0.1',
            'expected': 'Testing Purposes',
        },
        {
            'data': 'abc.def.ghi.jkl',
            'expected': None,
        }
    ]

    for test_case in test_table:
        assert nsc.ip_class(test_case['data']) == test_case['expected']
