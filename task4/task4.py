from sys import argv
from statistics import median
from typing import List

path_file = argv[1]


def read_file(path: str) -> List:
    """Читает файл."""
    with open(path, 'r') as file:
        data = file.read().split('\n')
    int_data = [int(num) for num in data]
    return int_data


def calc_moves(nums: List) -> int:
    """Считает количество шагов."""
    median_nums = median(nums)
    steps_count = 0
    for num in nums:
        steps_count += abs(median_nums - num)
    return int(steps_count)


def main():
    nums = read_file(path_file)
    print(calc_moves(nums))


if __name__ == '__main__':
    main()
