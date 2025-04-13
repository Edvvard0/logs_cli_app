from reports.base import BaseReport
from utils.log_types import RequestLog
from tables.handlers_table import HandlersColumn, HandlersTable


class HandlersReport(BaseReport):
    def __init__(
        self, total_requests: int, table: HandlersTable, totals_data: HandlersColumn
    ):
        self.total_requests = total_requests
        self.table = table
        self.totals_data = totals_data

    def generate(self):
        print(f"Total requests: {self.total_requests}")
        print("-" * 60)

        print(self.table.fields)
        for column in self.table.columns:
            print(column.convert_columns())

        print("-" * 60)
        print(self.totals_data.convert_columns())


    @classmethod
    def create_report(cls, file_paths: list[str]):
        table = HandlersTable()
        logs = RequestLog.convert_log_to_class(file_paths)
        totals = HandlersColumn()
        total_requests = 0
        handlers_data = {}

        for log in logs:
            if log.message:
                endpoint = log.message.endpoint

                if endpoint not in handlers_data:
                    column = HandlersColumn(handler=endpoint)
                    handlers_data[endpoint] = column

                level = str(log.level)

                column.level_increment(level)
                totals.level_increment(level)
                total_requests += 1

        handlers_data = dict(sorted(handlers_data.items()))
        table.columns = list(handlers_data.values())
        handlers = HandlersReport(
            total_requests=total_requests, table=table, totals_data=totals
        )
        return handlers
