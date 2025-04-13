# tests/test_log_parser.py

import pytest

from utils.log_parser import parse_log_files


# Фикстура для создания временного файла с тестовыми данными
@pytest.fixture
def test_log_file(tmp_path):
    log_file = tmp_path / "test.log"
    content = (
        "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]\n"
        "\n"  # Пустая строка
        "2025-03-28 12:11:57,000 ERROR django.request: Internal Server Error: /admin/dashboard/ [192.168.1.29] - ValueError: Invalid input data"
    )
    log_file.write_text(content, encoding="utf-8")
    return str(log_file)


def test_parse_log_files_with_existing_files():
    file_paths = ["tests/test_data/app1.log"]
    logs = list(parse_log_files(file_paths))

    assert isinstance(logs, list)
    assert len(logs) == 6  # 6 строк в app1.log
    assert all(isinstance(log, str) for log in logs)
    assert logs[0] == "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]\n"
    assert logs[-1] == "2025-03-28 12:01:42,000 WARNING django.security: IntegrityError: duplicate key value violates unique constraint"


def test_parse_log_files_multiple_files():
    file_paths = [
        "tests/test_data/app1.log",
        "tests/test_data/app2.log",
        "tests/test_data/app3.log",
    ]
    logs = list(parse_log_files(file_paths))

    assert isinstance(logs, list)
    assert len(logs) == 206  # Предполагаем, что все файлы имеют одинаковое содержимое (по 6 строк)
    assert all(isinstance(log, str) for log in logs)


def test_parse_log_files_skips_empty_lines(test_log_file):
    file_paths = [test_log_file]
    logs = list(parse_log_files(file_paths))

    assert len(logs) == 3  # Пустая строка пропущена
    print(logs)
    assert logs[0] == "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]\n"
    assert logs[2] == "2025-03-28 12:11:57,000 ERROR django.request: Internal Server Error: /admin/dashboard/ [192.168.1.29] - ValueError: Invalid input data"


def test_parse_log_files_empty_list():
    file_paths = []
    logs = list(parse_log_files(file_paths))
    assert logs == []