import argparse
import os
from typing import Type

from reports.base import BaseReport
from reports.handlers import HandlersReport
from utils.create_handlers import create_handlers

REPORT_CLASSES: dict[str, Type[BaseReport]] = {
    "handlers": HandlersReport
}

def validate_files(file_paths: list[str]) -> list[str]:
    valid_paths = []
    for path in file_paths:
        if not os.path.isfile(path):
            raise ValueError(f"путь к файлу указан не корректно ({path})")
        else:
            valid_paths.append(path)
    return valid_paths


def validate_reports(report: str):
    if report not in REPORT_CLASSES:
        raise ValueError(f"Данного отчета не существует ({report})")


def main():
    parser = argparse.ArgumentParser(description='My example explanation')

    parser.add_argument('file_names', nargs='*')
    parser.add_argument(
        '--report',
        type=str,
        default="handlers",
        help='provide an string (default: "handlers")'
    )
    args = parser.parse_args()

    # print(args.file_names)
    lst_filenames = validate_files(args.file_names)
    validate_reports(args.report)

    # convert_data = convert_log_to_class(lst_filenames)
    # print(convert_data)
    create_handlers(lst_filenames)
    handler = create_handlers(lst_filenames)
    handler.generate()


if __name__ == "__main__":
    main()