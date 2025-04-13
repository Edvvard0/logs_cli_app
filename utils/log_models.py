from datetime import date, time
from enum import Enum


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
            ip: list[str]
            ):

        self.method = method
        self.endpoint = endpoint
        self.status_code = status_code
        self.status = status
        self.ip = ip


class RequestError:
    def __init__(
            self,
            error: str,
            endpoint: str,
            ip: list[str],
            description: str
    ):
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
            message: RequestInfo | RequestError
            ):

        self.date = date_log
        self.time = time_log
        self.level = level
        self.name_logger = name_logger
        self.message: RequestInfo | RequestError | None = message


