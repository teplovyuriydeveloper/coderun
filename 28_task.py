import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())

    numbers = input().split()

    dp = [[] for _ in range(n)]


    for i in range(0, n):
        max_list = []
        max_list.append(int(numbers[i]))
        for j in range(i, -1, -1):
            if int(numbers[i]) > int(numbers[j]):
                if len(max_list) <= (len(dp[j]) + 1):
                    max_list = dp[j] + [int(numbers[i])] 
        dp[i] = max_list

    max_i = 0

    for i in range(n):
        if len(dp[i]) > len(dp[max_i]):
            max_i = i

    print(' '.join(map(str, dp[max_i])))


if __name__ == '__main__':
    main()
