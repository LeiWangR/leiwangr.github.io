# ============================================================
# MISSION CONTROL v9.0
# Week 9: Sets and Dictionaries
# Based on Mission Control v8.0
# ============================================================

import sys

HISTORY_FILE = "mission_history.txt"
REPORT_FILE = "mission_report.txt"


def show_header(title):
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


def classify_temperature(temperature):
    if temperature < 0:
        return "INVALID"
    elif temperature >= 100:
        return "CRITICAL"
    elif temperature > 80:
        return "WARNING"
    else:
        return "SAFE"


def format_reading(reading):
    sensor_number, temperature, status = reading
    return f"Sensor {sensor_number:<2} | {temperature:>6.1f} C | {status:<8}"


def load_history(filename):
    reading_history = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                if len(parts) != 3:
                    print(
                        f"Warning: skipped malformed line: {line}",
                        file=sys.stderr
                    )
                    continue

                try:
                    sensor_number = int(parts[0])
                    temperature = float(parts[1])
                    status = parts[2]

                    if status not in ("SAFE", "WARNING", "CRITICAL"):
                        raise ValueError("invalid status")

                    reading = (sensor_number, temperature, status)
                    reading_history.append(reading)

                except ValueError:
                    print(
                        f"Warning: skipped invalid reading: {line}",
                        file=sys.stderr
                    )

    except FileNotFoundError:
        print("No existing history file found. Starting a new mission log.")

    return reading_history


def append_history(filename, readings):
    with open(filename, "a") as file:
        for sensor_number, temperature, status in readings:
            file.write(
                f"{sensor_number}|{temperature}|{status}\n"
            )


def save_report(filename, report_lines):
    with open(filename, "w") as file:
        file.write("\n".join(report_lines))
        file.write("\n")


def create_new_report(filename, report_lines):
    try:
        with open(filename, "x") as file:
            file.write("\n".join(report_lines))
            file.write("\n")
        print(f"New report created: {filename}")
    except FileExistsError:
        print(
            f"Report '{filename}' already exists. "
            "Use the save command to replace it."
        )


def scan_sensors():
    scan_readings = []
    safe_count = 0
    warning_count = 0

    for sensor_number in range(1, 6):
        while True:
            try:
                temperature = float(
                    input(f"Sensor {sensor_number} temperature: ")
                )
                break
            except ValueError:
                print("Invalid temperature. Please enter a number.")

        status = classify_temperature(temperature)

        if status == "INVALID":
            print("Invalid reading - skipped.")
            continue

        reading = (sensor_number, temperature, status)
        scan_readings.append(reading)

        if status == "CRITICAL":
            print("CRITICAL - scan stopped")
            warning_count += 1
            break
        elif status == "WARNING":
            print("WARNING")
            warning_count += 1
        else:
            print("SAFE")
            safe_count += 1

    return scan_readings, safe_count, warning_count


# ---------------------------------------------------------------------
# Week 9: Sets
# ---------------------------------------------------------------------

def get_observed_statuses(reading_history):
    """Return the distinct statuses currently present in the history."""
    return {reading[2] for reading in reading_history}


def get_sensor_numbers(reading_history):
    """Return the distinct sensor numbers currently present in the history."""
    return {reading[0] for reading in reading_history}


def show_sets(reading_history):
    """Use sets to analyse distinct mission values."""
    print("\n--- SET ANALYSIS ---")

    observed_statuses = get_observed_statuses(reading_history)
    all_statuses = {"SAFE", "WARNING", "CRITICAL"}

    print(f"Observed statuses: {sorted(observed_statuses)}")
    print(f"All possible statuses: {sorted(all_statuses)}")

    print(
        "Statuses not yet observed:",
        sorted(all_statuses - observed_statuses)
    )

    print(
        "Statuses shared by both sets:",
        sorted(all_statuses & observed_statuses)
    )

    print(
        "Are all possible statuses represented?",
        observed_statuses == all_statuses
    )

    sensor_numbers = get_sensor_numbers(reading_history)
    required_sensors = set(range(1, 6))

    print(f"Observed sensors: {sorted(sensor_numbers)}")
    print(
        "Are all five sensors represented?",
        required_sensors <= sensor_numbers
    )

    if required_sensors.isdisjoint(sensor_numbers):
        print("No required sensor has been observed.")
    else:
        print("At least one required sensor has been observed.")


