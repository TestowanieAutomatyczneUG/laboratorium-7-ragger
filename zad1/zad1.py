

class FizzBuzz:
    def game(self, num):
        """
        >>> g = FizzBuzz()
        >>> g.game(5)
        'Buzz'
        >>> g.game(15)
        'FizzBuzz'
        >>> g.game(3)
        'Fizz'
        >>> g.game(3.0)
        'Fizz'
        >>> g.game(-5)
        'Buzz'
        >>> g.game(17)
        '17'
        >>> g.game("x")
        Traceback (most recent call last):
        ...
        Exception: Error in FizBuzz
        >>> g.game([3])
        Traceback (most recent call last):
        ...
        Exception: Error in FizBuzz
        >>> g.game({3})
        Traceback (most recent call last):
        ...
        Exception: Error in FizBuzz
        >>> g.game(None)
        Traceback (most recent call last):
        ...
        Exception: Error in FizBuzz
        >>> g.game(3.71)
        '3.71'
        >>> g.game(50625.0)
        'FizzBuzz'
        """

        if not isinstance(num, (int, float)):
            raise Exception("Error in FizBuzz")
        if (float(num) % 15) == 0:
            return "FizzBuzz"
        elif (float(num) % 5) == 0:
            return "Buzz"
        elif (float(num) % 3) == 0:
            return "Fizz"
        elif isinstance(num, str):
            return int(num)
        else:
            return ('' + str(num) + '')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
