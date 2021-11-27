def declination(age: int) -> str:
    """сколько лет?"""
    if (age % 10 == 1) and (age != 11) and (age != 111):
        return 'год'

    elif (age % 10 > 1) and (age % 10 < 5) and (age not in [12, 13, 14]):
        return 'года'

    else:
        return 'лет'


def declination_from(age: int) -> str:
    """от/до скольки лет?"""

    if (age % 10 >= 1) and (age % 10 < 2) and (age not in [11, 12, 13, 14]):
        return 'года'

    else:
        return 'лет'