def demonstrate_set_methods():
    """Demonstrate the main set operations and methods from Week 9."""
    print("\n--- SET METHODS DEMO ---")

    s1 = {"SAFE", "WARNING"}
    s2 = {"WARNING", "CRITICAL"}

    print(f"s1: {sorted(s1)}")
    print(f"s2: {sorted(s2)}")

    # Non-mutating set operations.
    print("Union:", sorted(s1 | s2))
    print("Intersection:", sorted(s1 & s2))
    print("Difference s1 - s2:", sorted(s1 - s2))
    print("Symmetric difference:", sorted(s1 ^ s2))

    # Set comparisons.
    print("s1 subset of s2:", s1 <= s2)
    print("s1 proper subset of s2:", s1 < s2)
    print("s1 superset of s2:", s1 >= s2)
    print("s1 proper superset of s2:", s1 > s2)
    print("s1 and s2 disjoint:", s1.isdisjoint(s2))

    # Mutating operations.
    working = set(s1)
    working.update(s2)
    print("After update():", sorted(working))

    working = set(s1)
    working.intersection_update(s2)
    print("After intersection_update():", sorted(working))

    working = set(s1)
    working.difference_update(s2)
    print("After difference_update():", sorted(working))

    working = set(s1)
    working.symmetric_difference_update(s2)
    print("After symmetric_difference_update():", sorted(working))

    # Individual-element methods.
    working = {"SAFE", "WARNING"}
    print("Starting individual-method set:", sorted(working))

    working.add("CRITICAL")
    print("After add('CRITICAL'):", sorted(working))

    working.discard("MAINTENANCE")
    print("After discard('MAINTENANCE'):", sorted(working))

    working.remove("WARNING")
    print("After remove('WARNING'):", sorted(working))

    removed = working.pop()
    print("pop() removed:", removed)
    print("After pop():", sorted(working))

    working.clear()
    print("After clear():", sorted(working))

    # Shorthand assignment operators.
    a = {1, 2, 3}
    b = {3, 4}

    a |= b
    print("After |=:", sorted(a))

    a = {1, 2, 3}
    a &= b
    print("After &=:", sorted(a))

    a = {1, 2, 3}
    a -= b
    print("After -=:", sorted(a))


# ---------------------------------------------------------------------
# Week 9: Dictionaries
# ---------------------------------------------------------------------

def demonstrate_dictionary_methods():
    """Demonstrate the main dictionary operations and methods from Week 9."""
    print("\n--- DICTIONARY METHODS DEMO ---")

    data = {"SAFE": 5, "WARNING": 2}
    print("Starting dictionary:", data)

    # [] can add a new key or replace the value of an existing key.
    data["CRITICAL"] = 1
    data["SAFE"] = 6
    print("After [] assignment:", data)

    print("keys():", list(data.keys()))
    print("values():", list(data.values()))
    print("items():", list(data.items()))

    # get() avoids a KeyError when a key may be absent.
    print("get('SAFE'):", data.get("SAFE"))
    print("get('MAINTENANCE'):", data.get("MAINTENANCE"))
    print("get('MAINTENANCE', 0):", data.get("MAINTENANCE", 0))

    # setdefault() keeps an existing value, or inserts a default.
    data.setdefault("WARNING", 0)
    data.setdefault("MAINTENANCE", 0)
    print("After setdefault():", data)

    # update() adds/replaces several key-value pairs.
    data.update({"SAFE": 7, "OTHER": 0})
    print("After update():", data)

    # pop() returns and removes a selected key.
    removed = data.pop("OTHER")
    print("pop('OTHER') returned:", removed)
    print("After pop():", data)

    # popitem() returns and removes one key-value pair.
    removed_pair = data.popitem()
    print("popitem() returned:", removed_pair)
    print("After popitem():", data)

    # del removes a selected entry.
    del data["CRITICAL"]
    print("After del data['CRITICAL']:", data)

    # fromkeys() creates a new dictionary from an iterable of keys.
    template = dict.fromkeys(
        ["SAFE", "WARNING", "CRITICAL"], 0
    )
    print("fromkeys():", template)

    # | merges two dictionaries. If a key occurs in both,
    # the value from the right-hand dictionary is used.
    left = {"SAFE": 5, "WARNING": 2}
    right = {"WARNING": 3, "CRITICAL": 1}
    merged = left | right
    print("Merged with |:", merged)

    data.clear()
    print("After clear():", data)


