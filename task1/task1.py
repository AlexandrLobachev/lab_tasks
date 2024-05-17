from collections import deque
from sys import argv


len_array = int(argv[1])
step = int(argv[2])


def main():
    """Основная логика программы."""
    list_for_array = [i for i in range(1, len_array + 1)]
    array = deque(list_for_array)
    path = [array[0]]
    array.rotate(-(step - 1))
    while array[0] != list_for_array[0]:
        path.append(array[0])
        array.rotate(-(step - 1))
    print(''.join([str(num) for num in path]))


if __name__ == '__main__':
    main()
