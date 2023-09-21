"""
Simple standard print() functions for subnets information
"""

from netsubcalc.calc_funcs import (
    netaddr,
    broadcast,
    hosts_ip_range,
    hosts_count,
    ip_class,
)
from netsubcalc.convert_funcs import (
    ip2bin,
    mask2prefix,
    ip2int_list,
    int_list2ip,
)
from netsubcalc.is_funcs import (
    is_ip,
    is_mask,
    is_ip_private,
)


def print_subnet_info(dec_ip: str, mask: str) -> None:
    """
    Prints subnet info for specified IP and Mask
    :param dec_ip: string decimal IP
    :param mask: string decimal Mask
    :return: None
    """
    if not is_ip(dec_ip):
        print("Invalid ID Address format")
        return
    if not is_mask(mask):
        print("Invalid Mask format")
        return
    print(f"{'IP Address:':<24}{dec_ip:>36}")
    print(f"{'Network Address:':<24}{netaddr(dec_ip, mask):>36}")
    print(f"{'Usable Host IP Range:':<24}{' - '.join(hosts_ip_range(dec_ip, mask)):>36}")
    print(f"{'Broadcast Address:':<24}{broadcast(dec_ip, mask):>36}")
    print(f"{'Total Number of Hosts:':<24}{hosts_count(mask):>36}")
    print(f"{'Usable Number of Hosts:':<24}{hosts_count(mask) - 2:>36}")
    print(f"{'Subnet Mask:':<24}{mask:>36}")
    print(f"{'Binary Subnet Mask:':<24}{ip2bin(mask):>36}")
    print(f"{'IP Class:':<24}{ip_class(dec_ip):>36}")
    print(f"{'CIDR Notation:':<24}{'/' + str(mask2prefix(mask)):>36}")
    print(f"{'IP Type:':<24}{'Private' if is_ip_private(dec_ip) else 'Public':>36}")


def __print_subnet_addresses(net_addr, usable_addr, broad_addr) -> None:
    print(f"{net_addr:>20}{usable_addr:>36}{broad_addr:>20}")


def print_all_possible_subnets(dec_ip: str, mask: str) -> None:
    """
    Prints all possible subnets for network
    :param dec_ip: string decimal IP address
    :param mask: string decimal mask address
    :return: None
    """
    if not is_ip(dec_ip):
        print("Invalid ID Address format")
        return
    if not is_mask(mask):
        print("Invalid Mask format")
        return

    mask_prefix = mask2prefix(mask)
    if mask_prefix % 8 == 0:  # Check for default mask: thus no subnets exist
        print("Whole network Mask, no subnets exists")
        return

    sub_count = 1 << (mask_prefix - (8 * (mask_prefix // 8)))
    net_octet = mask2prefix(mask) // 8

    common_ip = [str(octet) if i < net_octet else '*'
                 for i, octet in enumerate(ip2int_list(dec_ip))]
    print(
        f"\nAll {sub_count}" +
        f"of the Possible /{mask2prefix(mask)} Networks for {'.'.join(common_ip)}"
    )
    print('=' * 76)
    __print_subnet_addresses('Network Address',
                             'Usable Host Range',
                             'Broadcast Address')

    for i in range(sub_count):
        sub_ip = ip2int_list(dec_ip)
        sub_ip[net_octet] = sub_count * i
        sub_ip = int_list2ip(sub_ip)
        __print_subnet_addresses(netaddr(sub_ip, mask),
                                 ' - '.join(hosts_ip_range(sub_ip, mask)),
                                 broadcast(sub_ip, mask))

    print('=' * 76)
