import netsubcalc as nsc


def test_is_ip() -> None:
    test_table = [
        {
            "data": "192.168.16.1",
            "expected": True
        },
        {
            "data": "354.764.234.0",
            "expected": False
        },
        {
            "data": "35f.764.234.0",
            "expected": False
        },
        {
            "data": "df.sdg.D$!.v",
            "expected": False
        },
        {
            "data": "wfbhibvqewv!#*%&!371t8./\\",
            "expected": False
        },
    ]

    for test_case in test_table:
        assert nsc.is_ip(test_case["data"]) == test_case["expected"]
