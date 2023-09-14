def is_ip(ip: str) -> bool:
    div_ip = list(map(int, ip.split(".")))
    if len(div_ip) != 4:
        return False
    return not bool(sum(map(lambda x: x >> 8, div_ip)))


def is_mask(mask: str) -> bool:
    if not is_ip(mask):
        return False
    return len([i for i in ip2int_list(mask) if i != 0 or i != 255]) == 1


def ip2bin(ip: str) -> str:
    div_ip = list(map(
        lambda x:
        ("0" * (8 - (len(bin(int(x))) - 2)) + bin(int(x))[2::]),
        ip.split('.')
    ))
    return '.'.join(div_ip)


def ip2int_list(ip: str) -> list[int]:
    return list(map(int, ip.split(".")))


def ip_int_list2str(div_ip: list[int]) -> str:
    return ".".join(map(str, div_ip))


def bin2ip(bip: str) -> str:
    div_ip = list(map(
        lambda x:
        str(int('0b' + x, 2)),
        bip.split('.')
    ))
    return '.'.join(div_ip)


def mask2prefix(mask: str) -> int:
    return ip2bin(mask).count("1")


def netaddr(ip: str, mask: str) -> str:
    div_ip: list[int] = list(map(int, ip.split('.')))
    div_mask: list[int] = list(map(int, mask.split('.')))
    div_net: list[str] = [str(ip_octet & mask_octet) for ip_octet, mask_octet in zip(div_ip, div_mask)]
    return '.'.join(div_net)


def broadcast(ip: str, mask: str) -> str:
    div_ip: list[int] = list(map(int, ip.split('.')))
    div_mask: list[int] = list(map(int, mask.split('.')))
    broad: list[str] = [str(ip_octet | ~mask_octet & 0xff) for ip_octet, mask_octet in zip(div_ip, div_mask)]
    return '.'.join(broad)


def hosts_count(mask: str) -> int:
    return 1 << (32 - mask2prefix(mask))


def usable_ip_range(ip: str, mask: str) -> (str, str):
    div_net: list[int] = list(map(int, netaddr(ip, mask).split('.')))
    div_broad: list[int] = list(map(int, broadcast(ip, mask).split('.')))
    div_net[-1], div_broad[-1] = div_net[-1] + 1, div_broad[-1] - 1
    first: str = ".".join(map(str, div_net))
    last: str = ".".join(map(str, div_broad))
    return first, last


def ip_class(ip: str) -> str:
    first_octet = list(map(int, ip.split(".")))[0]
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


def is_ip_private(ip: str) -> bool:
    div_ip = list(map(int, ip.split(".")))
    f_oct, s_oct = div_ip[0], div_ip[1]  # First and Second IP octets
    if ((10 == f_oct) or  # Private Class A
            (172 == f_oct & 16 <= s_oct <= 31) or  # Private Class B
            (192 == f_oct & 168 == s_oct)):  # Private Class C
        return True
    return False


def subnet_info(ip: str, mask: str) -> None:
    print(f"{'IP Address:':<24}{ip:>36}")
    print(f"{'Network Address:':<24}{netaddr(ip, mask):>36}")
    print(f"{'Usable Host IP Range:':<24}{' - '.join(usable_ip_range(ip, mask)):>36}")
    print(f"{'Broadcast Address:':<24}{broadcast(ip, mask):>36}")
    print(f"{'Total Number of Hosts:':<24}{hosts_count(mask):>36}")
    print(f"{'Usable Number of Hosts:':<24}{hosts_count(mask) - 2:>36}")
    print(f"{'Subnet Mask:':<24}{mask:>36}")
    print(f"{'Binary Subnet Mask:':<24}{ip2bin(mask):>36}")
    print(f"{'IP Class:':<24}{ip_class(ip):>36}")
    print(f"{'CIDR Notation:':<24}{'/' + str(mask2prefix(mask)):>36}")
    print(f"{'IP Type:':<24}{'Private' if is_ip_private(ip) else 'Public':>36}")


def all_possible_subnets(ip: str, mask: str) -> None:
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
        sub_ip = ip_int_list2str(sub_ip)
        addr_print(netaddr(sub_ip, mask),
                   ' - '.join(usable_ip_range(sub_ip, mask)),
                   broadcast(sub_ip, mask))

    print('=' * 76)
