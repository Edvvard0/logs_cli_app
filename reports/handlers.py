from reports.base import BaseReport
from utils.table_models import HandlersColumn, HandlersTable


class HandlersReport(BaseReport):
    def __init__(
            self,
            total_requests: int,
            table: HandlersTable,
            totals_data: HandlersColumn
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


