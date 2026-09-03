# ============================================================
# MISSION CONTROL v6.0
# Collection-Based Sensor Monitor
# Week 6: Lists and Tuples
# ============================================================

def show_header(title):
    """Display a Mission Control header."""
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


def classify_temperature(temperature):
    """Return the status for one temperature reading."""
    if temperature < 0:
        return "INVALID"
    elif temperature >= 100:
        return "CRITICAL"
    elif temperature > 80:
        return "WARNING"
    else:
        return "SAFE"


def scan_sensors():
    """Scan up to five sensors and return this scan's readings."""
    scan_readings = []

    for sensor_number in range(1, 6):
        temperature = float(
            input(f"Sensor {sensor_number} temperature: ")
        )

        status = classify_temperature(temperature)

        if status == "INVALID":
            print("Invalid reading - skipped.")
            continue

        reading = (sensor_number, temperature, status)
        scan_readings.append(reading)

        if status == "CRITICAL":
            print("CRITICAL - scan stopped")
            break
        elif status == "WARNING":
            print("WARNING")
        else:
            print("SAFE")

    return scan_readings


def show_report(reading_history):
    """Display statistics calculated from the reading history."""
    print("\n--- CURRENT REPORT ---")

    total_valid = len(reading_history)
    print(f"Valid readings: {total_valid}")

    if not reading_history:
        print("No valid sensor data yet.")
        return

    temperatures = [reading[1] for reading in reading_history]
    statuses = [reading[2] for reading in reading_history]

    safe_count = statuses.count("SAFE")
    warning_count = statuses.count("WARNING")
    critical_count = statuses.count("CRITICAL")

    average = sum(temperatures) / len(temperatures)

    print(f"Safe readings: {safe_count}")
    print(f"Warnings: {warning_count}")
    print(f"Critical readings: {critical_count}")
    print(f"Average: {average:.1f}")
    print(f"Highest: {max(temperatures):.1f}")
    print(f"Lowest: {min(temperatures):.1f}")


def show_history(reading_history):
    """Display every valid reading stored in the session."""
    print("\n--- READING HISTORY ---")

    if not reading_history:
        print("No valid sensor readings recorded.")
        return

    for sensor_number, temperature, status in reading_history:
        print(
            f"Sensor {sensor_number}: "
            f"{temperature:.1f} -> {status}"
        )


def show_recent(reading_history):
    """Display the three most recent valid readings."""
    print("\n--- RECENT READINGS ---")

    if not reading_history:
        print("No valid sensor readings recorded.")
        return

    for sensor_number, temperature, status in reading_history[-3:]:
        print(
            f"Sensor {sensor_number}: "
            f"{temperature:.1f} -> {status}"
        )


def show_status(reading_history, required_status):
    """Display readings matching one status."""
    matching_readings = [
        reading
        for reading in reading_history
        if reading[2] == required_status
    ]

    print(f"\n--- {required_status} READINGS ---")

    if not matching_readings:
        print(f"No {required_status} readings recorded.")
        return

    for sensor_number, temperature, status in matching_readings:
        print(
            f"Sensor {sensor_number}: "
            f"{temperature:.1f} -> {status}"
        )


def show_highest_three(reading_history):
    """Display the three highest recorded temperatures."""
    print("\n--- HIGHEST THREE TEMPERATURES ---")

    if not reading_history:
        print("No valid sensor readings recorded.")
        return

    temperatures = [reading[1] for reading in reading_history]
    temperatures.sort()

    for temperature in temperatures[-3:][::-1]:
        print(f"{temperature:.1f}")


def run_mission_control():
    """Run the main Mission Control command loop."""
    reading_history = []

    show_header("MISSION CONTROL v6.0 - COLLECTION MONITOR")

    while True:
        command = input(
            "\nCommand [scan/report/history/recent/"
            "safe/warning/critical/top3/shutdown]: "
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

        if command != "scan":
            print("Unknown command.")
            continue

        scan_readings = scan_sensors()
        reading_history.extend(scan_readings)

    print("=" * 60)
    print("SESSION ENDED".center(60))
    print("=" * 60)


run_mission_control()
