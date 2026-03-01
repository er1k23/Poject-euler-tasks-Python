def solution(n: int) -> int:
    """Return the sum of all prime numbers below n."""
    if n <= 2:
        return 0

    total = 2
    for i in range(3, n, 2):
        is_prime = True
        for j in range(3, int(i**0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            total += i
    return total

if __name__ == "__main__":
    assert solution(10) == 17
    print(solution(2_000_000))