"""
netsubcalc Network / Subnetwork Calculation Module
"""


from netsubcalc.convert_funcs import ip2int_list, mask2prefix
from netsubcalc.is_funcs import is_ip, is_mask


__all__ = [
    "netaddr",
    "broadcast",
    "hosts_count",
    "hosts_ip_range",
    "ip_class"
]


def netaddr(dec_ip: str, dec_mask: str) -> str | None:
    """
    Calculates network address using
    string decimal IP address and string decimal mask address
    :param dec_ip: string decimal IP
    :param dec_mask: string decimal mask
    :return: string decimal network address |
    None if IP or mask are not string decimal format
    """
    div_ip: list[int] = ip2int_list(dec_ip)
    div_mask: list[int] = ip2int_list(dec_mask)
    if not (div_ip and div_mask):
        return None

    div_net: list[str] = [
        str(ip_octet & mask_octet)
        for ip_octet, mask_octet in zip(div_ip, div_mask)
    ]
    return '.'.join(div_net)


def broadcast(dec_ip: str, dec_mask: str) -> str | None:
    """
    Calculates broadcast address using
    string decimal IP address and string decimal mask address
    :param dec_ip: string decimal IP
    :param dec_mask: string decimal mask
    :return: string decimal network address |
    None if IP or mask are not string decimal format
    """
    div_ip: list[int] = ip2int_list(dec_ip)
    div_mask: list[int] = ip2int_list(dec_mask)
    if not (div_ip and div_mask):
        return None

    broad: list[str] = [
        str(ip_octet | ~mask_octet & 0xff)
        for ip_octet, mask_octet in zip(div_ip, div_mask)
    ]
    return '.'.join(broad)


def hosts_count(dec_mask: str) -> int | None:
    """
    Calculates all network hosts addresses count
    using string decimal mask address
    :param dec_mask: string decimal mask
    :return: int hosts address count |
    None if mask is not string decimal format
    """
    if not is_mask(dec_mask):
        return None

    return 1 << (32 - mask2prefix(dec_mask))


def hosts_ip_range(dec_ip: str, dec_mask: str) -> (str | None, str | None):
    """
    Calculates usable hosts IP addresses range and returns (str, str)
    tuple of 2 string decimal IP addresses using
    string decimal IP address and string decimal mask address
    :param dec_ip: string decimal IP
    :param dec_mask: string decimal mask
    :return: (str, str) string decimal IP tuple |
    (None, None) tuple if IP or mask are not string decimal format
    """
    net_addr = netaddr(dec_ip, dec_mask)
    broad = broadcast(dec_ip, dec_mask)
    if not (net_addr and broad):
        return None, None

    div_net: list[int] = ip2int_list(net_addr)
    div_broad: list[int] = ip2int_list(broad)
    div_net[-1], div_broad[-1] = div_net[-1] + 1, div_broad[-1] - 1
    first: str = ".".join(map(str, div_net))
    last: str = ".".join(map(str, div_broad))
    return first, last


def ip_class(dec_ip: str) -> str | None:
    """
    Calculates str IP network class
    using string decimal IP address
    :param dec_ip: string decimal IP
    :return: string IP network class |
    None if IP is not string decimal format
    """
    if not is_ip(dec_ip):
        return None

    res_class: str = ""
    first_octet: int = ip2int_list(dec_ip)[0]
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
