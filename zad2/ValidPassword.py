class ValidPassword:

    def password(self, s):
        """
        >>> p = ValidPassword()
        >>> p.password("")
        False
        >>> p.password("A@1x")
        False
        >>> p.password("123456789")
        False
        >>> p.password("Abcdefgh1!")
        True
        >>> p.password("AlaMaKot9@")
        True
        >>> p.password([])
        Traceback (most recent call last):
        ...
        Exception: Not a string
        >>> p.password({})
        Traceback (most recent call last):
        ...
        Exception: Not a string
        >>> p.password(12)
        Traceback (most recent call last):
        ...
        Exception: Not a string
        >>> p.password(None)
        Traceback (most recent call last):
        ...
        Exception: Not a string
        >>> p.password(False)
        Traceback (most recent call last):
        ...
        Exception: Not a string


        """
        if isinstance(s, str):
            l, u, p, d = 0, 0, 0, 0
            if (len(s) >= 8):
                for i in s:

                    if (i.islower()):
                        l += 1

                    if i.isupper():
                        u += 1

                    if i.isdigit():
                        d += 1

                    if i == '@' or i == '$' or i == '_' or i == '!' or i == '#':
                        p += 1
            if (l + u) >= 8 and l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s):
                return True
            else:
                return False
        else:
            raise Exception("Not a string")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
