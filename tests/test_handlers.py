import pytest

from reports.handlers import HandlersReport
from tests.test_main import convert_absolute_path


@pytest.mark.parametrize("file_paths, total_requests, info_requests", [(["test_data/app1.log"], 5, 4),
                                              (["test_data/app2.log"], 62, 50, ),
                                              (["test_data/app1.log", "test_data/app2.log"], 67, 54),
                                              (["test_data/app1.log", "test_data/app2.log", "test_data/app3.log"], 133, 104),])
def test_create_report(file_paths: list[str], total_requests, info_requests):
    file_paths = convert_absolute_path(file_paths)
    handler = HandlersReport.create_report(file_paths)

    assert handler.total_requests == total_requests
    assert handler.totals_data.info == info_requests