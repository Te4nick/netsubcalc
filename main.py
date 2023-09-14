from typing import Callable
import netsubcalc as cvs


def addresses_good(args) -> bool:
    ok: bool = True
    for i, addr in enumerate(args):
        try:
            if not cvs.is_ip(addr):
                ok = False
                print(f"ALERT: Invalid parameter at position {i}")
        except ValueError:
            ok = False
            print(f"ALERT: Invalid parameter at position {i}")
    return ok


def __print_res(func: Callable, *args):
    ok: bool = True
    for i, addr in enumerate(args):
        try:
            if not cvs.is_ip(addr):
                ok = False
                print(f"ALERT: Invalid parameter at position {i}")
        except ValueError:
            ok = False
            print(f"ALERT: Invalid parameter at position {i}")
    if ok:
        print(func(*args))


def print_help():
    hlp = '''
    help - display supported commands
    ip2bin <ip> - convert dec ip to bin ip
    bin2ip <binary ip> - convert bin ip to dec ip
    netaddr <ip> <mask> - calculate net address from dec ip and dec mask
    subnet <ip> <mask> - full subnet information
    '''
    print(hlp)


if __name__ == '__main__':
    print('--=0 NETCONVERT 0=--')
    command: str = "help"

    while command != "exit":

        ins = command.rstrip().lstrip().split()
        if len(ins) == 0:
            continue

        match ins[0]:
            case "help":
                print_help()

            case "ip2bin":
                __print_res(cvs.ip2bin, ins[1])

            case "bin2ip":
                __print_res(cvs.bin2ip, ins[1])

            case "netaddr":
                __print_res(cvs.netaddr, ins[1], ins[2])

            case "subnet":
                __print_res(cvs.subnet_info, ins[1], ins[2])
                __print_res(cvs.all_possible_subnets, ins[1], ins[2])

            case _:
                print('Unresolved command')

        command = input()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
