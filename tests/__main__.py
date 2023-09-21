"""
Main file for running tests for coverage
"""


from tests.test_is_funcs import (
    test_is_ip,
    test_is_bin_ip,
    test_is_mask,
    test_is_bin_mask,
    test_is_ip_private
)
from tests.test_convert_funcs import (
    test_ip2bin,
    test_bin2ip,
    test_ip2int_list,
    test_int_list2ip,
    test_mask2prefix,
    test_prefix2mask
)
from tests.test_calc_funcs import (
    test_netaddr,
    test_broadcast,
    test_hosts_count,
    test_hosts_ip_range,
    test_ip_class
)


def main() -> None:
    """
    Main function to run tests
    :return:
    """
    # test_is_funcs
    test_is_ip()
    test_is_bin_ip()
    test_is_mask()
    test_is_bin_mask()
    test_is_ip_private()
    # test_convert_funcs
    test_ip2bin()
    test_bin2ip()
    test_ip2int_list()
    test_int_list2ip()
    test_mask2prefix()
    test_prefix2mask()
    # test_calc_funcs
    test_netaddr()
    test_broadcast()
    test_hosts_count()
    test_hosts_ip_range()
    test_ip_class()


if __name__ == '__main__':
    main()
