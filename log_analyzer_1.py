import re

def parse_log_entry(entry):
    match = re.match(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)] (.*)", entry)
    if match:
        timestamp = match.group(1)
        level = match.group(2)
        message = match.group(3)
        return (timestamp, level, message)
    else:
        return None

def summarize_log(log_file):
    total_entries = 0
    entry_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    first_entries = {"INFO": None, "WARNING": None, "ERROR": None}
    last_entries = {"INFO": None, "WARNING": None, "ERROR": None}

    with open(log_file) as f:
        for entry in f:
            total_entries += 1

            parsed_entry = parse_log_entry(entry)
            if parsed_entry:
                timestamp, level, message = parsed_entry

                entry_counts[level] += 1

                if not first_entries[level]:
                    first_entries[level] = timestamp

                last_entries[level] = timestamp

    print("Total number of log entries:", total_entries)
    print()

    for level, count in entry_counts.items():
        print("Level:", level)
        print("Number of entries:", count)
        print("First entry timestamp:", first_entries[level])
        print("Last entry timestamp:", last_entries[level])
        print()

if __name__ == "__main__":
    summarize_log("./logs/system.log")
