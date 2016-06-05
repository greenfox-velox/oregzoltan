def presses(phrase):
    phrase = phrase.upper()
    one_press = '1ADGJMPTW*# '
    two_press = 'BEHKNQUX0'
    three_press = 'CFILORVY'
    four_press = 'SZ234568'
    five_press = '79'
    total = 0
    for i in phrase:
        if one_press.find(i) != -1:
            total += 1
        elif two_press.find(i) != -1:
            total += 2
        elif three_press.find(i) != -1:
            total += 3
        elif four_press.find(i) != -1:
            total += 4
        elif five_press.find(i) != -1:
            total += 5
    return total

print(presses("HOW R U"))
# 13
# ------- ------- -------
# |     | | ABC | | DEF |
# |  1  | |  2  | |  3  |
# ------- ------- -------
# ------- ------- -------
# | GHI | | JKL | | MNO |
# |  4  | |  5  | |  6  |
# ------- ------- -------
# ------- ------- -------
# |PQRS | | TUV | | WXYZ|
# |  7  | |  8  | |  9  |
# ------- ------- -------
# ------- ------- -------
# |     | |space| |     |
# |  *  | |  0  | |  #  |
# ------- ------- -------
