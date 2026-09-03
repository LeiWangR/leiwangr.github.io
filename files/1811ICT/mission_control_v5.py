# ============================================================
# MISSION CONTROL v5.0
# Functional Sensor Monitor
# Week 5: Functions
# ============================================================

def classify_temperature(temperature, critical_limit=100):
    """Return the status for one valid temperature."""
    if temperature >= critical_limit:
        return "CRITICAL"
    elif temperature > 80:
        return "WARNING"
    else:
        return "SAFE"


def calculate_average(total, count):
    """Return the average, or None when there is no valid data."""
    if count == 0:
        return None

    return total / count


def update_largest(current_largest, value):
    """Return the largest value seen so far."""
    if current_largest is None or value > current_largest:
        return value

    return current_largest


def show_report(total_valid, safe_count, warning_count,
                temperature_total, largest_temperature):
    """Display the current Mission Control report."""
    print("\n--- CURRENT REPORT ---")
    print(f"Valid readings: {total_valid}")
    print(f"Safe readings: {safe_count}")
    print(f"Warnings: {warning_count}")

    average = calculate_average(temperature_total, total_valid)

    if average is None:
        print("No valid sensor data yet.")
    else:
        print(f"Average: {average:.1f}")
        print(f"Highest: {largest_temperature:.1f}")


def scan_sensors(total_valid, safe_count, warning_count,
                 temperature_total, largest_temperature):
    """Scan five sensors and return the updated mission state."""
    for sensor_number in range(1, 6):
        temperature = float(
            input(f"Sensor {sensor_number} temperature: ")
        )

        if temperature < 0:
            print("Invalid reading - skipped.")
            continue

        total_valid += 1
        temperature_total += temperature
        largest_temperature = update_largest(
            largest_temperature, temperature
        )

        status = classify_temperature(temperature)

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

    return (total_valid, safe_count, warning_count,
            temperature_total, largest_temperature)


def run_mission_control():
    """Run the Mission Control command loop."""
    total_valid = 0
    safe_count = 0
    warning_count = 0
    temperature_total = 0
    largest_temperature = None

    while True:
        command = input(
            "\nCommand [scan/report/shutdown]: "
        ).strip().lower()

        if command == "shutdown":
            print("Shutting down Mission Control...")
            break

        if command == "report":
            show_report(
                total_valid,
                safe_count,
                warning_count,
                temperature_total,
                largest_temperature
            )
            continue

        if command != "scan":
            print("Unknown command.")
            continue

        (total_valid, safe_count, warning_count,
         temperature_total, largest_temperature) = scan_sensors(
            total_valid,
            safe_count,
            warning_count,
            temperature_total,
            largest_temperature
        )


print("=" * 60)
print("MISSION CONTROL v5.0 - FUNCTIONS".center(60))
print("=" * 60)

run_mission_control()

print("=" * 60)
print("SESSION ENDED".center(60))
print("=" * 60)
