import json
from typing import Dict, List
from sys import argv


tests_path = argv[1]
values_path = argv[2]
report_path = argv[3]


def open_json(path: str) -> Dict:
    """Открывает JSON файл."""
    with open(file=path, mode='r', encoding='utf-8') as file:
        return json.load(file)


def save_json(path: str, data: Dict) -> None:
    """Сохраняет данные в JSON файл."""
    with open(file=path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def filling(tests: List, values: Dict) -> List:
    """Заполняет шаблон результатами."""
    for test in tests:
        test['value'] = values.get(test['id'], 'Результат теста не найден')
        nested_tests = test.get('values')
        if nested_tests:
            filling(nested_tests, values)
    return tests


def get_dict_values(values: List) -> Dict:
    """Трансформирует список словарей результатов в словарь с результатами."""
    return {value['id']: value['value'] for value in values}


def main():
    """Основная логика программы."""
    values = open_json(values_path).get('values')
    tests = open_json(tests_path).get('tests')
    dict_values = get_dict_values(values)
    report = dict(tests = filling(tests, dict_values))
    save_json(report_path, report)


if __name__ == '__main__':
    main()