def build_status_counts(reading_history):
    """Build a dictionary mapping each status to its frequency."""
    counts = {}

    for reading in reading_history:
        status = reading[2]
        counts[status] = counts.get(status, 0) + 1

    return counts


def build_sensor_counts(reading_history):
    """Build a dictionary mapping each sensor number to its reading count."""
    counts = {}

    for reading in reading_history:
        sensor_number = reading[0]
        counts[sensor_number] = counts.get(sensor_number, 0) + 1

    return counts


def build_latest_readings(reading_history):
    """Build a dictionary mapping each sensor to its latest reading."""
    latest = {}

    for reading in reading_history:
        sensor_number = reading[0]
        latest[sensor_number] = reading

    return latest


def show_dictionaries(reading_history):
    """Use dictionaries to organise and summarise mission data."""
    print("\n--- DICTIONARY ANALYSIS ---")

    status_counts = build_status_counts(reading_history)
    sensor_counts = build_sensor_counts(reading_history)
    latest = build_latest_readings(reading_history)

    print("\nStatus counts:")
    if status_counts:
        for status in sorted(status_counts):
            print(f"{status:<10} {status_counts[status]}")
    else:
        print("No readings yet.")

    print("\nSensor reading counts:")
    if sensor_counts:
        for sensor_number in sorted(sensor_counts):
            print(
                f"Sensor {sensor_number}: "
                f"{sensor_counts[sensor_number]}"
            )
    else:
        print("No readings yet.")

    print("\nLatest reading for each sensor:")
    if latest:
        for sensor_number in sorted(latest):
            print(format_reading(latest[sensor_number]))
    else:
        print("No readings yet.")

    print("\nDictionary views:")
    print(f"Keys:   {sorted(status_counts.keys())}")
    print(f"Values: {list(status_counts.values())}")
    print(f"Items:  {sorted(status_counts.items())}")

    print("\nSafe lookup with get():")
    print(f"CRITICAL count: {status_counts.get('CRITICAL', 0)}")
    print(
        "MAINTENANCE count:",
        status_counts.get("MAINTENANCE", 0)
    )


# ---------------------------------------------------------------------
# Week 9: Comprehensions and references
# ---------------------------------------------------------------------

def show_comprehensions(reading_history):
    """Demonstrate set and dictionary comprehensions."""
    print("\n--- COMPREHENSION EXAMPLES ---")

    safe_sensors = {
        reading[0]
        for reading in reading_history
        if reading[2] == "SAFE"
    }

    average_by_sensor = {}

    for reading in reading_history:
        sensor_number = reading[0]
        temperature = reading[1]

        if sensor_number not in average_by_sensor:
            average_by_sensor[sensor_number] = []

        average_by_sensor[sensor_number].append(temperature)

    average_by_sensor = {
        sensor: sum(values) / len(values)
        for sensor, values in average_by_sensor.items()
    }

    print(
        "Sensors with at least one SAFE reading:",
        sorted(safe_sensors)
    )

    print("Average temperature by sensor:")
    if average_by_sensor:
        for sensor in sorted(average_by_sensor):
            print(
                f"Sensor {sensor}: "
                f"{average_by_sensor[sensor]:.1f} C"
            )
    else:
        print("No readings yet.")


