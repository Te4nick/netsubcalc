"""
Testing netsubcalc print functions
"""


from netsubcalc import print_subnet_info, print_all_possible_subnets


def test_print_subnet_info() -> None:
    """
    Test netsubcalc.print_subnet_info function
    :return:
    """
    test_table = [
        {
            'data': ('abc.def.ghi.jkl', '255.255.255.0'),
            'expected': None
        },
        {
            'data': ('192.168.17.2', 'abc.def.ghi.jkl'),
            'expected': None
        },
        {
            'data': ('192.168.17.2', '255.255.255.0'),
            'expected': None
        },
    ]

    for test_case in test_table:
        assert print_subnet_info(*test_case['data']) == test_case['expected']


def test_print_all_possible_subnets() -> None:
    """
    Test netsubcalc.print_all_possible_subnets function
    :return:
    """
    test_table = [
        {
            'data': ('abc.def.ghi.jkl', '255.255.255.0'),
            'expected': None
        },
        {
            'data': ('192.168.17.2', 'abc.def.ghi.jkl'),
            'expected': None
        },
        {
            'data': ('192.168.17.2', '255.255.255.0'),
            'expected': None
        },
        {
            'data': ('192.168.17.2', '255.255.255.128'),
            'expected': None
        },
    ]

    for test_case in test_table:
        assert print_all_possible_subnets(*test_case['data']) == test_case['expected']
