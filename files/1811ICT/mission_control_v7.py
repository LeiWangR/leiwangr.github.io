# ============================================================
# MISSION CONTROL v7.0
# Week 7: Strings and Text Data
# Based on Mission Control v6.0
# ============================================================

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

def scan_sensors():
    scan_readings = []
    safe_count = 0
    warning_count = 0

    for sensor_number in range(1, 6):
        temperature = float(input(f"Sensor {sensor_number} temperature: "))
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

def show_report(reading_history):
    print("\n--- CURRENT REPORT ---")
    total_valid = len(reading_history)
    print(f"Valid readings: {total_valid}")

    if not reading_history:
        print("No valid sensor data yet.")
        return

    temperatures = [reading[1] for reading in reading_history]
    statuses = [reading[2] for reading in reading_history]

    print(f"Safe readings: {statuses.count('SAFE')}")
    print(f"Warnings: {statuses.count('WARNING')}")
    print(f"Critical readings: {statuses.count('CRITICAL')}")

    average = sum(temperatures) / len(temperatures)
    print(f"Average: {average:.1f} C")
    print(f"Highest: {max(temperatures):.1f} C")
    print(f"Lowest: {min(temperatures):.1f} C")

def format_reading(reading):
    sensor_number, temperature, status = reading
    return f"Sensor {sensor_number:<2} | {temperature:>6.1f} C | {status:<8}"

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
        reading for reading in reading_history
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

def show_log(reading_history):
    print("\n--- MISSION LOG ---")

    if not reading_history:
        print("No valid sensor readings recorded.")
        return

    lines = []
    for reading in reading_history:
        lines.append(format_reading(reading))

    log = "\n".join(lines)
    print(log)
    print(f"\nLog contains {len(lines)} readings.")

def show_help():
    command_text = (
        "scan report history recent safe warning critical "
        "top3 mission search status log help shutdown"
    )

    commands = command_text.split()

    print("\n--- AVAILABLE COMMANDS ---")
    print(" | ".join(commands))

def run_mission_control():
    reading_history = []

    mission_name = input("Mission name: ").strip().title()
    destination = input("Destination: ").strip().title()

    show_header(f"MISSION CONTROL v7.0 — {mission_name}")
    print(f"Destination: {destination}")

    while True:
        command = input(
            "\nCommand [scan/report/history/recent/safe/warning/"
            "critical/top3/mission/search/status/log/help/shutdown]: "
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

        if command == "help":
            show_help()
            continue

        if command != "scan":
            print("Unknown command.")
            continue

        scan_readings, scan_safe, scan_warning = scan_sensors()
        reading_history.extend(scan_readings)

        print(
            f"Scan complete: {len(scan_readings)} valid readings, "
            f"{scan_safe} safe, {scan_warning} warning/critical."
        )

    print("=" * 60)
    print("SESSION ENDED".center(60))
    print("=" * 60)

run_mission_control()
