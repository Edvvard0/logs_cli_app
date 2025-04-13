from reports.handlers import HandlersReport
from utils.convert_log_to_class import convert_log_to_class
from utils.table_models import HandlersColumn, HandlersTable


def create_handlers(lst_file_path: list[str]) -> HandlersReport:
    table = HandlersTable()
    logs = convert_log_to_class(lst_file_path)
    totals = HandlersColumn()
    # print(logs)
    total_requests = 0
    res = {}

    for log in logs:
        if log.message:
            endpoint = log.message.endpoint

            if endpoint not in res:
                column = HandlersColumn(
                    handler=endpoint
                )
                res[endpoint] = column

            level = str(log.level)

            column.level_increment(level)
            totals.level_increment(level)
            total_requests += 1


    table.columns = list(res.values())
    handlers = HandlersReport(
        total_requests=total_requests,
        table=table,
        totals_data=totals
    )
    return handlers


# handler = create_hendlers("../app1.log")
# handler.generate()
#
# handler2 = create_hendlers("../app2.log")
# handler2.generate()
#
#
# HandlersReport.merge_handlers([handler, handler2])
