def multi_bracket_validation(input):
    """Checks to see if brackets are balanced (open and closed properly)

    Args:
        input (string): String of characters

    Returns:
        Boolean: True if balanced, else False
    """
    opening_bracket = ["(", "{", "["]
    closing_bracket = [")", "}", "]"]
    bracket_pairs = {"(":")", "{":"}", "[":"]"}

    user_input = list(input)

    open_bracket_list = []
    close_bracket_list = []
    test_list = []

    for x in user_input:
        for y in opening_bracket:
            if x == y:
                open_bracket_list.append(x)
        for z in closing_bracket:
            if x == z:
                close_bracket_list.append(x)

    if len(open_bracket_list) != len(close_bracket_list):
        return False

    for x in user_input:
        if x in bracket_pairs:
            test_list.append(x)
        if x in closing_bracket:
            if not open_bracket_list:
                return False
            elif x != bracket_pairs[test_list.pop()]:
                return False
    if test_list is not None:
        return True
    return False

if __name__ == "__main__":
    mult = multi_bracket_validation("()}")
    # print(mult)
    pass 