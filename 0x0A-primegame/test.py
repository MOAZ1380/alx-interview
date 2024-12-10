def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def isWinner(x, nums):
    maria = 0
    ben = 0

    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        moves = 0

        while primes:
            moves += 1
            # Remove the smallest prime and all its multiples
            smallest_prime = primes[0]
            primes = [p for p in primes if p % smallest_prime != 0]

        # Determine the winner for this round
        if moves % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None


# Example usage
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

