from utils.log_models import RequestError, RequestInfo, RequestLog
from utils.parser import pars_log_file


def convert_log_to_class(lst_file_path: list[str]) -> list[RequestLog]:
    logs = []
    for file_path in lst_file_path:
        logs.extend(pars_log_file(file_path=file_path))


    # print(logs)
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
                description=str(data[9] + data[10])
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


# print(convert_log_to_class(["../app1.log", "../app2.log"]))
