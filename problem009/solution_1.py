def solution(target_sum: int = 1000) -> int:
    for a in range(1, target_sum // 3):
        for b in range(a + 1, target_sum // 2):
            c = target_sum - a - b
            if b >= c:
                break
            if a*a + b*b == c*c:
                return a * b * c
    raise ValueError("No solution found")

if __name__ == '__main__':
    print(solution())