#!/usr/bin/python3
"""
determining the winner in each round of the prime game
"""


def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    # Find the maximum number in nums to limit our prime calculation
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(max_n ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_n + 1, start):
                sieve[multiple] = False

    # Create a list to track who wins for each n
    maria_wins = [False] * (max_n + 1)
    for n in range(2, max_n + 1):
        # Find all primes up to n
        primes_up_to_n = [
                num for num, is_prime in enumerate(sieve[:n + 1]) if is_prime
                ]
        # Dynamic programming approach to determine winning/losing position
        # True if Maria (first player) has a winning strategy,
        # False if she does not
        for prime in primes_up_to_n:
            if prime <= n and not maria_wins[n - prime]:
                maria_wins[n] = True
                break

    maria_score = 0
    ben_score = 0

    for n in nums:
        if maria_wins[n]:
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
