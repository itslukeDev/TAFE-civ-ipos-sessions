def add(a, b):
    """Adds two values together

    Args:
        a (num):
        b (num):

    Returns:
        num: result of the sum
    """
    if type(a) not in [int, float] or type(b) not in [int, float]:
        return TypeError("")

    return a + b
