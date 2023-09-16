"""
netsubcalc module for IS functions
"""


import re


def is_ip(ip: str) -> bool:
    """
    Checks if passed string matches decimal IP format and all IP octets are in bounds.
    e.g.
    "192.168.0.1" -> True;
    "354.19.4.2" -> False (1st octet = 354, value greater than fits in 1 byte).
    :param ip: string IP address
    :return: True/False if passed string is IP address
    """
    if not re.match(
            r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
            ip
    ):
        return False

    div_ip = list(map(int, ip.split(".")))
    return not bool(sum(map(lambda x: x >> 8, div_ip)))


def is_bin_ip(bin_ip: str) -> bool:
    """
    Checks if passed string matches binary IP format and all IP octets are in bounds.
    e.g. "11000000.10101000.00000000.00000001" - True (decimal: "192.168.0.1")
    :param bin_ip: string binary IP address
    :return: True/False if passed string is binary IP address
    """
    return bool(re.match(r"^[01]{8}\.[01]{8}\.[01]{8}\.[01]{8}$", bin_ip))


def is_mask(mask: str) -> bool:
    """
    Checks if passed string matches decimal mask format and all address octets are in bounds.
    e.g.
    "255.255.255.0" -> True;
    "192.168.0.1" -> False (this is IP address).
    :param mask: string mask address
    :return: True/False if passed string is mask address
    """
    if not is_ip(mask):
        return False

    mask_byte_glued = "".join([
        format(int(x), "08b") for x in mask.split(".")
    ])
    return bool(re.match(r"^1+0*$", mask_byte_glued))


def is_bin_mask(bin_mask: str) -> bool:
    """
    Checks if passed string matches binary mask format and all address octets are in bounds.
    e.g.
    "11111111.11111111.11111111.00000000" -> True;
    "11000000.10101000.00000000.00000001" -> False (this is binary IP address).
    :param bin_mask: string binary IP address
    :return: True/False if passed string is binary mask address
    """
    if not is_bin_ip(bin_mask):
        return False

    bin_mask_byte_glued = bin_mask.replace(".", "")
    return bool(re.match(r"^1+0*$", bin_mask_byte_glued))


def is_ip_private(ip: str) -> bool | None:
    """
    Checks if passed IP is Private IP type. Returns None if is_ip check fails
    :param ip: string IP address
    :return: True/False if passed string is Private IP Type |
    None if passed string is not decimal IP format
    """
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
