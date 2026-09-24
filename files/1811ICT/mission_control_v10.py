# ============================================================
# MISSION CONTROL v10.0
# Week 10: Object-Oriented Programming
# Based on Mission Control v9.0
# ============================================================

import sys

HISTORY_FILE = "mission_history.txt"
REPORT_FILE = "mission_report.txt"


def show_header(title):
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


# ---------------------------------------------------------------------
# Week 10: Classes and objects
# ---------------------------------------------------------------------

class SensorReading:
    """Represent one sensor reading."""

    VALID_STATUSES = {"SAFE", "WARNING", "CRITICAL"}

    def __init__(self, sensor_number, temperature, status):
        self.sensor_number = sensor_number
        self.temperature = temperature
        self.status = status

    def __str__(self):
        return (
            f"Sensor {self.sensor_number:<2} | "
            f"{self.temperature:>6.1f} C | "
            f"{self.status:<8}"
        )

    def is_safe(self):
        return self.status == "SAFE"

    def is_warning(self):
        return self.status == "WARNING"

    def is_critical(self):
        return self.status == "CRITICAL"


class MissionControl:
    """Manage mission information and sensor-reading objects."""

    VALID_STATUSES = {"SAFE", "WARNING", "CRITICAL"}

    def __init__(self, mission_name, destination):
        self.mission_name = mission_name
        self.destination = destination
        self.reading_history = []

    def add_reading(self, reading):
        self.reading_history.append(reading)

    def add_readings(self, readings):
        self.reading_history.extend(readings)

    def clear_history(self):
        self.reading_history.clear()

    def classify_temperature(self, temperature):
        if temperature < 0:
            return "INVALID"
        elif temperature >= 100:
            return "CRITICAL"
        elif temperature > 80:
            return "WARNING"
        else:
            return "SAFE"

    def scan_sensors(self):
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

            status = self.classify_temperature(temperature)

            if status == "INVALID":
                print("Invalid reading - skipped.")
                continue

            reading = SensorReading(
                sensor_number, temperature, status
            )
            scan_readings.append(reading)

            if reading.is_critical():
                print("CRITICAL - scan stopped")
                warning_count += 1
                break
            elif reading.is_warning():
                print("WARNING")
                warning_count += 1
            else:
                print("SAFE")
                safe_count += 1

        return scan_readings, safe_count, warning_count

    def load_history(self, filename):
        self.reading_history = []

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

                        if status not in SensorReading.VALID_STATUSES:
                            raise ValueError("invalid status")

                        reading = SensorReading(
                            sensor_number, temperature, status
                        )
                        self.reading_history.append(reading)

                    except ValueError:
                        print(
                            f"Warning: skipped invalid reading: {line}",
                            file=sys.stderr
                        )

        except FileNotFoundError:
            print(
                "No existing history file found. "
                "Starting a new mission log."
            )

    def append_history(self, filename, readings):
        with open(filename, "a") as file:
            for reading in readings:
                file.write(
                    f"{reading.sensor_number}|"
                    f"{reading.temperature}|"
                    f"{reading.status}\n"
                )

    def save_report(self, filename, report_lines):
        with open(filename, "w") as file:
            file.write("\n".join(report_lines))
            file.write("\n")

    def create_new_report(self, filename, report_lines):
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

    # -----------------------------------------------------------------
    # Week 9: Sets
    # -----------------------------------------------------------------

    def get_observed_statuses(self):
        return {reading.status for reading in self.reading_history}

    def get_sensor_numbers(self):
        return {reading.sensor_number for reading in self.reading_history}

    def show_sets(self):
        print("\n--- SET ANALYSIS ---")

        observed_statuses = self.get_observed_statuses()
        all_statuses = SensorReading.VALID_STATUSES

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

        sensor_numbers = self.get_sensor_numbers()
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

    def demonstrate_set_methods(self):
        print("\n--- SET METHODS DEMO ---")

        s1 = {"SAFE", "WARNING"}
        s2 = {"WARNING", "CRITICAL"}

        print(f"s1: {sorted(s1)}")
        print(f"s2: {sorted(s2)}")

        print("Union:", sorted(s1 | s2))
        print("Intersection:", sorted(s1 & s2))
        print("Difference s1 - s2:", sorted(s1 - s2))
        print("Symmetric difference:", sorted(s1 ^ s2))

        print("s1 subset of s2:", s1 <= s2)
        print("s1 proper subset of s2:", s1 < s2)
        print("s1 superset of s2:", s1 >= s2)
        print("s1 proper superset of s2:", s1 > s2)
        print("s1 and s2 disjoint:", s1.isdisjoint(s2))

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

    # -----------------------------------------------------------------
    # Week 9: Dictionaries
    # -----------------------------------------------------------------

    def demonstrate_dictionary_methods(self):
        print("\n--- DICTIONARY METHODS DEMO ---")

        data = {"SAFE": 5, "WARNING": 2}
        print("Starting dictionary:", data)

        data["CRITICAL"] = 1
        data["SAFE"] = 6
        print("After [] assignment:", data)

        print("keys():", list(data.keys()))
        print("values():", list(data.values()))
        print("items():", list(data.items()))

        print("get('SAFE'):", data.get("SAFE"))
        print("get('MAINTENANCE'):", data.get("MAINTENANCE"))
        print("get('MAINTENANCE', 0):", data.get("MAINTENANCE", 0))

        data.setdefault("WARNING", 0)
        data.setdefault("MAINTENANCE", 0)
        print("After setdefault():", data)

        data.update({"SAFE": 7, "OTHER": 0})
        print("After update():", data)

        removed = data.pop("OTHER")
        print("pop('OTHER') returned:", removed)
        print("After pop():", data)

        removed_pair = data.popitem()
        print("popitem() returned:", removed_pair)
        print("After popitem():", data)

        del data["CRITICAL"]
        print("After del data['CRITICAL']:", data)

        template = dict.fromkeys(
            ["SAFE", "WARNING", "CRITICAL"], 0
        )
        print("fromkeys():", template)

        left = {"SAFE": 5, "WARNING": 2}
        right = {"WARNING": 3, "CRITICAL": 1}
        merged = left | right
        print("Merged with |:", merged)

        data.clear()
        print("After clear():", data)

    def build_status_counts(self):
        counts = {}

        for reading in self.reading_history:
            status = reading.status
            counts[status] = counts.get(status, 0) + 1

        return counts

    def build_sensor_counts(self):
        counts = {}

        for reading in self.reading_history:
            sensor_number = reading.sensor_number
            counts[sensor_number] = counts.get(sensor_number, 0) + 1

        return counts

    def build_latest_readings(self):
        latest = {}

        for reading in self.reading_history:
            latest[reading.sensor_number] = reading

        return latest

    def show_dictionaries(self):
        print("\n--- DICTIONARY ANALYSIS ---")

        status_counts = self.build_status_counts()
        sensor_counts = self.build_sensor_counts()
        latest = self.build_latest_readings()

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
                print(latest[sensor_number])
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

    # -----------------------------------------------------------------
    # Week 9: Comprehensions and references
    # -----------------------------------------------------------------

    def show_comprehensions(self):
        print("\n--- COMPREHENSION EXAMPLES ---")

        safe_sensors = {
            reading.sensor_number
            for reading in self.reading_history
            if reading.is_safe()
        }

        average_by_sensor = {}

        for reading in self.reading_history:
            sensor_number = reading.sensor_number
            temperature = reading.temperature

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

    def show_reference_demo(self):
        print("\n--- REFERENCE DEMO ---")

        readings = [1, 2]
        mission_readings = readings

        print(f"Before mutation: readings = {readings}")
        print(
            "Before mutation: mission_readings = "
            f"{mission_readings}"
        )

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

    # -----------------------------------------------------------------
    # Existing Mission Control features from earlier weeks
    # -----------------------------------------------------------------

    def show_report(self):
        print("\n--- CURRENT REPORT ---")
        total_valid = len(self.reading_history)

        if not self.reading_history:
            print("No valid sensor data yet.")
            return []

        temperatures = [
            reading.temperature for reading in self.reading_history
        ]
        statuses = [
            reading.status for reading in self.reading_history
        ]

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

    def show_history(self):
        print("\n--- READING HISTORY ---")

        if not self.reading_history:
            print("No valid sensor readings recorded.")
            return

        for reading in self.reading_history:
            print(reading)

    def show_recent(self):
        print("\n--- RECENT READINGS ---")

        recent_readings = self.reading_history[-3:]

        if not recent_readings:
            print("No valid sensor readings recorded.")
            return

        for reading in recent_readings:
            print(reading)

    def show_status(self, required_status):
        matching_readings = [
            reading
            for reading in self.reading_history
            if reading.status == required_status
        ]

        print(f"\n--- {required_status} READINGS ---")

        if not matching_readings:
            print(f"No {required_status} readings recorded.")
            return

        for reading in matching_readings:
            print(reading)

    def show_highest_three(self):
        print("\n--- HIGHEST THREE TEMPERATURES ---")

        if not self.reading_history:
            print("No valid sensor readings recorded.")
            return

        temperatures = [
            reading.temperature for reading in self.reading_history
        ]
        temperatures.sort()

        for temperature in temperatures[-3:][::-1]:
            print(f"{temperature:.1f} C")

    def show_mission(self):
        print("\n--- MISSION INFORMATION ---")
        print(f"Mission: {self.mission_name}")
        print(f"Destination: {self.destination}")

        if len(self.mission_name) >= 3:
            print(f"Mission code: {self.mission_name[:3].upper()}")
        else:
            print("Mission code: " + self.mission_name.upper())

    def search_history(self):
        keyword = input("Search text: ").strip().lower()

        if keyword == "":
            print("Search text cannot be empty.")
            return

        matches = []

        for reading in self.reading_history:
            line = str(reading)

            if keyword in line.lower():
                matches.append(line)

        print("\n--- SEARCH RESULTS ---")

        if not matches:
            print("No matching readings found.")
        else:
            print("\n".join(matches))

    def status_command(self):
        status = input(
            "Enter status (SAFE/WARNING/CRITICAL): "
        ).strip().upper()

        if status in SensorReading.VALID_STATUSES:
            self.show_status(status)
        else:
            print("Invalid status.")

    def build_log_lines(self):
        return [str(reading) for reading in self.reading_history]

    def show_log(self):
        print("\n--- MISSION LOG ---")

        if not self.reading_history:
            print("No valid sensor readings recorded.")
            return

        lines = self.build_log_lines()
        log = "\n".join(lines)

        print(log)
        print(f"\nLog contains {len(lines)} readings.")

    def save_current_report(self):
        report_lines = self.show_report()

        if not report_lines:
            return

        self.save_report(REPORT_FILE, report_lines)
        print(f"Report saved to {REPORT_FILE}.")

    def create_report_file(self):
        report_lines = self.show_report()

        if not report_lines:
            return

        self.create_new_report(REPORT_FILE, report_lines)

    def show_file_preview(self, filename):
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

    def reset_history(self, filename):
        with open(filename, "w") as file:
            file.write("")

        self.clear_history()
        print(f"History file '{filename}' has been cleared.")

    def show_help(self):
        command_text = (
            "scan report history recent safe warning critical "
            "sets setmethods dictionaries dictmethods comprehensions "
            "references top3 mission search status log save newreport "
            "preview reset help shutdown"
        )

        commands = command_text.split()

        print("\n--- AVAILABLE COMMANDS ---")
        print(" | ".join(commands))

    def run(self):
        self.load_history(HISTORY_FILE)

        show_header(f"MISSION CONTROL v10.0 — {self.mission_name}")
        print(f"Destination: {self.destination}")
        print(
            f"Loaded {len(self.reading_history)} "
            "historical readings."
        )

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
                self.show_report()
                continue

            if command == "history":
                self.show_history()
                continue

            if command == "recent":
                self.show_recent()
                continue

            if command == "safe":
                self.show_status("SAFE")
                continue

            if command == "warning":
                self.show_status("WARNING")
                continue

            if command == "critical":
                self.show_status("CRITICAL")
                continue

            if command == "sets":
                self.show_sets()
                continue

            if command in ("setmethods", "set_methods"):
                self.demonstrate_set_methods()
                continue

            if command in ("dictionaries", "dict"):
                self.show_dictionaries()
                continue

            if command in ("dictmethods", "dict_methods"):
                self.demonstrate_dictionary_methods()
                continue

            if command == "comprehensions":
                self.show_comprehensions()
                continue

            if command in ("references", "reference"):
                self.show_reference_demo()
                continue

            if command == "top3":
                self.show_highest_three()
                continue

            if command == "mission":
                self.show_mission()
                continue

            if command == "search":
                self.search_history()
                continue

            if command == "status":
                self.status_command()
                continue

            if command == "log":
                self.show_log()
                continue

            if command == "save":
                self.save_current_report()
                continue

            if command == "newreport":
                self.create_report_file()
                continue

            if command == "preview":
                self.show_file_preview(HISTORY_FILE)
                continue

            if command == "reset":
                self.reset_history(HISTORY_FILE)
                continue

            if command == "help":
                self.show_help()
                continue

            if command != "scan":
                print("Unknown command.")
                continue

            scan_readings, scan_safe, scan_warning = self.scan_sensors()

            if scan_readings:
                self.add_readings(scan_readings)
                self.append_history(HISTORY_FILE, scan_readings)

            print(
                f"Scan complete: {len(scan_readings)} valid readings, "
                f"{scan_safe} safe, {scan_warning} warning/critical."
            )


def main():
    mission_name = input("Mission name: ").strip().title()
    destination = input("Destination: ").strip().title()

    mission = MissionControl(mission_name, destination)
    mission.run()

    print("=" * 60)
    print("SESSION ENDED".center(60))
    print("=" * 60)


if __name__ == "__main__":
    main()
