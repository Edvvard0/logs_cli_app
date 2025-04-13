from abc import abstractmethod, ABC


class BaseReport(ABC):
    @abstractmethod
    def generate(self) -> None:
        """print a report"""
        pass

    @classmethod
    @abstractmethod
    def create_report(cls, lst_file_path: list[str]):
        """
        Сreates a report
        Args:
            file_paths (list[str]): List of file paths to the log files.

        Returns:
            report: (BaseReport)
        """
        pass
