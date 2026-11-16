
def primes(start: int, end: int) -> list[int] | None:
    """
    Returns a list of prime numbers between start and end (inclusive).
    If there are no prime numbers in the range, returns None.
    """
    if start > end:
        return None

    prime_numbers = []
    for num in range(start, end + 1):
        if num > 1:  # 0 and 1 are not prime numbers
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)

    return prime_numbers if prime_numbers else None