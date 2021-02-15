"""
Caisse automatique
"""
MAX = 922_337_203_685_477_580_7


def change_inf_5(cash: int, cash_10: int) -> (None, dict):
    """
    refactor functions change
    :param cash: cash
    :param cash_10: value of cash 10
    :return:
    """
    cash_5 = 0
    cash_2 = 0
    if cash % 5 == 0 and cash >= 5:
        cash_5 = (cash - cash % 5) // 5
    elif cash % 5 == 2:
        cash_5 = (cash - cash % 5) // 5
        cash_2 = cash % 5 // 2
    else:
        if cash % 2 == 0:
            cash_2 = cash // 2
        else:
            return None
    return {"two": cash_2, "five": cash_5, "ten": cash_10}


def change(cash: int) -> (dict, None):
    """change function

    Args:
        cash ([long]): cash
    """
    if cash < 2 or cash > MAX:
        raise Exception("Impossible")

    cash_10 = 0
    cash_5 = 0
    cash_2 = 0

    if cash >= 10:
        if cash % 10 == 0:
            cash_10 = cash // 10
        else:
            cash_10 = (cash - cash % 10) // 10
            cash = cash % 10
            return change_inf_5(cash, cash_10)
    else:
        return change_inf_5(cash, cash_10)
    return {"two": cash_2, "five": cash_5, "ten": cash_10}
