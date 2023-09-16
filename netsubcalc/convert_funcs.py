"""
netsubcalc Convert IP/Mask from x to y format module
"""


from netsubcalc.is_funcs import is_ip, is_mask, is_bin_ip


__all__ = [
    "ip2bin",
    "bin2ip",
    "ip2int_list",
    "int_list2ip",
    "mask2prefix",
    "prefix2mask"
]


def ip2bin(dec_ip: str) -> str | None:
    """
    Converts decimal IP to binary format
    e.g. "192.168.0.1" -> "11000000.10101000.00000000.00000001"
    :param dec_ip: string decimal IP
    :return: string binary IP |
    None if passed string is not decimal IP format
    """
    if not is_ip(dec_ip):
        return None

    return '.'.join([format(int(x), "08b") for x in dec_ip.split(".")])


def bin2ip(bin_ip: str) -> str | None:
    """
    Converts binary IP to decimal format
    e.g. "11000000.10101000.00000000.00000001" -> "192.168.0.1"
    :param bin_ip: string binary IP
    :return: string decimal IP
    None if passed string is not binary IP format
    """
    if not is_bin_ip(bin_ip):
        return None

    div_ip = list(map(
        lambda x: str(int('0b' + x, 2)),
        bin_ip.split('.')
    ))
    return '.'.join(div_ip)


def ip2int_list(dec_ip: str) -> list[int] | None:
    """
    Splits decimal IP to list[int]
    e.g. "192.168.0.1" -> [192, 168, 0, 1]
    :param dec_ip: string decimal IP
    :return: list[int] split IP |
    None if passed string is not decimal IP format
    """
    if not is_ip(dec_ip):
        return None

    return list(map(int, dec_ip.split(".")))


def int_list2ip(div_ip: list[int]) -> str | None:
    """
    Glues list[int] IP octets to decimal IP string
    e.g. [192, 168, 0, 1] -> "192.168.0.1"
    :param div_ip: list[int] split IP
    :return: string decimal IP |
    None if passed list of invalid format
    """
    if len(div_ip) != 4:
        return None

    str_ip: str = ".".join(map(str, div_ip))
    if not is_ip(str_ip):
        return None

    return str_ip


def mask2prefix(dec_mask: str) -> int | None:
    """
    Counts mask bits and returns as prefix
    e.g. "255.255.255.0" -> 24
    :param dec_mask: string decimal mask address
    :return: int mask prefix |
    None if passed string is not decimal mask format
    """
    if not is_mask(dec_mask):
        return None

    return ip2bin(dec_mask).count("1")


def prefix2mask(prefix: int) -> str | None:
    """
    Generates string decimal mask from int mask prefix
    e.g. 24 -> "255.255.255.0"
    :param prefix: int mask prefix
    :return: string decimal mask address |
    None if passed int is not decimal mask prefix
    """
    if not 1 <= prefix <= 32:
        return None

    no_dot_mask = "1" * prefix + "0" * (32 - prefix)
    dot_mask = (no_dot_mask[:8] + '.' +
                no_dot_mask[8:16] + '.' +
                no_dot_mask[16:24] + '.' +
                no_dot_mask[24:])
    return bin2ip(dot_mask)
