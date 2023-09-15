import re


def is_ip(ip: str) -> bool:
    if not re.match(
            r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
            ip
    ):
        return False

    div_ip = list(map(int, ip.split(".")))
    return not bool(sum(map(lambda x: x >> 8, div_ip)))


def is_bin_ip(bin_ip: str) -> bool:
    return bool(re.match(r"^[01]{8}\.[01]{8}\.[01]{8}\.[01]{8}$", bin_ip))


def is_mask(mask: str) -> bool:
    if not is_ip(mask):
        return False

    mask_byte_glued = "".join([
        format(int(x), "08b") for x in mask.split(".")
    ])
    return bool(re.match(r"^1+0*$", mask_byte_glued))


def is_bin_mask(bin_mask: str) -> bool:
    if not is_bin_ip(bin_mask):
        return False

    bin_mask_byte_glued = bin_mask.replace(".", "")
    return bool(re.match(r"^1+0*$", bin_mask_byte_glued))


def ip2bin(ip: str) -> str | None:
    if not is_ip(ip):
        return None

    return '.'.join([format(int(x), "08b") for x in ip.split(".")])


def bin2ip(bin_ip: str) -> str | None:
    if not is_bin_ip(bin_ip):
        return None

    div_ip = list(map(
        lambda x: str(int('0b' + x, 2)),
        bin_ip.split('.')
    ))
    return '.'.join(div_ip)


def ip2int_list(ip: str) -> list[int] | None:
    if not is_ip(ip):
        return None

    return list(map(int, ip.split(".")))


def int_list2ip(div_ip: list[int]) -> str | None:
    if len(div_ip) != 4:
        return None

    ip: str = ".".join(map(str, div_ip))
    if not is_ip(ip):
        return None

    return ip


def mask2prefix(mask: str) -> int | None:
    if not is_mask(mask):
        return None

    return ip2bin(mask).count("1")


def prefix2mask(prefix: int) -> str | None:
    if not (1 <= prefix <= 32):
        return None

    no_dot_mask = "1" * prefix + "0" * (32 - prefix)
    dot_mask = (no_dot_mask[:8] + '.' +
                no_dot_mask[8:16] + '.' +
                no_dot_mask[16:24] + '.' +
                no_dot_mask[24:])
    return dot_mask


def netaddr(ip: str, mask: str) -> str | None:
    div_ip: list[int] = ip2int_list(ip)
    div_mask: list[int] = ip2int_list(mask)
    if not (div_ip and div_mask):
        return None

    div_net: list[str] = [
        str(ip_octet & mask_octet)
        for ip_octet, mask_octet in zip(div_ip, div_mask)
    ]
    return '.'.join(div_net)


def broadcast(ip: str, mask: str) -> str | None:
    div_ip: list[int] = ip2int_list(ip)
    div_mask: list[int] = ip2int_list(mask)
    if not (div_ip and div_mask):
        return None

    broad: list[str] = [
        str(ip_octet | ~mask_octet & 0xff)
        for ip_octet, mask_octet in zip(div_ip, div_mask)
    ]
    return '.'.join(broad)


def hosts_count(mask: str) -> int | None:
    if not is_mask(mask):
        return None

    return 1 << (32 - mask2prefix(mask))


def hosts_ip_range(ip: str, mask: str) -> (str | None, str | None):
    net_addr = netaddr(ip, mask)
    broad = broadcast(ip, mask)
    if not (net_addr and broad):
        return None, None

    div_net: list[int] = ip2int_list(net_addr)
    div_broad: list[int] = ip2int_list(broad)
    div_net[-1], div_broad[-1] = div_net[-1] + 1, div_broad[-1] - 1
    first: str = ".".join(map(str, div_net))
    last: str = ".".join(map(str, div_broad))
    return first, last


def ip_class(ip: str) -> str | None:
    if not is_ip(ip):
        return None

    first_octet: int = ip2int_list(ip)[0]
    if 1 <= first_octet <= 126:
        return "A"
    if 128 <= first_octet <= 191:
        return "B"
    if 192 <= first_octet <= 223:
        return "C"
    if 224 <= first_octet <= 239:
        return "D"
    if 240 <= first_octet <= 255:
        return "E"
    if first_octet == 127:
        return "Testing Purposes"


def is_ip_private(ip: str) -> bool | None:
    if not is_ip(ip):
        return None

    div_ip = list(map(int, ip.split(".")))
    f_oct, s_oct = div_ip[0], div_ip[1]  # First and Second IP octets
    if 10 == f_oct:
        return True  # Private Class A
    if (172 == f_oct) & (16 <= s_oct <= 31):  # Private Class B
        return True
    if (192 == f_oct) & (168 == s_oct):  # Private Class C
        return True
    return False


def print_subnet_info(ip: str, mask: str) -> None:
    print(f"{'IP Address:':<24}{ip:>36}")
    print(f"{'Network Address:':<24}{netaddr(ip, mask):>36}")
    print(f"{'Usable Host IP Range:':<24}{' - '.join(hosts_ip_range(ip, mask)):>36}")
    print(f"{'Broadcast Address:':<24}{broadcast(ip, mask):>36}")
    print(f"{'Total Number of Hosts:':<24}{hosts_count(mask):>36}")
    print(f"{'Usable Number of Hosts:':<24}{hosts_count(mask) - 2:>36}")
    print(f"{'Subnet Mask:':<24}{mask:>36}")
    print(f"{'Binary Subnet Mask:':<24}{ip2bin(mask):>36}")
    print(f"{'IP Class:':<24}{ip_class(ip):>36}")
    print(f"{'CIDR Notation:':<24}{'/' + str(mask2prefix(mask)):>36}")
    print(f"{'IP Type:':<24}{'Private' if is_ip_private(ip) else 'Public':>36}")


def print_all_possible_subnets(ip: str, mask: str) -> None:
    if mask2prefix(mask) % 8 == 0:  # Check for default mask: thus no subnets exist
        return

    sub_count = 1 << (8 - (mask2prefix(mask) % 8))
    net_octet = mask2prefix(mask) // 8

    addr_print = lambda net, use, broad: print(f"{net:>20}{use:>36}{broad:>20}")
    common_ip = [str(octet) if i < net_octet else '*' for i, octet in enumerate(ip2int_list(ip))]
    print(f"\nAll {sub_count} of the Possible /{mask2prefix(mask)} Networks for {'.'.join(common_ip)}")
    print('='*76)
    addr_print('Network Address', 'Usable Host Range', 'Broadcast Address')

    for i in range(sub_count):
        sub_ip = ip2int_list(ip)
        sub_ip[net_octet] = sub_count * i
        sub_ip = int_list2ip(sub_ip)
        addr_print(netaddr(sub_ip, mask),
                   ' - '.join(hosts_ip_range(sub_ip, mask)),
                   broadcast(sub_ip, mask))

    print('=' * 76)
