import argparse
import os

from reports.base import BaseReport
from reports.handlers import HandlersReport


REPORT_CLASSES = {"handlers": HandlersReport}


def validate_files(file_paths: list[str]) -> list[str]:
    """
    Validates a list of file paths, ensuring they exist and are files.

    Args:
        file_paths (list[str]): List of file paths to validate.

    Returns:
        list[str]: List of valid file paths.

    Raises:
        ValueError: If a file path does not exist or is not a file.
    """

    invalid_paths = [path for path in file_paths if not os.path.isfile(path)]
    if invalid_paths:
        raise ValueError(f"The file path is not specified correctly ({invalid_paths})")
    return file_paths


def get_report_class(report_name: str) -> BaseReport:
    """
    Checks if there is such a report in REPORT_CLASSES

    Arguments:
        report_name(str): The name of the report

    Returns:
        BaseReport: a class report that inherits from the BaseReport class

    Raises:
        ValueError: If a report with this name does not exist
    """

    if report_name not in REPORT_CLASSES:
        raise ValueError(f"This report does not exist({report_name})")
    return REPORT_CLASSES[report_name]


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("file_paths", nargs="*")
    parser.add_argument(
        "--report",
        type=str,
        default="handlers",
        help='provide an string (default: "handlers")',
    )
    args = parser.parse_args()

    file_paths = validate_files(args.file_paths)
    report = get_report_class(args.report)

    report = report.create_report(file_paths)
    report.generate()


if __name__ == "__main__":
    main()
