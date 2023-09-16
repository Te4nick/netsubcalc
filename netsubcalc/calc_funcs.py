from convert_funcs import ip2int_list, mask2prefix
from is_funcs import is_ip, is_mask


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

    res_class: str = ""
    first_octet: int = ip2int_list(ip)[0]
    if 1 <= first_octet <= 126:
        res_class = "A"
    if 128 <= first_octet <= 191:
        res_class = "B"
    if 192 <= first_octet <= 223:
        res_class = "C"
    if 224 <= first_octet <= 239:
        res_class = "D"
    if 240 <= first_octet <= 255:
        res_class = "E"
    if first_octet == 127:
        res_class = "Testing Purposes"
    return res_class
