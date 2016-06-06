def valid_parentheses(string):
    checker = 0
    for i in string:
        if i == '(':
            checker += 1
        elif i == ')':
            checker -= 1
        if checker < 0:
            return False
    if checker == 0:
        return True
    else:
        return False
