import pytest

def rotate(string, n):
    """Rotate characters in a string. Expects string and n (int) for
       number of characters to move.
    """
    if type(n) != int:
        return "Not an integer"

    if n == 0:
        return string

    if n > 0:
        s_new = string[0:n]
        l = list(string)
        l[0:n] = ""
        l.append(s_new)
        string = "".join(l)
        return string

    if n < 0:
        s_new = string[n:len(string)]
        l = list(string)
        l[n:len(string)] = ""
        l.insert(0, s_new)
        string = "".join(l)
        return string
