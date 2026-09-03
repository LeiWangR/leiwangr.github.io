# ============================================================
# AUSTRALIAN SPACE MISSION CONTROL - VERSION 2.0
# Week 2: Strings, variables, input, conversion and output
# ============================================================

print("=" * 60)
print(" AUSTRALIAN SPACE MISSION CONTROL ".center(60, "="))
print(" Interactive Mission Planner - v2.0 ".center(60))
print("=" * 60)

# INPUT - mission identity
commander = input("\nCommander name: ")
mission_name = input("Mission name: ")
destination = input("Destination: ")

print("\nWelcome, " + commander + "!")
print("Configuring mission", mission_name, "to", destination + "...")

# INPUT - mission parameters
rocket_speed = float(input("\nRocket speed (km/h): "))
mission_hours = float(input("Mission duration (hours): "))
fuel_required = float(input("Fuel required (litres): "))
tank_capacity = float(input("Fuel tank capacity (litres): "))

# PROCESS
distance = rocket_speed * mission_hours
full_tanks = fuel_required // tank_capacity
fuel_remainder = fuel_required % tank_capacity
communication_delay = distance / 300000

# OUTPUT
print("\n" + "=" * 60)
print(" MISSION PLAN ".center(60, "="))
print("=" * 60)

print("Commander".ljust(28), commander)
print("Mission".ljust(28), mission_name)
print("Destination".ljust(28), destination)

print("-" * 60)

print("Rocket speed".ljust(28), rocket_speed, "km/h")
print("Mission duration".ljust(28), mission_hours, "hours")
print("Distance travelled".ljust(28), distance, "km")
print("Communication delay".ljust(28), communication_delay, "seconds")
print("Full fuel tanks".ljust(28), full_tanks)
print("Fuel remainder".ljust(28), fuel_remainder, "L")

print("=" * 60)
print(("MISSION " + mission_name + " CONFIGURED").center(60))
print("=" * 60)
