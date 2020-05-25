class FibonacciDeath:
    """ Problem Mortal Fibonacci Rabbits
    Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”,
    which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits
    reaches maturity in one month and produces a single pair of offspring (one male, one female)
    each subsequent month. Our aim is to somehow modify this recurrence relation to achieve
    a dynamic programming solution in the case that all rabbits die out after a fixed number
    of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three
    months (meaning that they reproduce only twice before dying).

    Given: Positive integers n≤100 and m≤20.
    Return: The total number of pairs of rabbits that will remain after the n
    -th month if all rabbits live for m-months.

    Sample Dataset
    6 3
    Sample Output
    4
    """

    def __init__(self, month, live):
        """
        Math: f(0) = 1, f(1) = 1, f(n) = f(n-1) + f(n-2) - f(n-(m+1))
        """
        if month < 0 or month > 100:
            raise ValueError("Error: Number of months must be in range [0, 40]")
        if live < 0 or live > 20:
            raise ValueError("Error: Lifetime (in months) must be in range [0, 20].")
        self.__n = month
        self.__m = live
        self.__fib = [1, 1]
        self.__fibonacci()

    def __fibonacci(self):
        for i in range(self.__n - 2):
            if i < self.__m - 2:
                self.__fib.append(self.__fib[-1] + self.__fib[-2])
            elif i == self.__m - 2 or i == self.__m - 1:
                self.__fib.append(self.__fib[-1] + self.__fib[-2] - 1)
            else:
                self.__fib.append(self.__fib[-1] + self.__fib[-2] - self.__fib[-(self.__m + 1)])

    def get_result(self):
        return self.__fib[-1]
