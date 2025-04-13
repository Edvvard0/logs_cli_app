"""
Я реализовал классы только для RequestInfo и RequestError,
потому что в примерах логов,
которые были, имена эндпоинтов были указанны только в этих уровнях.
Также я не совсем понимаю зачем выводить в таблице остальные уровни,
если я не смогу их никак связать с эндпоинтом и там просто будут 0.
Если я что-то неправильно понял, дайте знать
"""

from datetime import date, time
from enum import Enum

from utils.log_parser import parse_log_files


class LevelEnum(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class HttpMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class RequestInfo:
    def __init__(
        self,
        method: HttpMethods,
        endpoint: str,
        status_code: int,
        status: str,
        ip: list[str],
    ):

        self.method = method
        self.endpoint = endpoint
        self.status_code = status_code
        self.status = status
        self.ip = ip


class RequestError:
    def __init__(self, error: str, endpoint: str, ip: list[str], description: str):
        self.error = error
        self.endpoint = endpoint
        self.ip = ip
        self.description = description


class RequestLog:
    def __init__(
        self,
        date_log: date,
        time_log: time,
        level: LevelEnum,
        name_logger: str,
        message: RequestInfo | RequestError,
    ):

        self.date = date_log
        self.time = time_log
        self.level = level
        self.name_logger = name_logger
        self.message: RequestInfo | RequestError | None = message

    @classmethod
    def convert_log_to_class(cls, file_paths: list[str]):
        logs = parse_log_files(file_paths)

        convert_logs = []

        for log in logs:
            data = list(log.split())
            message = None

            if data[2] == "INFO":
                message = RequestInfo(
                    method=data[4],
                    endpoint=data[5],
                    status_code=data[6],
                    status=data[7],
                    ip=data[8],
                )

            elif data[2] == "ERROR":
                message = RequestError(
                    error=str(data[4] + data[5] + data[6]),
                    endpoint=data[7],
                    ip=data[8],
                    description=str(data[9] + data[10]),
                )

            request_log = RequestLog(
                date_log=data[0],
                time_log=data[1],
                level=data[2],
                name_logger=data[3],
                message=message,
            )
            convert_logs.append(request_log)

        return convert_logs