def show_reference_demo():
    """Show aliasing, mutation and reassignment."""
    print("\n--- REFERENCE DEMO ---")

    readings = [1, 2]
    mission_readings = readings

    print(f"Before mutation: readings = {readings}")
    print(f"Before mutation: mission_readings = {mission_readings}")

    readings.append(3)

    print(f"After readings.append(3): readings = {readings}")
    print(
        "After mutation, mission_readings = "
        f"{mission_readings}"
    )

    new_readings = [10, 20]
    readings = new_readings

    print(f"After reassignment: readings = {readings}")
    print(
        "mission_readings still refers to the old list: "
        f"{mission_readings}"
    )


# ---------------------------------------------------------------------
# Existing Mission Control features from earlier weeks
# ---------------------------------------------------------------------

def show_report(reading_history):
    print("\n--- CURRENT REPORT ---")
    total_valid = len(reading_history)
    print(f"Valid readings: {total_valid}")

    if not reading_history:
        print("No valid sensor data yet.")
        return []

    temperatures = [reading[1] for reading in reading_history]
    statuses = [reading[2] for reading in reading_history]

    safe_count = statuses.count("SAFE")
    warning_count = statuses.count("WARNING")
    critical_count = statuses.count("CRITICAL")

    average = sum(temperatures) / len(temperatures)

    report_lines = [
        "--- CURRENT REPORT ---",
        f"Valid readings: {total_valid}",
        f"Safe readings: {safe_count}",
        f"Warnings: {warning_count}",
        f"Critical readings: {critical_count}",
        f"Average: {average:.1f} C",
        f"Highest: {max(temperatures):.1f} C",
        f"Lowest: {min(temperatures):.1f} C"
    ]

    for line in report_lines[1:]:
        print(line)

    return report_lines


def show_history(reading_history):
    print("\n--- READING HISTORY ---")

    if not reading_history:
        print("No valid sensor readings recorded.")
        return

    lines = []

    for reading in reading_history:
        lines.append(format_reading(reading))

    print("\n".join(lines))


def show_recent(reading_history):
    print("\n--- RECENT READINGS ---")

    recent_readings = reading_history[-3:]

    if not recent_readings:
        print("No valid sensor readings recorded.")
        return

    for reading in recent_readings:
        print(format_reading(reading))


def show_status(reading_history, required_status):
    matching_readings = [
        reading
        for reading in reading_history
        if reading[2] == required_status
    ]

    print(f"\n--- {required_status} READINGS ---")

    if not matching_readings:
        print(f"No {required_status} readings recorded.")
        return

    for reading in matching_readings:
        print(format_reading(reading))


def show_highest_three(reading_history):
    print("\n--- HIGHEST THREE TEMPERATURES ---")

    if not reading_history:
        print("No valid sensor readings recorded.")
        return

    temperatures = [reading[1] for reading in reading_history]
    temperatures.sort()

    for temperature in temperatures[-3:][::-1]:
        print(f"{temperature:.1f} C")


def show_mission(mission_name, destination):
    print("\n--- MISSION INFORMATION ---")
    print(f"Mission: {mission_name}")
    print(f"Destination: {destination}")

    if len(mission_name) >= 3:
        print(f"Mission code: {mission_name[:3].upper()}")
    else:
        print("Mission code: " + mission_name.upper())


def search_history(reading_history):
    keyword = input("Search text: ").strip().lower()

    if keyword == "":
        print("Search text cannot be empty.")
        return

    matches = []

    for reading in reading_history:
        line = format_reading(reading)

        if keyword in line.lower():
            matches.append(line)

    print("\n--- SEARCH RESULTS ---")

    if not matches:
        print("No matching readings found.")
    else:
        print("\n".join(matches))


def status_command(reading_history):
    status = input(
        "Enter status (SAFE/WARNING/CRITICAL): "
    ).strip().upper()

    if status in ("SAFE", "WARNING", "CRITICAL"):
        show_status(reading_history, status)
    else:
        print("Invalid status.")


def build_log_lines(reading_history):
    lines = []

    for reading in reading_history:
        lines.append(format_reading(reading))

    return lines


def show_log(reading_history):
    print("\n--- MISSION LOG ---")

    if not reading_history:
        print("No valid sensor readings recorded.")
        return

    lines = build_log_lines(reading_history)
    log = "\n".join(lines)

    print(log)
    print(f"\nLog contains {len(lines)} readings.")


