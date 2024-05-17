from math import sqrt
from sys import argv
from typing import List, Dict

path_circle = argv[1]
path_dot = argv[2]


def read_file(path: str) -> List:
    """Читает файл."""
    with open(path, 'r') as file:
        data = file.read().split('\n')
    return data


def get_circle(data: List) -> Dict:
    """Возвращает словарь с параметрами окружности."""
    x_center, y_center = map(int, data[0].split())
    radius = int(data[1])
    circle = {
        'x_center': x_center,
        'y_center': y_center,
        'radius': radius,
    }
    return circle


def get_dots(data: List) -> Dict:
    """Возвращает словарь с параметрами точек."""
    dots = {}
    number_dot = 1
    for dot in data:
        x_dot, y_dot = map(int, dot.split())
        dots[number_dot] = {
            'x_dot': x_dot,
            'y_dot': y_dot,
        }
        number_dot += 1
    return dots


def check_dot_in_circle(circle: Dict, dots: Dict) -> None:
    """Проверяет принадлежность точки окружности."""
    x_center = circle.get('x_center')
    y_center = circle.get('y_center')
    radius = circle.get('radius')
    for dot in dots.values():
        dist = sqrt( (x_center - dot['x_dot'])**2 + (y_center - dot['y_dot'])**2 )
        if dist < radius:
            print(1)
        elif dist == radius:
                print(0)
        else:
            print(2)


def main():
    """Основная логика программы."""
    circle_data = read_file(path_circle)
    dots_data = read_file(path_dot)
    circle = get_circle(circle_data)
    dots = get_dots(dots_data)
    check_dot_in_circle(circle, dots)



if __name__ == '__main__':
    main()
