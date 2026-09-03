print("=" * 60)
print("MISSION CONTROL v4.0 - CONTINUOUS MONITOR".center(60))
print("=" * 60)

total_valid = 0
safe_count = 0
warning_count = 0
temperature_total = 0
largest_temperature = None

while True:
    command = input("\nCommand [scan/report/shutdown]: ")

    if command == "shutdown":
        print("Shutting down Mission Control...")
        break

    if command == "report":
        print("\n--- CURRENT REPORT ---")
        print(f"Valid readings: {total_valid}")
        print(f"Safe readings:  {safe_count}")
        print(f"Warnings:       {warning_count}")

        if total_valid > 0:
            average = temperature_total / total_valid
            print(f"Average:        {average:.1f}")
            print(f"Highest:        {largest_temperature:.1f}")
        else:
            print("No valid sensor data yet.")

        continue

    if command != "scan":
        print("Unknown command.")
        continue

    for sensor_number in range(1, 6):
        temperature = float(
            input(f"Sensor {sensor_number} temperature: ")
        )

        if temperature < 0:
            print("Invalid reading - skipped.")
            continue

        total_valid += 1
        temperature_total += temperature

        if largest_temperature is None or temperature > largest_temperature:
            largest_temperature = temperature

        if temperature >= 100:
            print("CRITICAL - scan stopped")
            warning_count += 1
            break
        elif temperature > 80:
            print("WARNING")
            warning_count += 1
        else:
            print("SAFE")
            safe_count += 1

print("=" * 60)
print("SESSION ENDED".center(60))
print("=" * 60)
