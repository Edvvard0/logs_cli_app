import os

import pytest

from main import validate_files, get_report_class
from reports.handlers import HandlersReport


def convert_absolute_path(file_paths: list[str]) -> list[str]:
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_paths = [os.path.join(tests_dir, path) for path in file_paths]
    return absolute_paths


@pytest.mark.parametrize("file_paths", [(["test_data/app1.log"]),
                                              (["test_data/app2.log"]),
                                              (["test_data/app1.log", "test_data/app2.log"]),
                                              (["test_data/app1.log", "test_data/app2.log", "test_data/app3.log"]),])
def test_validate_correct_files(file_paths):
    file_paths = convert_absolute_path(file_paths)
    print(file_paths)
    assert validate_files(file_paths) is None


@pytest.mark.parametrize("file_paths", [(["test_data/not_correct.log"]),
                                              (["test_data/app1.log", "test_data/not_correct.log"]),
                                              (["test_data/app1.log", "test_data/app2.log", "test_data/not_correct.log"]),])
def test_validate_not_correct_files(file_paths):
    with pytest.raises(ValueError):
        validate_files(file_paths)


@pytest.mark.parametrize("report_name", [("handlers"),])
def test_get_report_class(report_name):
    assert get_report_class(report_name) == HandlersReport


@pytest.mark.parametrize("report_name", [("no_correct"),])
def test_not_correct_report_class(report_name):
    with pytest.raises(ValueError):
        get_report_class(report_name)