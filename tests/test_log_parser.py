import pytest

from tests.test_main import convert_absolute_path
from utils.log_parser import parse_log_files


@pytest.mark.parametrize("file_paths, lines", [(["test_data/app1.log"], 6),
                                              (["test_data/app2.log"], 100),
                                              (["test_data/app1.log", "test_data/app2.log"], 106),
                                              (["test_data/app1.log", "test_data/app2.log", "test_data/app3.log"], 206),])
def test_log_parse_log_files(file_paths, lines):
    file_paths = convert_absolute_path(file_paths)
    assert len(parse_log_files(file_paths)) == lines