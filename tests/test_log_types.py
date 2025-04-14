import pytest

from tests.test_main import convert_absolute_path
from utils.log_types import RequestLog


@pytest.mark.parametrize("file_paths", [(["test_data/app1.log"]),
                                        (["test_data/app1.log", "test_data/app2.log"]),
                                        (["test_data/app1.log", "test_data/app2.log", "test_data/app3.log"]),])
def test_convert_log_to_class(file_paths: list[str]):
    file_paths = convert_absolute_path(file_paths)
    logs = RequestLog.convert_log_to_class(file_paths)
    log = logs[0]

    assert log.date == "2025-03-28"
    assert log.time == "12:44:46,000"
    assert log.level == "INFO"
    assert log.name_logger == "django.request:"
    assert log.message.endpoint == "/api/v1/reviews/"

