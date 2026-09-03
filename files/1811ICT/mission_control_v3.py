# ============================================================
# MISSION CONTROL v3.0 - LAUNCH DECISION ENGINE
# ============================================================

print("=" * 66)
print("MISSION CONTROL v3.0 - LAUNCH DECISION ENGINE".center(66))
print("=" * 66)

# -------------------- INPUT --------------------
commander = input("Commander: ")
mission = input("Mission name: ")
destination = input("Destination: ")

fuel = float(input("Fuel level (%): "))
wind = float(input("Wind speed (km/h): "))
temperature = float(input("Engine temperature: "))

primary_link = input("Primary link online? (yes/no): ") == "yes"
backup_link = input("Backup link online? (yes/no): ") == "yes"
emergency_lock = input("Emergency lock active? (yes/no): ") == "yes"

# ---------------- BOOLEAN QUESTIONS ----------------
fuel_ok = fuel >= 70
wind_ok = wind <= 40
temperature_ok = 10 <= temperature <= 80
communication_ok = primary_link or backup_link
lock_clear = not emergency_lock

launch_ready = (
    fuel_ok
    and wind_ok
    and temperature_ok
    and communication_ok
    and lock_clear
)

# ---------------- DIAGNOSTICS ----------------
print("\n" + "-" * 66)
print("SAFETY DIAGNOSTICS".center(66))
print("-" * 66)

print(f"Fuel OK:              {fuel_ok}")
print(f"Wind OK:              {wind_ok}")
print(f"Temperature OK:       {temperature_ok}")
print(f"Communication OK:     {communication_ok}")
print(f"Emergency lock clear: {lock_clear}")

print("-" * 66)

# ---------------- DECISION ----------------
if launch_ready:
    print(f"LAUNCH AUTHORISED - Commander {commander}")
    print(f"Mission {mission} cleared for {destination}.")
else:
    print("LAUNCH HOLD")
    print("Safety review:")

    if not fuel_ok:
        print(" - Fuel below 70%")

    if not wind_ok:
        print(" - Wind exceeds 40 km/h")

    if not temperature_ok:
        print(" - Temperature must be between 10 and 80")

    if not communication_ok:
        print(" - Primary and backup communication links are offline")

    if not lock_clear:
        print(" - Emergency lock is active")

print("=" * 66)
