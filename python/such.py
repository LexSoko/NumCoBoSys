def such(list_, z, a, b):
    """
    Binary search for a state `z` in the `list_` between indices `a` and `b`.

    Parameters:
        list_: Sorted list of states.
        z: Target state to search for.
        a: Start index.
        b: End index.

    Returns:
        Index of the state in `list_`, or 0 if not found.
    """
    while b - a > 1:
        c = (a + b) // 2
        if list_[c] == z:
            return c + 1
        elif list_[c] > z:
            b = c
        else:
            a = c

    if list_[a] == z:
        return a + 1
    elif list_[b] == z:
        return b + 1
    else:
        return 0
