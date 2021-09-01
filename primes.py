'''
An implementation of the Sieve of Eratosthenes in Python
'''

from math import sqrt
from time import perf_counter as pc


def get_user_input():
    print('\n All the primes from 2 up to the integer entered will be returned.')
    N = input(" enter a positive integer: ")
    return int(N)

def sieve(N):
    '''Create an array that will have True at prime-numbered indices 
    and False everywhere else.'''
    arr = [True] * (N + 1)
    arr[0], arr[1] = False, False

    for idx in range(2, int(sqrt(N))+ 1):
        if arr[idx]:
            k = 0
            jdx = idx ** 2
            while jdx <= N:
                arr[jdx] = False
                k += 1
                jdx = idx ** 2 + idx * k
    return arr

def primed(arr):
    '''Take the Boolean array returned from sieve(),
    and return the list of primes up to N.'''
    return [idx for idx in range(len(arr)) if arr[idx]]


def pretty_print(lst, N):
    nr_of_primes = len(lst)
    print(f" the {nr_of_primes} primes from 2 to {N} are\n ")
    for idx in range(len(lst)):
        string = str(lst[idx]).rjust(8)
        if not (idx + 1) % 6:
            string += '\n'
        print(string, end='')
    print('\n\n')


if __name__ == '__main__':
    N = get_user_input()
    t0 = pc()
    list_of_primes = primed(sieve(N)) 
    t1 = pc() - t0
    pretty_print(list_of_primes, N)
    print(' time:  ', t1, ' sec',  '\n')

