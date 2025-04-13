# tests/test_cli.py

import pytest
import sys
from unittest.mock import patch, MagicMock

from main import validate_files, get_report_class, main, REPORT_CLASSES


# Тесты для validate_files
def test_validate_files_with_existing_files(tmp_path):
    # Создаём временный файл
    log_file = tmp_path / "test.log"
    log_file.write_text("test content", encoding="utf-8")

    file_paths = [str(log_file)]
    result = validate_files(file_paths)
    assert result == file_paths


def test_validate_files_with_nonexistent_files():
    file_paths = ["nonexistent.log"]
    with pytest.raises(ValueError, match="The file path is not specified correctly \\(\\['nonexistent.log'\\]\\)"):
        validate_files(file_paths)


def test_validate_files_with_directory(tmp_path):
    # Создаём временную директорию
    directory = tmp_path / "test_dir"
    directory.mkdir()

    file_paths = [str(directory)]
    with pytest.raises(ValueError):
        validate_files(file_paths)


def test_validate_files_mixed(tmp_path):
    # Создаём один существующий файл и один несуществующий
    log_file = tmp_path / "test.log"
    log_file.write_text("test content", encoding="utf-8")

    file_paths = [str(log_file), "nonexistent.log"]
    with pytest.raises(ValueError, match="The file path is not specified correctly \\(\\['nonexistent.log'\\]\\)"):
        validate_files(file_paths)


# Тесты для get_report_class
def test_get_report_class_valid():
    report_class = get_report_class("handlers")
    assert report_class == REPORT_CLASSES["handlers"]


def test_get_report_class_invalid():
    with pytest.raises(ValueError, match="This report does not exist\\(invalid_report\\)"):
        get_report_class("invalid_report")


# Тесты для main
@patch("main.get_report_class")
@patch("sys.argv", ["main.py", "tests/test_data/app1.log", "--report", "handlers"])
def test_main_successful_execution(mock_get_report_class):
    # Мокаем report_class и его методы
    mock_report_instance = MagicMock()
    mock_get_report_class.return_value.create_report.return_value = mock_report_instance

    main()

    # Проверяем, что методы были вызваны
    mock_get_report_class.assert_called_once_with("handlers")
    mock_get_report_class.return_value.create_report.assert_called_once_with(["tests/test_data/app1.log"])
    mock_report_instance.generate.assert_called_once()


@patch("main.get_report_class")
@patch("sys.argv", ["main.py", "--report", "handlers"])
def test_main_empty_file_paths(mock_get_report_class):
    # Проверяем, что validate_files не вызывает исключение при пустом списке
    main()

    # Проверяем, что get_report_class был вызван
    mock_get_report_class.assert_called_once_with("handlers")
    mock_get_report_class.return_value.create_report.assert_called_once_with([])


@patch("sys.argv", ["main.py", "nonexistent.log", "--report", "handlers"])
def test_main_invalid_file_paths():
    with pytest.raises(ValueError, match="The file path is not specified correctly \\(\\['nonexistent.log'\\]\\)"):
        main()


@patch("main.get_report_class")
@patch("sys.argv", ["main.py", "tests/test_data/app1.log", "--report", "invalid_report"])
def test_main_invalid_report(mock_get_report_class):
    mock_get_report_class.side_effect = ValueError("This report does not exist(invalid_report)")

    with pytest.raises(ValueError, match="This report does not exist\\(invalid_report\\)"):
        main()


@patch("main.get_report_class")
@patch("sys.argv", ["main.py", "tests/test_data/app1.log"])
def test_main_default_report(mock_get_report_class):
    # Мокаем report_class и его методы
    mock_report_instance = MagicMock()
    mock_get_report_class.return_value.create_report.return_value = mock_report_instance

    main()

    # Проверяем, что get_report_class вызван с де