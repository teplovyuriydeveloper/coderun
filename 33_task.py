import sys

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    first_string = input()
    second_string = input()

    n, m = len(first_string), len(second_string)

    if n > m:
        first_string, second_string = second_string, first_string
        n, m = m, n

    prev = list(range(n + 1))
    for i in range(1, m+1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            cost = 0 if first_string[j-1] == second_string[i-1] else 1
            curr[j] = min(
                prev[j] + 1,
                curr[j-1] + 1,
                prev[j-1] + cost
            )
        
        prev = curr

    print(prev[-1])

if __name__ == '__main__':
    main()