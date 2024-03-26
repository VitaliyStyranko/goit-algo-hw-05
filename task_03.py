import sys
import collections


def parse_log_line(line: str) -> dict:
    """Parses a log line and returns a dictionary with extracted components."""
    parts = line.split()
    date, time, level = parts[:3]
    message = " ".join(parts[3:])
    return {"date": date, "time": time, "level": level, "message": message}
    # return dict(date=date, time=time, level=level, message=message)


def load_logs(file_path: str) -> list:
    """Loads logs from a file and returns a list of parsed log entries."""
    try:
        with open(file_path, "r") as file:
            logs = [parse_log_line(line.strip()) for line in file]
        return logs
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found: (file_path)")


def filter_logs_by_level(logs: list, level: str) -> list:
    """Filters logs by the specified level."""
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    """Counts log entries for each logging level."""
    levels = [log["level"] for log in logs]
    return dict(collections.Counter(levels))


def display_log_counts(counts: dict):
    """Displays log counts in a tabular format."""
    print("-" * 23)
    print(f"| {'Level':<8} | {'Count':<5} |")
    # print("|  Level   |  Count | ")
    print("-" * 23)
    for level, count in counts.items():
        print(f"| {level:<8} | {count:<5} |")
    print("-" * 23)


def display_filtered_logs(logs: list):
    """Displays details of filtered logs."""
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Usage: python task_03.py logfile.log [level]")

    log_file = sys.argv[1]
    level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    logs = load_logs(log_file)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nDetails of logs for level '{level}':")
        display_filtered_logs(filtered_logs)
