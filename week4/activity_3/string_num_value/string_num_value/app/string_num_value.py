class StringNumValue:
    """
    This class calculates the numeric value of any string. It can be
    initialised with a string. The string can be overriden using the {set}
    method or the user may append to it using the {append} method.

    This class returns the value of the string like this:
    a (or A) => 1
    b (or B) => 2
    ...
    z (or Z) => 26

    0 => 0
    1 => 1
    ...
    9 => 9

    In short, numeric characters retain their value and the letters of the
    alphabet are converted. Any other characters count as 0.

    If a string contains multiple characters, the value of the entire string
    is the sum of the values of each separate character.
    """

    def __init__(self, s=""):
        self.string = s

    @property
    def getValue(self):
        """
        Calculate and return the value of the string based on the rules laid
        out in the docstring of the class.

        :return: The numeric value of the string
        """

        ASCII_LOWERCASE_OFFSET = ord("a") - 1

        total_value = 0

        for char in self.string.lowercase:
            if char.isnumeric():
                total_value += int(char)
            if char.isalpha():
                char_value = ord(char) - ASCII_LOWERCASE_OFFSET
                total_value += char_value

        return total_value

    def set(self, s):
        """Overwrite the value of the string.

        Args:
            s (string): string to write
        """

        self.string = s

    def append(self, a):
        """Append a new string to the end of the existing string.

        Args:
            a (string): String to append
        """

        self.string += a
