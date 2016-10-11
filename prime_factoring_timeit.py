import time

def naive_algorithm(n):
    def is_prime(n):
        return len(naive_algorithm(n)) == 0

    prime_factors = []

    for i in range(1, n):
        if n % i == 0:
            if is_prime(i):
                prime_factors.append(i)

    return prime_factors

def smarter_algorithm(n):
    def is_prime(n):
        for i in range(1, (n//2) + 1):
            if n % i == 0:
                return False

        return True

    prime_factors = []

    for i in range(1, (n//2) + 1):
        if n % i == 0 and is_prime(n):
            prime_factors.append(i)

    return prime_factors

if __name__ == '__main__':
    import timeit

    def timeit_(cmd, setup=None, number=100, print_result=True):
        '''Returns the time it took to run cmd, in milli(?)seconds.'''
        if setup != None:
            result = timeit.timeit(cmd, setup=setup, number=number)
        else:
            result = timeit.timeit(cmd, number=number)

        if print_result:
            formatted_result      = round(result, 2)
            formatted_result_each = round(result / number, 2)
            print("'{cmd}' * {number}: "
                "{formatted_result} seconds, "
                "{formatted_result_each} each".format_map(locals()))

        return result

    timeit_('naive_algorithm(1000)',
        setup='from __main__ import naive_algorithm')

    timeit_('smarter_algorithm(1000)',
        setup='from __main__ import smarter_algorithm')
