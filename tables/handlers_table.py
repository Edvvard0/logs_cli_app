from tables.base_table import BaseTable


class HandlersColumn:
    handler_width = 20
    value_width = 8

    def __init__(
        self,
        handler: str = "",
        debug: int = 0,
        info: int = 0,
        warning: int = 0,
        error: int = 0,
        critical: int = 0,
    ):

        self.handler = handler
        self.debug = debug
        self.info = info
        self.warning = warning
        self.error = error
        self.critical = critical

    def level_increment(self, level: str, value: int = 1):
        if level == "DEBUG":
            self.debug += value
        elif level == "INFO":
            self.info += value
        elif level == "WARNING":
            self.warning += value
        elif level == "ERROR":
            self.error += value
        elif level == "CRITICAL":
            self.critical += value

    def convert_columns(self):
        row = (
            f"{self.handler:<{self.handler_width}}"
            f"{self.debug:^{self.value_width}}"
            f"{self.info:^{self.value_width}}"
            f"{self.warning:^{self.value_width}}"
            f"{self.error:^{self.value_width}}"
            f"{self.critical:^{self.value_width}}"
        )
        return row


class HandlersTable(BaseTable):
    handler_width = 20
    value_width = 8
    fields = (
        f"{'HANDLER':<{handler_width}}"
        f"{'DEBUG':^{value_width}}"
        f"{'INFO':^{value_width}}"
        f"{'WARNING':^{value_width}}"
        f"{'ERROR':^{value_width}}"
        f"{'CRITICAL':^{value_width}}"
    )
    columns: list[HandlersColumn] = []

    @classmethod
    def get_columns(cls) -> list[HandlersColumn]:
        return cls.columns