def save_current_report(reading_history):
    report_lines = show_report(reading_history)

    if not report_lines:
        return

    save_report(REPORT_FILE, report_lines)
    print(f"Report saved to {REPORT_FILE}.")


def create_report_file(reading_history):
    report_lines = show_report(reading_history)

    if not report_lines:
        return

    create_new_report(REPORT_FILE, report_lines)


def show_file_preview(filename):
    print(f"\n--- FILE PREVIEW: {filename} ---")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if not lines:
            print("File is empty.")
            return

        print(f"Lines in file: {len(lines)}")
        print("First two lines:")

        for line in lines[:2]:
            print(line.rstrip())

        if len(lines) > 2:
            print("Last two lines:")

            for line in lines[-2:]:
                print(line.rstrip())

    except FileNotFoundError:
        print(f"File '{filename}' was not found.")


def reset_history(filename):
    with open(filename, "w") as file:
        file.write("")

    print(f"History file '{filename}' has been cleared.")


def show_help():
    command_text = (
        "scan report history recent safe warning critical "
        "sets setmethods dictionaries dictmethods comprehensions "
        "references top3 mission search status log save newreport "
        "preview reset help shutdown"
    )

    commands = command_text.split()

    print("\n--- AVAILABLE COMMANDS ---")
    print(" | ".join(commands))


def run_mission_control():
    reading_history = load_history(HISTORY_FILE)

    mission_name = input("Mission name: ").strip().title()
    destination = input("Destination: ").strip().title()

    show_header(f"MISSION CONTROL v9.0 — {mission_name}")
    print(f"Destination: {destination}")
    print(f"Loaded {len(reading_history)} historical readings.")

    while True:
        command = input(
            "\nCommand [scan/report/history/recent/safe/warning/"
            "critical/sets/setmethods/dictionaries/dictmethods/"
            "comprehensions/references/top3/mission/search/status/"
            "log/save/newreport/preview/reset/help/shutdown]: "
        ).strip().lower()

        if command == "shutdown":
            print("Shutting down Mission Control...")
            break

        if command == "report":
            show_report(reading_history)
            continue

        if command == "history":
            show_history(reading_history)
            continue

        if command == "recent":
            show_recent(reading_history)
            continue

        if command == "safe":
            show_status(reading_history, "SAFE")
            continue

        if command == "warning":
            show_status(reading_history, "WARNING")
            continue

        if command == "critical":
            show_status(reading_history, "CRITICAL")
            continue

        if command == "sets":
            show_sets(reading_history)
            continue

        if command in ("setmethods", "set_methods"):
            demonstrate_set_methods()
            continue

        if command in ("dictionaries", "dict"):
            show_dictionaries(reading_history)
            continue

        if command in ("dictmethods", "dict_methods"):
            demonstrate_dictionary_methods()
            continue

        if command == "comprehensions":
            show_comprehensions(reading_history)
            continue

        if command in ("references", "reference"):
            show_reference_demo()
            continue

        if command == "top3":
            show_highest_three(reading_history)
            continue

        if command == "mission":
            show_mission(mission_name, destination)
            continue

        if command == "search":
            search_history(reading_history)
            continue

        if command == "status":
            status_command(reading_history)
            continue

        if command == "log":
            show_log(reading_history)
            continue

        if command == "save":
            save_current_report(reading_history)
            continue

        if command == "newreport":
            create_report_file(reading_history)
            continue

        if command == "preview":
            show_file_preview(HISTORY_FILE)
            continue

        if command == "reset":
            reset_history(HISTORY_FILE)
            reading_history = []
            continue

        if command == "help":
            show_help()
            continue

        if command != "scan":
            print("Unknown command.")
            continue

        scan_readings, scan_safe, scan_warning = scan_sensors()

        if scan_readings:
            reading_history.extend(scan_readings)
            append_history(HISTORY_FILE, scan_readings)

        print(
            f"Scan complete: {len(scan_readings)} valid readings, "
            f"{scan_safe} safe, {scan_warning} warning/critical."
        )

    print("=" * 60)
    print("SESSION ENDED".center(60))
    print("=" * 60)


run_mission_control()

