def parse_log_files(file_paths: list[str]) -> list[str]:
    """
    Reads log files and returns their contents as a list of strings.

    Args:
        file_paths (list[str]): List of file paths to the log files.

    Returns:
        list[str]: List of log entries.
    """

    logs = []
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as f:
            log = f.readlines()
        logs.extend(log)

    return logs

